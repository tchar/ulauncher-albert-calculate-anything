# <img src="images/icon.svg" alt="drawing" width="25"/> Ulauncher/Albert Calculate Anything Extension

Currency and Unit converter as well as a Calculator for numbers, complex numbers, percentages and time that supports mathematical functions and Complex Numbers for [Ulauncher](https://ulauncher.io/), with the help of [simpleeval](https://github.com/danthedeckie/simpleeval), [pint](https://github.com/hgrecco/pint) and [fixer.io](https://fixer.io)

## Ulauncher Demo 

![](images/demo-ulauncher.gif)

## Albert Demo

![](images/demo-albert.gif)

## Contents

 - [Install for Ulauncher](#install-for-ulauncher)
 - [Install for Albert](#install-for-albert)
 - [How to setup](#how-to-setup)
 - [Examples](#examples)
 - [Extending and more](#extending-and-more)


## Install for Ulauncher

Thus extension depends on [requests](https://github.com/psf/), [pint](https://github.com/hgrecco/pint), [simpleeval](https://github.com/danthedeckie/simpleeval) and [parsedatetime](https://github.com/bear/parsedatetime). Install them with:
```bash
pip install requests pint simpleeval parsedatetime
```

Open `Ulauncher` go to `Extensions` > `Add extension` and paste https://github.com/tchar/ulauncher-albert-calculate-anything

## Install for Albert

Similarly to `Ulauncher` the same dependencies are are required.

To install the extension for Albert run
```bash
pip install requests pint simpleeval parsedatetime
mkdir -p ~/.local/share/albert/org.albert.extension.python/modules/
git clone https://github.com/tchar/ulauncher-albert-calculate-anything ~/.local/share/albert/org.albert.extension.python/modules/
```

Open albert, enable `Python` extensions and then enable the `Calculate Anything` extension.

You can double click it to open module's location and edit `__init__.py` to add your preferences.

## How to Setup

### Albert

If you ar using Albert open the extension location normally at `~/.local/share/albert/org.albert.extension.python/modules/ulauncher-albert-calculate-anything/__init__.py` and edit the preferences mentioned below in the apropriate variable `API_KEY`, `CACHE`, `DEFAULT_CURRENCIES` or `__triggers` for the keyword

By default the Albert extension does not use any keywords (can be changed the aforementioned file), so in the examples below just remove the `calc ` at the begining

### Ulauncher

If you are using Ulauncher use the extension preferences.

### Set API Key

In order for the currency conversion to work you need to provide a [fixer.io](https://fixer.io/) API Key. Sign up at https://fixer.io/signup (there is free subscription available) and then go to your `fixer.io` dashboard and copy your API key to the appropriate input box in this extension's preferences.


### Cache

For currency conversion you can enable the cache (located by default at `~/.cache/extension_calculate_anything`) for a minimum of 1 day up to 1 year. This will store the results fetched by `fixer.io` to prevent redundant requests. This is especially helpful if you have a free plan on `fixer.io`. It will also display the results faster, since no request is made. If all requested currencies have been cached, not request is made to `fixer.io`

### Default currency

In the preferences you can define a comma separated list of default currencies to show when typing conversion without target unit/currency.
Defaults to `USD,EUR,CAD,GBP,AUD`

### Commands and Syntax

To convert anything you can use the keyword  (default `calc` for `Ulauncher`, no keyword for `Albert`)

To convert currency type your keyword and then

`AMOUNT CURRENCY` to get conversion in the default currencies set in the preferences (requires cache)

`AMOUNT CURRENCY in(or to) CURRENCY1,CURRENCY2,CURRENCY3` or

`CURRENCY in(or to) CURRENCY1,CURRENCY2,CURRENCY3`

To convert units use

`AMOUNT UNIT in(or to) UNIT1,UNIT2,UNIT3` or

`UNIT in(or to) UNIT1,UNIT2,UNIT3`

If you select one results it will be copied to clipboard.

Comma separated units and currencies can have spaces between them.

## Examples

### Currency
**Simple Conversion**
```
10 EUR TO USD
# or
10 euros to $
# or
10 eurs to dollars

# Converts 10 euros to american dollars
```

**Multiple Conversion**
```
10 EUR to USD,canadian,bitcoin,mexican

# Converts 10 euros to american dollars, canadian dollars, bitcoin, and mexican pesos
```

### Units

The units supported are all units that [pint](https://github.com/hgrecco/pint) supports (which is quite a lot)

**Simple Conversion**
Simple conversion
```
100 f to c

# converts 100 fahrenheit to celsius, which is  37.7778 Celcius
```

**Multiple Conversion**
```
20 cm in inches,m
# or
20 cm in inches,meters

# produce 2 results with conversion in inches and meters
```

**Advanced Conversion**
```
20 km/h to cm/min,km/minute,in/s,cm/sec

# Converts convert to centimeters per minute, kilometers per minute, inches per second and centimeters per second.
```

### Percentages

***Simple Cases***

To calculate what is 10% of 40 use
```
10% of 40

# Returns 4
```

To calculate what percentage of 30 is 5 any of the following works
```
5 is what % of 30
5 is what % 30
5 as % of 30
5 in % of 30
5 in % 30

# Returns 16.6667%
```

***Advanced Cases***

You can also do more advanced things like the following
```
10% of cos(pi) + 5
# Returns 0.4

3 + 2 * pi % of cos(pi) + 5
# Returns 0.371328

5 as % sqrt(2) + 5
# Returns 77.9519%

1 + sin(pi) as % sqrt(2) + 5
# Returns 15.5904%
```

### Time
You can also add and subtract time
For example if now is `2021-07-05 14:14:42` then you can use the following
**NOTE: You can use the keyword now and time interchangeable**
```
now
# Returns 2021-07-05 14:14:42

now + 1 hour
# Returns Today at 15:14:42

now + 1 day
# Returns Tomorrow at 14:14:42

time - 1 day
# Returns Yesterday at 14:14:42

time + 2 hours 2 minutes 5 seconds
# Returns Today at 15:16:47

time + 1 year
# Returns 2022-07-05 14:14:42

time 
now + 1 year 2 days 2 hours - 4 years 4 minutes
# Returns 2018-07-07 16:10:42
```

### Calculator
The calculator works like a normal calculator, but is able to work with complex numbers too.

The following constants exist: `pi`, `e`, `tau` and others from [cmath](https://docs.python.org/3/library/cmath.html)

The following functions exist: `phase`, `polar`, `rect`, `exp`, `log`, `log10`, `sqrt`, `acos`, `asin`, `atan`, `cos`, `sin`, `tan`, `acosh`, `asinh`, `atanh`, `cosh`, `sinh`, `tanh` and others from [cmath](https://docs.python.org/3/library/cmath.html)

Here are some examples
```
10 + sqrt(2)
# Will output 11.4142

10 + cos(pi) + 30 * e ^ 2
# Will output 230.672
```

With complex numbers too (j is the imaginary unit)
```
10 + sqrt(2) + j
# Will output 11.4142 + j

cos(1 + j)
# Will output 0.83373 - 0.988898j

e ^ (pi * j) + 1
# Will output 0 (Euler's identity)
```

## Extending and More

The calculate_anything module does not depend on ulauncher or albert, only the `main.py` (for Ulauncher) and `__init__.py` (for albert) do. You can extend it for other cases.

### Adding flags

If your currencie's flag is missing you can place it in the extension's flags directory at `images/flags/` and restart your launcher or make a pull request to include it.

Make sure to name your flag image in uppercase 3 letter name of your currency. For example American Dollar's flag is in `images/flags/USD.svg`. You can use most image formats (i.e `svg`, `png`) 

You can find the flags that were used for this project at https://github.com/HatScripts/circle-flags/tree/gh-pages/flags.