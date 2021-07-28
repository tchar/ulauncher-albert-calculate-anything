import os
import shutil
from datetime import datetime
import json
from threading import RLock
try:
    import sqlite3
except ImportError:
    sqlite3 = None
from calculate_anything import logging
from calculate_anything.utils import lock
from calculate_anything.constants import (
    MAIN_DIR, TIMEZONES_SQLITE_FILE_DEFAULT,
    TIMEZONES_SQLITE_FILE_USER, TIMEZONES_SQL_FILE
)


class TimezoneSqliteCache:
    def __init__(self):
        super().__init__()
        self._logger = logging.getLogger(__name__)
        self._db = None
        self._lock = RLock()

    @lock
    def load(self):
        if sqlite3 is None:
            return False

        sql_filepath = os.path.join(MAIN_DIR, 'data', 'time', 'timezones.sql')
        if not os.path.isfile(sql_filepath):
            return False

        if not self._init_db(TIMEZONES_SQLITE_FILE_USER, load_only=True):
            self._init_db(TIMEZONES_SQLITE_FILE_DEFAULT)

        self._post_init()
        return True

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
        elif sqlite_file_exists and sqlite_file_exists and \
                sqlite_file_mtime >= sql_file_mtime:
            mode = MODE_LOAD
        elif sqlite_file_exists and sql_file_exists and \
                sqlite_file_mtime < sql_file_mtime:
            mode = MODE_DELETE | MODE_CREATE
        elif not sqlite_file_exists:
            mode = MODE_CREATE
        else:
            mode = MODE_LOAD

        if mode & (MODE_LOAD | MODE_LOAD_ONLY):
            try:
                self._db = db = sqlite3.connect(
                    file_path,
                    check_same_thread=False,
                    cached_statements=500
                )
                db.cursor().execute('PRAGMA foreign_keys = ON;').close()
                self._logger.info(
                    'Loaded timezone database: {}'.format(file_path))
            except sqlite3.DatabaseError as e:
                self._logger.exception(
                    'Could not read database file {}: {}'.format(file_path, e))
                mode |= MODE_DELETE
            except Exception as e:
                self._logger.exception(
                    'Got unexpected error when reading database file: {}'
                    .format(e))
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
                    'Got unexpected exception when trying to remove the '
                    'database: {}'.format(e))
                mode = MODE_MEMORY

        if mode & (MODE_CREATE | MODE_MEMORY):
            with open(TIMEZONES_SQL_FILE, 'r') as f:
                data = f.read()
            if mode & MODE_CREATE:
                try:
                    self._db = db = sqlite3.connect(
                        file_path,
                        check_same_thread=False,
                        cached_statements=500
                    )
                    self._logger.info(
                        'Did not find {}, created from scratch'
                        .format(file_path))
                except Exception as e:
                    self._logger.exception(
                        'Got unexpected exception when trying to create the '
                        'database: {}'.format(e))
                    mode |= MODE_MEMORY
            if mode & MODE_MEMORY:
                self._db = db = sqlite3.connect(
                    ':memory:',
                    check_same_thread=False,
                    cached_statements=500
                )
                self._logger.info('Fell back to memory')
            cursor = db.cursor()
            cursor.executescript(data)
            cursor.execute('PRAGMA foreign_keys = ON;')
            db.commit()
            cursor.close()

    def _post_init(self):
        try:
            cur = self._db.cursor()
            rows = cur.execute(
                '''SELECT city_name_chunks_max FROM meta LIMIT 1''')
            self._city_name_chunks_max = next(iter(rows))[0]
        except Exception as e:
            self._city_name_chunks_max = None
            self._logger.exception(
                'Got exception when trying to fetch city_name_chunks_max: {}'
                .format(e))
        finally:
            cur.close()

    def _query_no_search_terms(self, city_name_search, exact):
        # Allow user to use underscore
        if not exact:
            primary_query = 'name_alias LIKE ?'
            param = city_name_search + '%'
        else:
            primary_query = 'name_alias = ?'
            param = city_name_search

        query = '''SELECT id city_id, name city_name, state_name, country_name,
                country_iso2, timezone
            FROM view_search_by_city_name
            WHERE {}
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

            countries_query.extend(
                ['iso2 = ?', 'iso3 = ?', 'name_alias LIKE ?'])
            countries_params.extend(
                [search_term_upper, search_term_upper, search_term])

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
            cities_param = city_name_search

        params = [cities_param, *countries_params, *
                  states_params, *timezones_params, city_name_search]

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
            WHERE country.id IS NOT NULL OR state.id IS NOT NULL OR
                tz.city_id IS NOT NULL
            ORDER BY (city.name_alias = ?) DESC, city.population DESC
            '''.format(cities_query, countries_query,
                       states_query, timezones_query)

        cur = self._db.cursor()
        for row in cur.execute(query, params):
            yield row
        cur.close()

    def get(self, city_name_search, *search_terms, exact=False):
        city_name_search = city_name_search.replace('?', '')
        search_terms = map(lambda s: s.replace('?', ''), search_terms)
        search_terms = list(search_terms)

        if not search_terms:
            gen = self._query_no_search_terms(city_name_search, exact=exact)
        else:
            gen = self._query_search_terms(
                city_name_search, search_terms, exact=exact)

        cities = []
        for row in gen:
            _id, name, state_name, country_name, country_iso, tz_name = row
            cities.append({
                'id': _id,
                'name': name,
                'country': country_name,
                'cc': country_iso,
                'state': state_name,
                'timezone': tz_name
            })

        return cities

    @lock
    def close_db(self):
        if self._db is None:
            return
        self._db.close()
        self._logger.info('Database closed')
