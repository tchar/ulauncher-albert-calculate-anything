# API

The module works by parsing the input string and uses different handlers to calculate the expression.

The following handlers are supported:
- `UnitsQueryHandler`: Handles Units
- `CalculatorQueryHandler`: Handles Calculations
- `CurrencyQueryHandler`: Handles Currency
- `PercentagesQueryHandler`: Handles Percentages
- `TimeQueryHandler`: Handles Time
- `Base10QueryHandler`: Handles Decimal
- `Base16QueryHandler`: Handles Hexadecimal
- `Base8QueryHandler`: Handles Octal
- `Base2QueryHandler`: Handles Binary

There is also a generic handler (`MultiHandler`) which handles a request using all or a subset of handlers.

## Setup

The currency service by default is enabled, however it is not running.
There is also a cache which you can enable/disable.

You can enable/disable it before running any query with
```python
from calculate_anything.currency.service import CurrencyService

# To enable
CurrencyService().enable()

# To enable but disable cache
CurrencyService().enable().disable_cache()

# To enable the service and cache and run every 1 day = 86400 seconds
CurrencyService().enable().enable_cache(86400).run()

# To disable
CurrencyService().disable()

# To set the default currencies for results when no target currency is set.
CurrencyService().set_default_currencies(['EUR', 'USD', 'CAD', 'BTC'])
```

The service by default uses the [fixer.io](https://fixer.io) currency provider.

You can create your own provider by subclassing `CurrencyProvider` or `ApiKeyCurrencyProvider` (subclass of `CurrencyProvider`) class and implement its methods.

For example:
```python
from calculate_anything.currency.providers import CurrencyProvider
from calculate_anything.exceptions import (
    CurrencyProviderException,
    CurrencyProviderRequestException
)

class MyProvider(ApiKeyCurrencyProvider):
    def request_currencies(self, *currencies, force=False):
        # Write your code. Return a dictionary like
        if some_error:
            raise CurrencyProviderRequestException('Some error')
        return {
            'EUR': {'rate': 1, 'timestamp' 123123123123},
            'USD': {'rate': 1.2231, 'timestmap': 123123123},
            # ...
        }

    @property
    def api_key_valid(self):
        return True or False # If api key is valid

    def set_api_key(self, api_key):
        # If you need to change the behavior of the method, else don't implement.
        pass

my_provider = MyProvider()
# Or implement it in __init__
my_provider.set_api_key('your key')

# Then set your provider to service with
CurrencyService().add_provider(my_provider)

# Force run to make it run now
CurrencyService().run(force=True)
```

## Example use case

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
    result = MultiHandler().handle(query)
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
    CurrencyQueryHandler, TimeQueryHandler, UnitsQueryHandler,
    PercentagesQueryHandler, CalculatorQueryHandler,
    Base10QueryHandler, Base16QueryHandler, Base2QueryHandler,
    Base8QueryHandler
)

handlers = [CurrencyQueryHandler, TimeQueryHandler]

for query in queries:
    result = MultiHandler().handle(query, *handlers)
    # Do something with the result
```

## QueryResult

The `QueryResult` object is returned when using the `MultiHandler` class
In the case you want access to the underlying `Calculation` that produced the `QueryResult` you can pass a query directly to one of the handlers

```python
query = '10 + sqrt(2)'
calculations = CalculatorQueryHandler().handle(query)

for calculation in calculations:
    calculation.value # Value of calculation
    calculation.value_type # Value_type of calculation (int)
    calculation.get_description()
    calculation.format_query()
    calculation.format()
    calculation.to_query_result() # Returns the relevant QueryResult

# You can also get the Calculations by using the MultiHandler like this
calculations = MultiHandler().handle(query, return_raw=True)
```

**Some subclasses of the Calculation object can have more properties.**

## Handlers

You can write your own handler by implementing the `QueryHandlerInterface`

```python
from calculate_anything.query.handlers import QueryHandlerInterface
from calculate_anything.calculation import Calculation
from calculate_anything.query.handlers import CalculatorQueryHandler

class MyHandler(QueryHandlerInterface):
    def handle(self, query):
        # Use other query handler to calculate something
        calculation = CalculatorQueryHandler(query)
        
        # Check if errors exist
        if calculatione.error:
            return [calculation]
        
        value = calculation.value
        calculation1 = Calculation(value=value + 1, order=0)
        calculation2 = Calculation(value=value + 1.2, order=1)
        return [calculation1, calculation2]
```