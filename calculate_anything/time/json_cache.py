import json
from typing import List
from calculate_anything import logging
from calculate_anything.time.data import CityData
from calculate_anything.constants import TIMEZONES_JSON_FILE


logger = logging.getLogger(__name__)


class TimezoneJsonCache:
    def __init__(self) -> None:
        self._data = {}

    def load(self) -> bool:
        try:
            with open(TIMEZONES_JSON_FILE, 'r', encoding='utf-8') as f:
                self._data = json.loads(f.read())
        except Exception as e:  # pragma: no cover
            logger.exception(
                'Could not load timezone data: {}: {}'.format(
                    TIMEZONES_JSON_FILE, e
                )
            )  # pragma: no cover
            return False  # pragma: no cover
        return True

    def get(self, city_name: str, *search_terms: str) -> List[CityData]:
        city_code = city_name.strip().lower()
        if city_code not in self._data:
            return []
        cities = self._data[city_code]
        if not search_terms:
            return cities

        search_terms = [s.lower() for s in search_terms]
        cities_found = []
        for city in cities:
            for search_term in search_terms:
                found = False
                if search_term == city['state'].lower():
                    found = True
                elif search_term == city['country'].lower():
                    found = True
                elif search_term == city['cc'].lower():
                    found = True
                elif search_term == city['timezone'].lower():
                    found = True
                if not found:
                    break
            else:
                cities_found.append(city)
        return cities_found or cities
