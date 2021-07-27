import re
from calculate_anything.time.sqlite_cache import TimezoneSqliteCache
from calculate_anything.time.json_cache import TimezoneJsonCache
from calculate_anything.utils import Singleton


__all__ = ['TimezoneService']


class TimezoneService(metaclass=Singleton):
    def __init__(self):
        self._default_cities = []
        self._default_cities_search = []
        self._running = False
        self._cache = TimezoneSqliteCache()

    def get(self, name, *search_terms):
        return self._cache.get(name, *search_terms)

    @property
    def default_cities(self):
        return self._default_cities

    def set_default_cities(self, default_cities):
        self._default_cities_search = default_cities

    def parse_default_cities_str(self, default_cities_str, save=False):
        regex = re.compile(r'^(.*)\s+([a-z]{2,3})$', flags=re.IGNORECASE)

        default_cities = default_cities_str.strip().split(',')
        cities = []
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
                cities.append((default_city, country_code))
            else:
                cities.append((default_city, None))

        if save or self._running:
            self.set_default_cities(cities)
        if self._running:
            self._default_cities_from_parsed()
        return cities

    def _default_cities_from_parsed(self):
        cities = []
        for city, country_code in self._default_cities_search:
            search_terms = (country_code,) if country_code else ()
            if isinstance(self._cache, TimezoneSqliteCache):
                cities.extend(self._cache.get(city, *search_terms, exact=True))
            else:
                cities.extend(self._cache.get(city, *search_terms))
        self._default_cities = cities

    def start(self):
        if self._running:
            return
        if not self._cache.load():
            fallback = TimezoneJsonCache()
            fallback.load()
            self._cache = fallback
        self._default_cities_from_parsed()
        self._running = True

    def stop(self):
        if isinstance(self._cache, TimezoneSqliteCache):
            self._cache.close_db()
