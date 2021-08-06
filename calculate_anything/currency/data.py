import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict
from typing import Dict


__all__ = ['CurrencyRate', 'CurrencyData']


class CurrencyRate(TypedDict):
    rate: float
    last_update_timestamp: float


CurrencyData = Dict[str, CurrencyRate]
