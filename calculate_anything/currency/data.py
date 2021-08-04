from typing import Dict, TypedDict


__all__ = ['CurrencyRate', 'CurrencyData']


class CurrencyRate(TypedDict):
    rate: float
    last_update_timestamp: float


CurrencyData = Dict[str, CurrencyRate]
