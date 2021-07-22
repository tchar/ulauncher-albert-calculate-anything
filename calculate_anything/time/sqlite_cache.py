import os
import shutil
from datetime import datetime
import json
from functools import wraps
from threading import RLock
try:
    import sqlite3
except ImportError:
    sqlite3 = None
from .json_cache import TimezoneJsonCache
from .. import logging
from ..utils import Singleton
from ..constants import MAIN_DIR, TIMEZONES_SQLITE_FILE_DEFAULT, TIMEZONES_SQLITE_FILE_USER, TIMEZONES_SQL_FILE


def lock(func):
    @wraps(func)
    def _wrapper(self, *args, **kwargs):
        with self._lock:
            return func(self, *args, **kwargs)
    return _wrapper


class SqliteTimezoneCache(TimezoneJsonCache, metaclass=Singleton):
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._db = None
        if sqlite3 is None:
            super().__init__()
            return

        sql_filepath = os.path.join(MAIN_DIR, 'data', 'time', 'timezones.sql')
        if not os.path.isfile(sql_filepath):
            super().__init__()
            return

        self._last_clear_cache_timestamp = datetime.now().timestamp()
        self._lock = RLock()
        if not self._init_db(TIMEZONES_SQLITE_FILE_USER, load_only=True):
            self._init_db(TIMEZONES_SQLITE_FILE_DEFAULT)

        self._init_cache()
        self._post_init()

    @lock
    def _init_db(self, file_path, load_only=False):
        MODE_LOAD_ONLY = 1
        MODE_LOAD = MODE_LOAD_ONLY << 1
        MODE_CREATE = MODE_LOAD << 2
        MODE_DELETE = MODE_LOAD << 3
        MODE_MEMORY = MODE_LOAD << 4

        sqlite_file_exists = os.path.exists(file_path)
        if sqlite_file_exists:
            sqlite_file_mtime = os.path.getmtime(file_path)
        elif load_only:
            return False
        else:
            sqlite_file_mtime = 0

        sql_file_exists = os.path.exists(TIMEZONES_SQL_FILE)
        if sql_file_exists:
            sql_file_mtime = os.path.getmtime(TIMEZONES_SQL_FILE)
        else:
            sql_file_mtime = 0

        if load_only:
            mode = MODE_LOAD_ONLY
        elif sqlite_file_exists and sqlite_file_exists and sqlite_file_mtime >= sql_file_mtime:
            mode = MODE_LOAD
        elif sqlite_file_exists and sql_file_exists and sqlite_file_mtime < sql_file_mtime:
            mode = MODE_DELETE | MODE_CREATE
        elif not sqlite_file_exists:
            mode = MODE_CREATE
        else:
            mode = MODE_LOAD

        if mode & (MODE_LOAD | MODE_LOAD_ONLY):
            try:
                self._db = db = sqlite3.connect(file_path,
                                                check_same_thread=False)
                db.cursor().execute('PRAGMA foreign_keys = ON;').close()
                self._logger.info(
                    'Loaded timezone database: {}'.format(file_path))
            except sqlite3.DatabaseError as e:
                self._logger.exception(
                    'Could not read database file {}: {}'.format(file_path, e))
                mode |= MODE_DELETE
            except Exception as e:
                self._logger.error(
                    'Got unexpected error when reading database file: {}'.format(e))
                mode |= MODE_DELETE

        if mode & MODE_LOAD_ONLY:
            # Return True only if mode did not change
            return mode == MODE_LOAD_ONLY

        if mode & MODE_DELETE:
            try:
                if os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                else:
                    os.remove(file_path)
                self._logger.info('Found new timezones, cleared database')
            except Exception as e:
                self._logger.exception(
                    'Got unexpected exception when trying to remove the database: {}'.format(e))
                mode = MODE_MEMORY

        if mode & (MODE_CREATE | MODE_MEMORY):
            with open(TIMEZONES_SQL_FILE, 'r') as f:
                data = f.read()
            if mode & MODE_CREATE:
                try:
                    self._db = db = sqlite3.connect(
                        file_path, check_same_thread=False)
                    self._logger.info(
                        'Did not find {}, created from scratch'.format(file_path))
                except Exception as e:
                    self._logger.exception(
                        'Got unexpected exception when trying to create the database: {}'.format(e))
                    mode |= MODE_MEMORY
            if mode & MODE_MEMORY:
                self._db = db = sqlite3.connect(
                    ':memory:', check_same_thread=False)
                self._logger.info('Fell back to memory')
            cursor = db.cursor()
            cursor.executescript(data)
            cursor.execute('PRAGMA foreign_keys = ON;')
            db.commit()
            cursor.close()

    def _init_cache(self):
        db = sqlite3.connect(':memory:', check_same_thread=False)
        cur = db.cursor()
        cur.execute('PRAGMA foreign_keys = ON;')
        cur.execute('''CREATE TABLE IF NOT EXISTS queries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    key STRING UNIQUE COLLATE NOCASE,
                    timestamp DATETIME DEFAULT (DATETIME('now', 'localtime')))''')

        cur.execute('''CREATE TABLE IF NOT EXISTS results (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data_id INTEGER UNIQUE,
                    data JSON)''')

        cur.execute('''CREATE TABLE IF NOT EXISTS queries_results (
                    query_id INTEGER,
                    result_id INTEGER,
                    result_order INTEGER,
                    FOREIGN KEY(query_id) REFERENCES queries(id) ON DELETE CASCADE,
                    FOREIGN KEY(result_id) REFERENCES results(data_id) ON DELETE CASCADE)''')

        cur.execute(
            '''CREATE INDEX queries_timestamp_idx ON queries(timestamp)''')
        cur.execute(
            '''CREATE INDEX queries_key_idx ON queries(key COLLATE NOCASE)''')
        cur.execute(
            '''CREATE INDEX queries_results_result_order_idx ON queries_results(result_order)''')
        db.commit()
        cur.close()
        self._db_cache = db

    def _post_init(self):
        try:
            cur = self._db.cursor()
            rows = cur.execute(
                '''SELECT city_name_chunks_max FROM meta LIMIT 1''')
            self._city_name_chunks_max = next(iter(rows))[0]
        except Exception as e:
            self._city_name_chunks_max = None
            self._logger.exception(
                'Got exception when trying to fetch city_name_chunks_max: {}'.format(e))
        finally:
            cur.close()

    def _query_no_search_terms(self, city_name_search, exact):
        # Allow user to use underscore
        if not exact:
            primary_query = 'city_name_alias LIKE ?'
            param = city_name_search + '%'
        else:
            primary_query = 'city_name_alias = ?'
            param = city_name_search

        query = '''SELECT id city_id, name city_name, state_name, country_name, country_iso2, timezone
            FROM view_search_by_city_name
            WHERE name_alias LIKE ?
            GROUP BY id
            ORDER BY (name_alias = ?) DESC, population DESC
            LIMIT 10
            '''.format(primary_query)

        cur = self._db.cursor()
        for row in cur.execute(query, (param, city_name_search)):
            yield row
        cur.close()

    def _query_search_terms(self, city_name_search, search_terms, exact):
        countries_query = []
        countries_params = []

        states_query = []
        states_params = []

        timezones_query = []
        timezones_params = []
        
        for search_term in search_terms:
            search_term_upper = search_term.upper()
            search_term = '{}%'.format(search_term)

            countries_query.extend(['iso2 = ?', 'iso3 = ?', 'name_alias LIKE ?'])
            countries_params.extend([search_term_upper, search_term_upper, search_term])
            
            states_query.append('s.name LIKE ?')
            states_params.append(search_term)
            
            timezones_query.append('t.name LIKE ?')
            timezones_params.append(search_term)

        countries_query = ' OR '.join(countries_query)
        states_query = ' OR '.join(states_query)
        timezones_query = ' OR '.join(timezones_query)

        if not exact:
            cities_query = 'name_alias LIKE ?'
            cities_param = city_name_search + '%'
        else:
            cities_query = 'name_alias = ?'
            cities_param =city_name_search

        params = [cities_param, *countries_params, *states_params, *timezones_params, city_name_search]

        query = '''SELECT
            city.id city_id, city.name city_name, city.state_name,
            city.country_name, city.country_iso2, city.timezone
            FROM (
                SELECT * FROM view_search_by_city_name
                WHERE {}
                GROUP BY id, country_id, state_id
            ) city
            LEFT JOIN (
                SELECT * FROM view_search_by_country_name
                WHERE {}
                GROUP BY id
            ) country ON country.id = city.country_id
            LEFT JOIN (
                SELECT * FROM cities ct
                INNER JOIN cities_states cs ON cs.city_id = ct.id
                INNER JOIN states s ON s.id = cs.state_id
                WHERE {}
                GROUP BY ct.id, s.id
            ) state ON state.id = city.state_id
            LEFT JOIN (
                SELECT ct.id city_id
                FROM cities ct
                INNER JOIN timezones t ON t.id = ct.timezone_id
                WHERE {}
            ) tz ON tz.city_id = city.id
            WHERE country.id IS NOT NULL OR state.id IS NOT NULL or tz.city_id IS NOT NULL
            ORDER BY (city.name_alias = ?) DESC, city.population DESC
            '''.format(cities_query, countries_query, states_query, timezones_query)

        cur = self._db.cursor()
        for row in cur.execute(query, params):
            yield row
        cur.close()

    @lock
    def _cache_results(self, city_name_search, search_terms, cities):
        city_name_search = city_name_search.replace('::', '')
        if search_terms:
            result_keys = []
            for search_term in search_terms:
                result_key = city_name_search + '::' + \
                    search_term.replace('::', '')
                result_keys.append(result_key)
        else:
            result_keys = [city_name_search]

        db_cache = self._db_cache
        cursor = db_cache.cursor()
        for result_key in result_keys:
            cursor.execute('''INSERT OR REPLACE INTO queries (key, timestamp)
                            VALUES (?, datetime('now', 'localtime'))''', (result_key,))
            qid = cursor.lastrowid
            for i, city in enumerate(cities):
                cursor.execute('''INSERT OR IGNORE INTO
                            results (data_id, data)
                            VALUES (?, ?)''', (city['id'], json.dumps(city),))
                cursor.execute('''INSERT OR IGNORE INTO
                            queries_results (query_id, result_id, result_order)
                            VALUES (?, ?, ?)''', (qid, city['id'], i))
        db_cache.commit()
        cursor.close()

    @lock
    def _get_from_cached(self, city_name_search, search_terms):
        city_name_search = city_name_search.replace('::', '')
        result_keys = []
        if search_terms:
            for search_term in search_terms:
                result_key = city_name_search + '::' + \
                    search_term.replace('::', '')
                result_keys.append(result_key)
        else:
            result_keys = [city_name_search]

        query = ['?'] * len(result_keys)
        query = ','.join(query)

        db_cache = self._db_cache
        cursor = db_cache.cursor()
        cities = []
        for row in cursor.execute('''SELECT r.data FROM
            queries q
            INNER JOIN queries_results qr ON qr.query_id = q.id
            INNER JOIN results r ON qr.result_id = r.data_id
            WHERE q.key IN ({})
            GROUP BY r.data_id
            ORDER BY qr.result_order ASC'''.format(query), result_keys):
            city = json.loads(row[0])
            cities.append(city)
        cursor.close()
        return cities

    @lock
    def _clear_cache(self):
        time_diff = datetime.now().timestamp() - self._last_clear_cache_timestamp
        if time_diff <= 7200:
            return
        db_cache = self._db_cache
        cursor = db_cache.cursor()
        cursor.execute('''DELETE FROM queries
                        WHERE datetime(timestamp, '+2 hour') < datetime('now', 'localtime')''')
        db_cache.commit()
        cursor.close()
        self._last_clear_cache_timestamp = datetime.now().timestamp()
        self._logger.info('Cleared cache')

    def get(self, city_name_search, *search_terms, exact=False):
        if self._db is None:
            return super().get(city_name_search, *search_terms)

        city_name_search = city_name_search.replace('?', '')
        search_terms = map(lambda s: s.replace('?', ''), search_terms)
        search_terms = list(search_terms)

        if not exact:
            cities = self._get_from_cached(city_name_search, search_terms)
            if cities:
                self._clear_cache()
                self._logger.info('Returning cached city results')
                return cities

        if not search_terms:
            gen = self._query_no_search_terms(city_name_search, exact=exact)
        else:
            gen = self._query_search_terms(
                city_name_search, search_terms, exact=exact)

        cities = []
        for row in gen:
            _id, city_name, state_name, country_name, country_iso, timezone_name = row
            cities.append({
                'id': _id,
                'name': city_name,
                'country': country_name,
                'cc': country_iso,
                'state': state_name,
                'timezone': timezone_name
            })

        self._clear_cache()
        if not exact:
            self._cache_results(city_name_search, search_terms, cities)

        return cities

    @lock
    def close_db(self):
        if self._db is None:
            return
        self._db.close()
        self._logger.info('Database closed')
