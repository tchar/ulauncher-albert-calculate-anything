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
from .cache import TimezoneCache
from .. import logging
from ..utils import Singleton
from ..constants import TIMEZONE_SQLITE_FILE, MAIN_DIR


def lock(func):
    @wraps(func)
    def _wrapper(self, *args, **kwargs):
        with self._lock:
            return func(self, *args, **kwargs)
    return _wrapper


class SqliteTimezoneCache(TimezoneCache, metaclass=Singleton):
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
        self.__init_db()

    @lock
    def __init_db(self):
        MODE_CREATE = 1
        MODE_DELETE = 2
        MODE_LOAD = 3
        MODE_MEMORY = 4

        mode = MODE_LOAD

        sqlite_file_exists = os.path.exists(TIMEZONE_SQLITE_FILE)
        if sqlite_file_exists:
            sqlite_file_mtime = os.path.getmtime(TIMEZONE_SQLITE_FILE)
        else:
            sqlite_file_mtime = 0

        sql_filepath = os.path.join(MAIN_DIR, 'data', 'time', 'timezones.sql')
        sql_file_exists = os.path.exists(sql_filepath)
        if sql_file_exists:
            sql_file_mtime = os.path.getmtime(sql_filepath)
        else:
            sql_file_mtime = 0

        if sqlite_file_exists and sqlite_file_exists and sqlite_file_mtime >= sql_file_mtime:
            mode = MODE_LOAD
        elif sqlite_file_exists and sql_file_exists and sqlite_file_mtime < sql_file_mtime:
            mode = MODE_DELETE
        elif not sqlite_file_exists:
            mode = MODE_CREATE
        else:
            mode = MODE_LOAD

        if mode == MODE_LOAD:
            try:
                db = sqlite3.connect(TIMEZONE_SQLITE_FILE,
                                     check_same_thread=False)
                db.cursor().execute('PRAGMA foreign_keys = ON;').close()
                self._logger.info('Loaded timezone database')
            except sqlite3.DatabaseError as e:
                self._logger.exception(
                    'Could not read database file {}: {}'.format(TIMEZONE_SQLITE_FILE, e))
                mode = MODE_DELETE
            except Exception as e:
                self._logger.error(
                    'Got unexpected error when reading database file: {}'.format(e))
                mode = MODE_DELETE

        if mode == MODE_DELETE:
            try:
                if os.path.isdir(TIMEZONE_SQLITE_FILE):
                    shutil.rmtree(TIMEZONE_SQLITE_FILE)
                else:
                    os.remove(TIMEZONE_SQLITE_FILE)
                mode = MODE_CREATE
                self._logger.info('Found new timezones, cleared database')
            except Exception as e:
                self._logger.exception(
                    'Got unexpected exception when trying to remove the database: {}'.format(e))
                mode = MODE_MEMORY

        if mode in [MODE_CREATE, MODE_MEMORY]:
            with open(sql_filepath, 'r') as f:
                data = f.read()
            if mode == MODE_CREATE:
                try:
                    db = sqlite3.connect(
                        TIMEZONE_SQLITE_FILE, check_same_thread=False)
                    self._logger.info(
                        'Did not find {}, created from scratch'.format(TIMEZONE_SQLITE_FILE))
                except Exception as e:
                    self._logger.exception(
                        'Got unexpected exception when trying to create the database: {}'.format(e))
                    mode = MODE_MEMORY
            if mode == MODE_MEMORY:
                db = sqlite3.connect(':memory:', check_same_thread=False)
                self._logger.info('Fell back to memory')
            cursor = db.cursor()
            cursor.executescript(data)
            cursor.execute('PRAGMA foreign_keys = ON;')
            db.commit()
            cursor.close()

        self._db = db
        self.__init_cache()

    def __init_cache(self):
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
                    FOREIGN KEY(query_id) REFERENCES queries(id) ON DELETE CASCADE,
                    FOREIGN KEY(result_id) REFERENCES results(data_id) ON DELETE CASCADE)''')

        cur.execute(
            '''CREATE INDEX queries_timestamp_idx ON queries(timestamp)''')
        cur.execute(
            '''CREATE INDEX queries_key_idx ON queries(key COLLATE NOCASE)''')
        db.commit()
        cur.close()
        self._db_cache = db

    def _query_no_search_terms(self, city_name, exact):
        # Allow user to use underscore
        city_name = city_name.replace('%', '')

        if not exact:
            primary_query = 'cta.name LIKE ?'
            param = city_name + '%'
        else:
            primary_query = 'cta.name = ?'
            param = city_name

        cur = self._db.cursor()
        for row in cur.execute('''SELECT j.city_id, j.city_name, j.state_name, j.country_name, j.country_iso, j.timezone_name FROM 
            cities ct INNER JOIN (
                SELECT ct.id city_id, cta.name city_name, s.name state_name, ca.name country_name, c.iso2 country_iso, t.name timezone_name
                FROM cities ct
                INNER JOIN states s ON s.id = ct.state_id
                INNER JOIN timezones t ON t.id = ct.timezone_id
                LEFT OUTER JOIN cities_countries cc ON cc.city_id = ct.id
                LEFT OUTER JOIN countries c ON c.id = cc.country_id
                INNER JOIN countries_aliases ca ON ca.country_id = c.id
                INNER JOIN cities_aliases cta ON cta.city_id = ct.id
                WHERE {}
                GROUP BY ct.id
            ) j ON j.city_id = ct.id
            ORDER BY ct.population DESC
            LIMIT 10'''.format(primary_query), (param,)):
            yield row
        cur.close()

    def _query_search_terms(self, city_name, search_terms, exact):
        # Allow user to use underscore
        city_name = city_name.replace('%', '')
        search_terms = map(lambda s: s.replace('%', ''), search_terms)
        extra_query = []
        params = []
        for search_term in search_terms:
            search_term_upper = search_term.upper()
            search_term = search_term.replace('%', '') + '%'
            params.extend([search_term_upper, search_term_upper,
                          search_term, search_term, search_term])
            extra_query.append(
                'c.iso2 = ? OR c.iso3 = ?OR ca.name LIKE ? OR s.name LIKE ? OR t.name LIKE ?')

        if not exact:
            primary_query = 'cta.name LIKE ?'
            params.insert(0, city_name + '%')
        else:
            primary_query = 'cta.name = ?'
            params.insert(0, city_name)
        extra_query = ' OR '.join(extra_query)

        q = primary_query + ' AND ' + extra_query
        for p in params:
            q = q.replace('?', '\'' + p + '\'', 1)

        cur = self._db.cursor()
        for row in cur.execute('''SELECT j.city_id, j.city_name, j.state_name, j.country_name, j.country_iso, j.timezone_name FROM 
            cities ct INNER JOIN (
                SELECT ct.id city_id, cta.name city_name, s.name state_name, ca.name country_name, c.iso2 country_iso, t.name timezone_name
                FROM cities ct
                INNER JOIN states s ON s.id = ct.state_id
                INNER JOIN timezones t ON t.id = ct.timezone_id
                LEFT OUTER JOIN cities_countries cc ON cc.city_id = ct.id
                LEFT OUTER JOIN countries c ON c.id = cc.country_id
                INNER JOIN countries_aliases ca ON ca.country_id = c.id
                INNER JOIN cities_aliases cta ON cta.city_id = ct.id
                WHERE {} AND ({})
                GROUP BY ct.id
            ) j ON j.city_id = ct.id
            ORDER BY ct.population DESC'''.format(primary_query, extra_query), params):
            yield row
        cur.close()

    @lock
    def _cache_results(self, city_name, search_terms, cities):
        city_name = city_name.replace('::', '')
        if search_terms:
            result_keys = []
            for search_term in search_terms:
                result_key = city_name + '::' + search_term.replace('::', '')
                result_keys.append(result_key)
        else:
            result_keys = [city_name]

        db_cache = self._db_cache
        cursor = db_cache.cursor()
        for result_key in result_keys:
            cursor.execute('''INSERT OR REPLACE INTO queries (key, timestamp)
                            VALUES (?, datetime('now', 'localtime'))''', (result_key,))
            qid = cursor.lastrowid
            for city in cities:
                cursor.execute('''INSERT OR IGNORE INTO results (data_id, data)
                            VALUES (?, ?)''', (city['id'], json.dumps(city),))
                cursor.execute('''INSERT OR IGNORE INTO queries_results (query_id, result_id)
                            VALUES (?, ?)''', (qid, city['id']))
        db_cache.commit()
        cursor.close()

    @lock
    def _get_from_cached(self, city_name, search_terms):
        city_name = city_name.replace('::', '')
        result_keys = []
        if search_terms:
            for search_term in search_terms:
                result_key = city_name + '::' + search_term.replace('::', '')
                result_keys.append(result_key)
        else:
            result_keys = [city_name]

        query = ['?'] * len(result_keys)
        query = ','.join(query)

        db_cache = self._db_cache
        cursor = db_cache.cursor()
        cities = []
        for row in cursor.execute('''SELECT r.data FROM
            queries q
            INNER JOIN queries_results qr ON qr.query_id = q.id
            INNER JOIN results r ON qr.result_id = r.data_id
            WHERE q.key IN ({}) ORDER BY r.id ASC'''.format(query), result_keys):
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
        self._logger.info('Cleared cache')

    def get(self, city_name, *search_terms, exact=False):
        if self._db is None:
            return super().get(city_name, *search_terms)

        if not exact:
            cities = self._get_from_cached(city_name, search_terms)
            if cities:
                self._clear_cache()
                self._logger.info('Returning cached city results')
                return cities

        if not search_terms:
            gen = self._query_no_search_terms(city_name, exact=exact)
        else:
            gen = self._query_search_terms(
                city_name, search_terms, exact=exact)

        cities = []
        for row in gen:
            _id, name, state_name, country_name, country_iso, timezone_name = row
            cities.append({
                'id': _id,
                'name': name,
                'country': country_name,
                'cc': country_iso,
                'state': state_name,
                'timezone': timezone_name
            })

        self._clear_cache()
        if not exact:
            self._cache_results(city_name, search_terms, cities)

        return cities

    @lock
    def close_db(self):
        if self._db is None:
            return
        self._db.close()
        self._logger.info('Database closed')
