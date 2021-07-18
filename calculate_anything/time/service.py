import re
from .sqlite_cache import SqliteTimezoneCache
from ..utils import Singleton

class TimezoneService(metaclass=Singleton):
    def __init__(self):
        self._default_cities = []

    def get(self, name, *search_terms):
        return SqliteTimezoneCache().get(name, *search_terms)

    def get_defaults(self):
        return self._default_cities

    def set_default_cities(self, default_cities):
        self._default_cities = default_cities

    @staticmethod
    def parse_default_cities(default_cities_str):
        regex = re.compile(r'^(.*)\s+([a-z]{2})$', flags=re.IGNORECASE)

        default_cities = default_cities_str.strip().split(',')
        cities_found = []
        for default_city in default_cities:
            default_city = default_city.strip().lower()
            # Check for country code. It is messy but avoids keeping a regex 
            matches = regex.findall(default_city)
            country_code = None
            if matches:
                default_city, country_code = matches[0]
                default_city = default_city.strip()
                country_code = country_code.upper()
            if country_code:
                cities_found_tmp = SqliteTimezoneCache().get(default_city, country_code, exact=True)
            else:
                cities_found_tmp = SqliteTimezoneCache().get(default_city, exact=True)
            cities_found.extend(cities_found_tmp)

        return cities_found

    def stop(self):
        SqliteTimezoneCache().close_db()        