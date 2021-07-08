# <img src="images/icon.svg" alt="drawing" width="25"/> Ulauncher/Albert Calculate Anything Extension

Currency and Unit converter as well as a Calculator for numbers, complex numbers, percentages and time that supports mathematical functions and Complex Numbers for [Ulauncher](https://ulauncher.io/), with the help of [simpleeval](https://github.com/danthedeckie/simpleeval), [pint](https://github.com/hgrecco/pint) and [fixer.io](https://fixer.io)


## Albert Demo

![](images/demo-albert.gif)

## Ulauncher Demo 

![](images/demo-ulauncher.gif)

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

If you ar using Albert open the extension location normally at `~/.local/share/albert/org.albert.extension.python/modules/ulauncher-albert-calculate-anything/__init__.py` and edit the preferences mentioned below in the apropriate variable `API_KEY`, `CACHE`, `DEFAULT_CURRENCIES`, `DEFAULT_CITIES`, `SHOW_EMPTY_PLACEHOLDER` or `__triggers__` for the keyword

The extension can work in albert without keywords if you comment out the `__triggers__` option, however if another extension has the keyword you type, `Calculate Anything won't trigger` (see [relevant issue](https://github.com/albertlauncher/albert/issues/978))

### Ulauncher

If you are using Ulauncher use the extension preferences.

### Set API Key

In order for the currency conversion to work you need to provide a [fixer.io](https://fixer.io/) API Key. Sign up at https://fixer.io/signup (there is free subscription available) and then go to your `fixer.io` dashboard and get your API key.
- ULauncher: Copy your api key to the `API KEY` box in preferences
- Albert: Modify the `API_KEY` in `__init__.py`


### Cache

For currency conversion you can enable the cache (located by default at `~/.cache/extension_calculate_anything`) for a minimum of 1 day up to 1 year. This will store the results fetched by `fixer.io` to prevent redundant requests. This is especially helpful if you have a free plan on `fixer.io`. It will also display the results faster, since no request is made. If all requested currencies have been cached, not request is made to `fixer.io`

- Ulauncher: Edit `Currency Cache` in the extension preferences
- Albert: Edit `CACHE=86400` in `__init__.py` and set it to your interval in seconds

### Default currency

In the preferences you can define a comma separated list of default currencies to show when typing conversion without target unit/currency.
Defaults to `USD,EUR,CAD,GBP,AUD`

- ULauncher: Edit in `Default Currencies` preferences
- Albert: Edit `DEFAULT_CURRENCIES` in `__init__.py`

### Default cities

In the preferences you can define a comma separated list of default cities when using the time command

- ULauncher: Edit in `Default Currencies` preferences
- Albert: Edit `DEFAULT_CITIES` in `__init__.py`

### Show Empty Placeholder

 - ULauncher: Default is `No`. Set to `Yes` to show an empty placeholder when extension doesn't return anything
 - Albert: Change `SHOW_EMPTY_PLACEHOLDER=True` in `__init__.py`

### Commands and Syntax

To convert anything you can use the keyword  (default `=` and `time` as in the demo for `Ulauncher`)

You can go directly to [examples](#examples) or use the ones from the demo

To convert currency type your keyword and then

- `AMOUNT CURRENCY` to get conversion in the default currencies set in the preferences (requires cache)
- `AMOUNT CURRENCY in(or to) CURRENCY1,CURRENCY2,CURRENCY3`
- `CURRENCY in(or to) CURRENCY1,CURRENCY2,CURRENCY3`

To convert units use

- `AMOUNT UNIT in(or to) UNIT1,UNIT2,UNIT3`
- `UNIT in(or to) UNIT1,UNIT2,UNIT3`

Comma separated units and currencies can have spaces between them.

For time you can use the time keyword with a syntax

- `time` To get the current time plus the `default cities` you defined in the preferences
- `time at CITY,[COUNTRY|COUNTRY CODE|STATE CODE]` to get the current time for a specified city
- `time + AMOUNT [MONTH|YEAR|WEEK|DAY|HOUR|MINUTE|SECOND] [+ AMOUNT ...] [at CITY, [COUNTRY|COUNTRY CODE|STATE CODE]]` to get the time after the calculation at a specified city.

To calculate an expression just type your expression as in the demo
 - You can use functions such as `tan`,`atan`,`asinh`
 - You can use complex numbers too like `1 + 5i`

To calculate percentages you can use one of the following
- `AMOUNT1% of AMOUNT2` to calculate the AMOUNT1 percent of AMOUNT2
- `AMOUNT1 as % of AMOUNT2` to calculate AMOUNT1 as a percentage of AMOUNT2

If you select one results it will be copied to clipboard.

## Examples

### Currency

**Simple Conversion**
- Convert 10 euros to american dollars
- `10 eur to USD`
- `10 euros to $`
- `10 eurs to dollars`

**Multiple Conversion**
- Convert 10 euros to american dollars, canadian dollars, bitcoin, and mexican pesos
    - `10 EUR to USD,canadian,bitcoin,mexican`

### Units

The units supported are all units that [pint](https://github.com/hgrecco/pint) supports (which is quite a lot)

**Simple Conversion**
- Convert 100 fahrenheit to celsius, which is  37.7778 Celcius
   - `100 f to c`

**Multiple Conversion**
  - Convert 20 centimeters to inches and meters
  - `20 cm in inches, m`
  - `20 cm in inches,meters`

**Advanced Conversion**
- Convert kilometers per meter to centimeters per minute, kilometers per minute, inches per second and centimeters per second.
    - `20 km/h to cm/min, km/minute, in/s, cm/sec`
- Convert kilowhats per second to horsepower per hour and megawatts per second
    - `10 kw/sec to hp/h, mw/s`
- Convert meters per squared second to kilometers per squared hour
    - `10 m/s^2 to km/h^2`
- Convert megabytes per second to gigabytes per hour
    - `10 mb/s to gb/h`

**You can lieterally convert anything if the apropriate units match**
- Convert kilometer * centimeter * second per gibabyte to inches * meter * hour per megabyte
    - `10 km * cm * s / gb to inches * meter * hour / mb`

### Percentages

**Simple Cases**
- Calculate what is 10% of 40 (Answer is 4)
    - `10% of 40`
- To calculate what percentage of 30 is 5 (Answer is 16.6667%) any of the following works
    - `5 is what % of 30`
    - `5 is what % 30`
    - `5 as % of 30`
    - `5 in % of 30`
    - `5 in % 30`

**Advanced Cases**
- `10% of cos(pi) + 5`: Returns 0.4
- `3 + 2 * pi % of cos(pi) + 5`: Returns 0.371328
- ``5 as % sqrt(2) + 5`: Returns 77.9519%
- `1 + sin(pi) as % sqrt(2) + 5`: Returns 15.5904%

### Time

You can also add and subtract time
For example if now is `2021-07-05 14:14:42` then you can use the following

**NOTE: You can use the keyword now and time interchangeably in Albert**

**In the following examples the time returned is accompanied by the date time in the `default cities` you specified in the extension preferences**

- `time`: Returns 2021-07-05 14:14:42 as well as the date time in the default cities specified in settings
- `time plus 1 hour`: Returns Today at 15:14:42 
- `time + 1 day`: Returns Tomorrow at 14:14:42
- `time minus 1 day`: Returns Yesterday at 14:14:42
- `time + 2 hours` 2 minutes 5 seconds: Returns Today at 15:16:47
- `time + 1 year`: Returns 2022-07-05 14:14:42
- `time + 1 year 2 days 2 hours - 4 years 4 minutes`: Returns 2018-07-07 16:10:42

**Specifying a custom city**

You can use all the commands above followed by `at CITY NAME` or `at CITY NAME, COUNTRY NAME|COUNTRY CODE|STATE CODE` to get te result in your local time as well as the specified city
- `time at Prague`
- `time + 2 hours at Madrid`
- `time + 2 hours at Vancouver, CA`: (There are two Vancouvers, so by specifying CA as returns the Canadian Vancouver)
- `time + 2 days 3 seconds at Vancouver, Canada`
- `time + 1 hour + 3 years at Athens, AL`: (Athens AL refenrs to Athens at Alabama)

### Calculator

The calculator works like a normal calculator, but is able to work with complex numbers too.

The following constants exist: `pi`, `e`, `tau` and others from [cmath](https://docs.python.org/3/library/cmath.html)

The following functions exist: `phase`, `polar`, `rect`, `exp`, `log`, `log10`, `sqrt`, `acos`, `asin`, `atan`, `cos`, `sin`, `tan`, `acosh`, `asinh`, `atanh`, `cosh`, `sinh`, `tanh` and others from [cmath](https://docs.python.org/3/library/cmath.html)

**Simple Cases**
- `10 + sqrt(2)`: Answer is 11.4142
- `10 + cos(pi) + 30 * e ^ 2`: Answer is 230.672

**Complex Numbers**
Use j or i as the imaginary unit
- `10 + sqrt(2) + j`: Answer is 11.4142 + j
- `cos(1 + j)`: Answer is 0.83373 - 0.988898j
- `e ^ (pi * j) + 1`: Answer is 0 (Euler's identity)

## Extending and More

The calculate_anything module does not depend on ulauncher or albert, only the `main.py` (for Ulauncher) and `__init__.py` (for albert) do. You can extend it for other cases.

### Adding flags

If your currencie's flag is missing you can place it in the extension's flags directory at `images/flags/` and restart your launcher or make a pull request to include it.

Make sure to name your flag image in uppercase 2 letter name of your country. To make a currency flag, simply link the country flag you want to the currency `e.g ln -s US.svg USD.svg` or add a completely new flat For example American Dollar's flag is in `images/flags/USD.svg`. You can use most image formats (i.e `svg`, `png`) 

<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>