# Ulauncher Calculate Anything Extension

Currency and Unit converter as well as a Calculator that supports mathematical functions and Complex Numbers for [Ulauncher](https://ulauncher.io/), with the help of [simpleeval](https://github.com/danthedeckie/simpleeval), [pint](https://github.com/hgrecco/pint) and [fixer.io](https://fixer.io)

## Demo

![](images/demo.gif)

## Contents

 - [Install](#install)
 - [How to use](#how-to-use)
 - [Examples](#examples)


## Install

Thus extension depends on [requests](https://github.com/psf/), [pint](https://github.com/hgrecco/pint) and [simpleeval](https://github.com/danthedeckie/simpleeval). Install them with:
```bash
pip install requests pint simpleeval
```

## How to Use

### Set API Key

In order for the currency conversion to work you need to provide a [fixer.io](https://fixer.io/) API Key. Sign up at https://fixer.io/signup (there is free subscription available) and then go to your `fixer.io` dashboard and copy your API key to the appropriate input box in this extension's preferences.

### Cache

For currency conversion you can enable the cache (located by default at `~/.cache/extension_calculate_anything`) for a minimum of 1 day up to 1 year. This will store the results fetched by `fixer.io` to prevent redundant requests. This is especially helpful if you have a free plan on `fixer.io`. It will also display the results faster, since no request is made. If all requested currencies have been cached, not request is made to `fixer.io`

### Default currency

In the preferences you can define a comma separated list of default currencies to show when typing conversion without target unit/currency.
Defaults to `USD,EUR,CAD,GBP,AUD`

### Commands and Syntax

To convert anything you need to use the keyword (default `calc`, can be changed in preferences).

To convert currency

`calc AMOUNT CURRENCY` to get conversion in the default currencies set in the preferences (requires cache)

`calc AMOUNT CURRENCY in(or to) CURRENCY1,CURRENCY2,CURRENCY3` or

`calc CURRENCY in(or to) CURRENCY1,CURRENCY2,CURRENCY3`

To convert units use

`calc AMOUNT UNIT in(or to) UNIT1,UNIT2,UNIT3` or

`calc UNIT in(or to) UNIT1,UNIT2,UNIT3`

If you select one results it will be copied to clipboard.

Comma separated units and currencies can have spaces between them.

## Examples

### Currency
**Simple Conversion**
```
calc 10 EUR TO USD
# or
calc 10 euros to $
# or
calc 10 eurs to dollars

# Converts 10 euros to american dollars
```

**Multiple Conversion**
```
calc 10 EUR to USD,canadian,bitcoin,mexican

# Converts 10 euros to american dollars, canadian dollars, bitcoin, and mexican pesos
```

### Units

The units supported are all units that [pint](https://github.com/hgrecco/pint) supports (which is quite a lot)

**Simple Conversion**
Simple conversion
```
calc 100 f to c

# converts 100 fahrenheit to celsius, which is  37.7778 Celcius
```

**Multiple Conversion**
```
calc 20 cm in inches,m
# or
calc 20 cm in inches,meters

# produce 2 results with conversion in inches and meters
```

**Advanced Conversion**
```
calc 20 km/h to cm/min,km/minute,in/s,cm/sec

# Converts convert to centimeters per minute, kilometers per minute, inches per second and centimeters per second.
```

### Calculator
The calculator works like a normal calculator, but is able to work with complex numbers too.

The following constants exist: `pi`, `e`, `tau` and others from [cmath](https://docs.python.org/3/library/cmath.html)

The following functions exist: `phase`, `polar`, `rect`, `exp`, `log`, `log10`, `sqrt`, `acos`, `asin`, `atan`, `cos`, `sin`, `tan`, `acosh`, `asinh`, `atanh`, `cosh`, `sinh`, `tanh` and others from [cmath](https://docs.python.org/3/library/cmath.html)

Here are some examples
```
calc 10 + sqrt(2)
# Will output 11.4142

calc 10 + cos(pi) + 30 * e ^ 2
# Will output 230.672
```

With complex numbers too (j is the imaginary unit)
```
calc 10 + sqrt(2) + j
# Will output 11.4142 + j

calc cos(1 + j)
# Will output 0.83373 - 0.988898j

calc e ^ (pi * j) + 1
# Will output 0 (Euler's identity)
```