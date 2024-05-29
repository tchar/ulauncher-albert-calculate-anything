# API

## Contents
- [How it works](#how-it-works)
- [Setup](#setup)
- [Making Queries](#making-queries)
- [The QueryResult Object](#the-queryresult-object)
- [Extending QueryHandlers](#extending-queryhandlers)
- [Currency Providers](#currency-providers)
- [Logging](#logging)
- [Preferences Documentation](#preferences-documentation)

## How it works

The module works by parsing the input string and uses different handlers to calculate the expression.

The following handlers are supported:
- `UnitsQueryHandler`: Handles Units and Currency
- `CalculatorQueryHandler`: Handles Calculations
- `PercentagesQueryHandler`: Handles Percentages
- `TimeQueryHandler`: Handles Time
- `Base10QueryHandler`: Handles Decimal
- `Base16QueryHandler`: Handles Hexadecimal
- `Base8QueryHandler`: Handles Octal
- `Base2QueryHandler`: Handles Binary

There is also a generic handler (`MultiHandler`) which handles a request using all or a subset of handlers.

## Setup

The currency service by default is enabled, however it is not running.
There is also a cache to store results in a cache directory which you can enable/disable.

### Cache directories
Suppose your username is `username`:
- Linux: `/home/username/.cache/com.github.tchar.calculate-anything`
- Windows: `'C:\Users\username\AppData\Local\tchar\com.github.tchar.calculate-anything\Cache`
- macOS: `/Users/username/Library/Caches/com.github.tchar.calculate-anything`

### Log directories
Supose your username is `username`:
- Linux: `/home/username/.cache/com.github.tchar.calculate-anything/log`
- Windows: `'C:\Users\username\AppData\Local\tchar\com.github.tchar.calculate-anything\Logs`
- macOS: `/Users/username/Library/Logs/com.github.tchar.calculate-anything`


You can enable/disable the services manually but the prefered way is to use the `calculate_anything.preferences.Preferences` class

**The full preferences documentation can be found at [Preferences Documentation](#preferences-documentation)

Example
```python
import locale
from calculate_anything.preferences import Preferences

preferences = Preferences()
# Set the language
preferences.language.set('en_US')
# Set currencies to get by default when no target currency is specified
preferences.currency.set_default_currencies(['USD', 'EUR', 'CAD', 'BTC'])

# Enable cache and run every day (value specified in seconds). If set to 0 it is disabled
preferences.currency.enable_cache(60 * 60 * 24)

# Set default cities to show when no target city is specified when using time
preferences.time.set_default_cities('London GB,Athens GR,Tokyo JP')

# Commit preferences. If you don't commit, no change is made
preferences.commit()
```

## Making queries

You can make queries by either using the `MultiHandler` or a specific handler

Here are some examples
```python
# Import the handlers

from calculate_anything.query import MultiHandler


# Create a queries
queries = [
    '= 10 EUR to CAD',
    '= 10 + sqrt(2) + 5i',
    'time at Vancouver Canada',
    '= 10 meters to inches',
    'bin 1011011 mod 1010 and 10',
    'hex #ff12dd',
    #....
]

# Get the results
for query in queries:
    results = MultiHandler().handle(query)
    for result in results:
        # Result is of QueryResult type with following attributes
        result.icon # relative path of icon
        result.name # result text (formatted)
        result.description # result description
        result.clipboard # value to copy to clipboard if any
        result.value # result value (not formatted)
        result.error # If error or None
        result.order # Order of result


# If you want to handle the query using one or more
# particular handlers you can use the following


# Import one or more handlers
from calculate_anything.query.handlers import (
    TimeQueryHandler, UnitsQueryHandler,
    PercentagesQueryHandler, CalculatorQueryHandler,
    Base10QueryHandler, Base16QueryHandler, Base2QueryHandler,
    Base8QueryHandler
)

handlers = [UnitsQueryHandler, TimeQueryHandler]

for query in queries:
    results = MultiHandler().handle(query, *handlers)
    for result in results:
        # Do something with the result
        pass
```

## The QueryResult object

The `QueryResult` object is returned when using the `MultiHandler` class. However you can have access to the underlying `Calculation` by either using `MultiHandler`'s `handle_raw` method, or by using directly a `QueryHandler`.

**Some subclasses of the Calculation object can have more properties.**
The `Calculation` objects holds more information, such as
- Raw values calculated
- Other values associated with the calculated value.
    - For units it is the origin unit, target unit and rate
    - For percentages it is the left/right amount of your query
    - etc...
- Query parsed by `calculate_anything`

*The `Calculation` API is not yet stable but the underlying properties are*
**Example to get the `Calculation` object.**
```python
query = '10 + sqrt(2)'
calculations = CalculatorQueryHandler().handle(query)

for calculation in calculations:
    calculation.value # Value of calculation
    calculation.value_type # Value_type of calculation (int)
    calculation.get_description()
    calculation.format()
    result = calculation.to_query_result() # Returns the relevant QueryResult

# You can also get the Calculations by using the MultiHandler like this
calculations = MultiHandler().handle_raw(query)
for calculation in calculations:
    # ....
    result = calculation.to_query_result()
```

## Extending QueryHandlers

You can write your own handler by subclassing the `QyeryHandler` class

```python
from calculate_anything.query.handlers.base import QueryHandler
from calculate_anything.calculation import Calculation
from calculate_anything.query.handlers import CalculatorQueryHandler

class MyHandler(QyeryHandler):
    # The keyword can be anything (i.e "=", "+", ...)
    def __init__(self, keyword='customKeyword'):
        super().__init__(keyword)

    # You can implement this class if you want more granular control
    # of what queries your handler can handle. By default it is anything that
    # starts with your handler's keyword
    def can_handle(self, query):
        return super().can_handle(query)

    # Here you implement the logic of handling. You can use other handlers
    # too to help you parse your query. For example you can split your query
    # and calculate each part with the CalculatorQueryHandler and then concatenate
    # everythin to a custom Caclulation
    def handle_raw(self, query):
        # Use other query handler to calculate something
        calculation = CalculatorQueryHandler(query)
        
        # Check if errors exist
        if calculatione.error:
            return [calculation]
        
        value = calculation.value
        parsed_query = calculation.query
        calculation1 = Calculation(value + 1, parsed_query, order=0)
        calculation2 = Calculation(value + 1.2, parsed_query, order=1)
        return [calculation1, calculation2]


    # You can use this decorator to automatically reject queries 
    # That do not start with your keyword. This will call the 
    # can_handle() method above, or if not implemented it will call the super method
    @QyeryHandler.Decorators.can_handle
    def handle(self, query):
        return self.handle_raw(query)
```

## Currency Providers

By default there are 3 internal `CurrencyProvider`s. Which are of type `FreeCurrencyProvider` (subclass of `CurrencyProvider`). This means they don't need any authorization or API KEY
- `CoinbaseCurrencyProvider`: Gets currencies from coinbase (usually cryptocurrencies)
- `ECBCurrencyProvider`: Gets currencies from European Central Bank
- `MyCurrencyNetCurrencyProvider`: Gets currencies from mycurrency.net

There is 1 `ApiKeyCurrencyProvider` subclass of `CurrencyProvider` which requires an API Key and you can enable it through the preferences (see [Preferences Documentation](#preferences-documentation))
- `FixerIOCurrencyProvider`: Gets currencies from fixer.io

The main provider that combines all of these together to get all results, is the `CombinedCurrencyProvider` and handles the requesting of all the aforementioned providers so you don't have to request each and every one of them

You can also create your custom `CurrencyProvider` by subclassing either the `FreeCurrencyProvider` or the `ApiKeyCurrencyProvider` depending on if you require an api key or not.

**NOTE: The currency conversion system works with base currency the EURO. So you have to convert any rate to EURO base**

**Example**
```python
from datetime import datetime
import json
from json.decoder import JSONDecodeError
from urllib.request import urlopen
from urllib.error import HTTPError
# Get some supah nice logging
from calculate_anything import logging
from calculate_anything.currency.providers import ApiKeyCurrencyProvider
from calculate_anything.exceptions import CurrencyProviderException


logger = logging.getLogger(__name__)


class CustomCurrencyProvider(ApiKeyCurrencyProvider):
    PROTOCOL = 'https'
    HOSTNAME = 'your-base-url'
    API_URL = '/the-path-to/api/some-version/whatever'

    def __init__(self, api_key=''):
        super().__init__(api_key)

    def request_currencies(self, *currencies, force=False):
        super().request_currencies(*currencies, force=force)
        # Some query params for the request
        params = {'access_key': self._api_key, 'base': 'EUR'}
        try:
            # This is a super method, you can redefine it.
            request = self.get_request(params)
            logger.info('Making request to: {}'.format(request.full_url))
            with urlopen(request) as response:
                data = response.read().decode()
                response_code = response.getcode()
        except HTTPError as e:
            response_code = e.code
        except Exception as e:
            msg = 'Could not connect: {}'.format(e)
            logger.exception(e)
            self.had_error = True
            raise CurrencyProviderException(msg)

        if not str(response_code).startswith('2'):
            self.had_error = True
            msg = 'Response code not 2xx: {}'.format(response_code)
            logger.error(msg)
            raise CurrencyProviderException(msg)

        try:
            data = json.loads(data)
        except JSONDecodeError as e:
            self.had_error = True
            logger.exception('Could not decode json data: {}'.format(e))
            raise CurrencyProviderException('Could not decode json data')

        # Here you can handle your result
        # You need to return a dictionary as follows and EUR must be present in the currencies
        .... Code to process results
        # Get timestamp from provider or use datetime.now
        timestamp = datetime.now().timestamp()
        return {
            'EUR': {'rate': 1.0, 'timestamp_refresh': timestamp},
            'USD': {'rate': 0.900001, 'timestamp_refresh': timestamp},
            'CAD': {'rate': 0.75757, 'timestamp_refresh': timestamp},
            'AUD': {'rate': 0.667766, 'timestamp_refresh': timestamp},
        }
```

### Adding your provider 

Not documented yet (It should be added through the `CombinedCurrencyProvider`)


## Logging

The logging module used by `calculate_anything` is at `calculate_anything.logging` and is a wrapper for Python's `loggin` module.
By default 2 handlers are used
- A `StreamHandler` with color formatting to print to the stdout/stderr
- A `RotatingFileHandler` that stores logs to the `[path to calculate_anything's cache]/logs`

You can disable these handlers or set your own handlers/formatters
**Example**
```python
from calculate_anything import logging

# Disable both or just one handler
logging.disable_file_handler()
logging.disable_stdout_handler()

# Or even set a custom handler
handler = logging.CustomHandler(debug=print, info=print, warning=print, critical=print, critical=print)
# You can even use custom format and coloring, just remeber to use double braces for Python's logging format and single braces for coloring
handler.setFormatter(logging.ColorFormatter(
    fmt='[{BLUE}{{name}}.{{funcName}}:{{lineno}}{RESET}]: {{message}}',
    use_color=True
))
logging.set_stdout_handler(handler)
```

## Preferences Documentation
This is the preferences documentation with all possible preferences.

Suppose you already have initiated the `preferences` object with
```python
from calculate_anything import Preferences
pref = Preferences()
```

| Preference | Description |
| ----------- | ----------- |
| `pref.language.lang` | the current language as a `str`    |
| `pref.language.set(lang)` | sets the language to be comitted. lang must be a `str` (i.e 'en_US')       |
| `pref.time.default_cities` | returns the current default cities as a `list` of `dicts`|
| `pref.time.set_default_cities(cities)` | sets the default cities. cities must be either comma seperated `str` or an `iterable` of `str` |
| `pref.currency.default_currencies` | returns the current default currencies as a `list` of `str` |
| `pref.currency.set_default_currencies(currencies)` | sets the default currencies to be commited. must be a `str` of comma separated currencies or an `iterable` of `str` |
| `pref.currency.cache_update_frequency` | returns the current cache update frequency as an `int` representing seconds |
| `pref.currency.set_cache_update_frequency(freq)` | sets the cache update frequency to be commited. must be `int` representing seconds |
| `pref.currency.enable_cache(freq)` | Alias of `pref.currency.set_cache_update_frequency` |
| `pref.currency.disable_cache()` | Disables cache (i.e `frequency = 0`)        |
| `pref.currency.providers` | Returns a `list` of `str` representing the current currency providers used |
| `pref.currency.add_provider(provider, api_key='')` | Sets the currency provider to be used. If the first parameter is an instance of `CurrencyProvider`, `api_key` is ignored, otherwise uses provider as a `str` to find a matching provider by name (`api_key` is optional and `''` by default) |
| `pref.currency.remove_provider(provider)` | Removes provider. provider can be either a `str` or a `CurrencyProvider` instance |
| `pref.units.conversion_mode` | Gets the current units conversion mode as an `int` from `UnitsService.ConversionMode` `enum` |
| `pref.units.set_conversion_mode(mode)` | Sets the conversion mode to be commited. Can be either a str (i.e 'normal'/'crazy' or an int from `UnitsService.ConversionMode` `enum`)        |
