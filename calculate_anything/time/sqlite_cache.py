from typing import Generator, Iterable, List, Tuple

try:
    import sqlite3
except ImportError:  # pragma: no cover
    sqlite3 = None  # pragma: no cover
from threading import RLock
from calculate_anything import logging
from calculate_anything.time.data import CityData
from calculate_anything.utils import with_lock
from calculate_anything.utils.loaders import SqliteLoader
from calculate_anything.constants import (
    TIMEZONES_SQLITE_FILE_DEFAULT,
    TIMEZONES_SQLITE_FILE_USER,
    TIMEZONES_SQL_FILE,
)


logger = logging.getLogger(__name__)


class TimezoneSqliteCache:
    def __init__(self) -> None:
        super().__init__()
        self._db = None
        self._lock = RLock()

    @property
    def lock(self) -> RLock:
        return self._lock

    @with_lock
    def load(self) -> bool:
        if sqlite3 is None:
            return False  # pragma: no cover

        loader = SqliteLoader(TIMEZONES_SQLITE_FILE_USER)

        if not loader.load():
            loader = SqliteLoader(
                TIMEZONES_SQLITE_FILE_DEFAULT, TIMEZONES_SQL_FILE
            )

        # If second time loading fails we can't do anything about it
        if not loader.load():
            return False  # pragma: no cover
        self._db = loader.db
        self._post_init()
        return True

    def _post_init(self) -> None:
        try:
            cur = self._db.cursor()
            rows = cur.execute(
                '''SELECT city_name_chunks_max FROM meta LIMIT 1'''
            )
            self._city_name_chunks_max = next(iter(rows))[0]
        # This should not happen but capture it just in case
        # It is no fatal error
        except Exception as e:  # pragma: no cover
            self._city_name_chunks_max = None
            msg = 'Could not fetch city_name_chunks_max {}'
            msg = msg.format(e)
            logger.exception(msg)
        finally:
            cur.close()

    def _query_no_search_terms(
        self, city_name_search: str, exact: bool
    ) -> Generator[Tuple[int, str, str, str, str], None, None]:
        if not exact:
            primary_query = '''name_alias LIKE ? || '%' '''
            param = city_name_search
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
            '''  # nosec

        query = query.format(primary_query)

        cur = self._db.cursor()
        for row in cur.execute(query, (param, city_name_search)):
            yield row
        cur.close()

    def _query_search_terms(
        self, city_name_search: str, search_terms: Iterable[str], exact: bool
    ) -> Generator[Tuple[int, str, str, str, str], None, None]:
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
                ['iso2 = ?', 'iso3 = ?', 'name_alias LIKE ?']
            )
            countries_params.extend(
                [search_term_upper, search_term_upper, search_term]
            )

            states_query.append('s.name LIKE ?')
            states_params.append(search_term)

            timezones_query.append('t.name LIKE ?')
            timezones_params.append(search_term)

        countries_query = ' OR '.join(countries_query)
        states_query = ' OR '.join(states_query)
        timezones_query = ' OR '.join(timezones_query)

        if not exact:
            cities_query = '''name_alias LIKE ? || '%' '''
            cities_param = city_name_search
        else:
            cities_query = 'name_alias = ?'
            cities_param = city_name_search

        params = [
            cities_param,
            *countries_params,
            *states_params,
            *timezones_params,
            city_name_search,
        ]

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
            '''  # nosec

        query = query.format(
            cities_query, countries_query, states_query, timezones_query
        )

        cur = self._db.cursor()
        for row in cur.execute(query, params):
            yield row
        cur.close()

    def get(
        self, city_name_search: str, *search_terms: str, exact: bool = False
    ) -> List[CityData]:
        # Allow user to use underscore in LIKE
        city_name_search = city_name_search.replace('?', '')
        search_terms = map(lambda s: s.replace('?', ''), search_terms)
        search_terms = list(search_terms)

        if not search_terms:
            gen = self._query_no_search_terms(city_name_search, exact=exact)
        else:
            gen = self._query_search_terms(
                city_name_search, search_terms, exact=exact
            )

        cities = []
        for row in gen:
            _id, name, state_name, country_name, country_iso, tz_name = row
            cities.append(
                {
                    'id': _id,
                    'name': name,
                    'country': country_name,
                    'cc': country_iso,
                    'state': state_name,
                    'timezone': tz_name,
                }
            )

        return cities

    @with_lock
    def close_db(self):
        if self._db is None:
            return  # pragma: no cover
        self._db.close()
        logger.info('Database closed')
