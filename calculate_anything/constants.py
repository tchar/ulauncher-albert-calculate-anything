import os
import re
import calculate_anything

XDG_FALLBACK = os.path.join(os.getenv('HOME'), '.cache')
XDG_CACHE = os.getenv('XDG_CACHE_HOME', XDG_FALLBACK)
CACHE_DIR = os.path.join(XDG_CACHE,  'extension_calculate_anything')
DATA_FILE = os.path.join(CACHE_DIR, 'data.json')

FILENAME_REGEX = re.compile(r'([a-z]{3})\.json', flags=re.IGNORECASE)

UNIT_QUERY_REGEX = re.compile(r'^\s*(.*)\s+(to|in)\s+(.*)$', flags=re.IGNORECASE)
UNIT_QUERY_REGEX_DEFAULT = re.compile(r'^\s*(.*)\s*')
UNIT_REGEX_SPLIT = re.compile(r'[a-z]+')

CURRENCY_QUERY_REGEX = re.compile(r'^\s*(\d+\.?\d*)?\s*(.*)\s+(to|in)\s+(.*)$', flags=re.IGNORECASE)
CURRENCY_REGEX = re.compile(r'^[a-z]{3}$', flags=re.IGNORECASE)
CURRENCY_DEFAULT_REGEX = re.compile(r'^\s*(\d+\.?\d*)?\s*(.*)\s*(to|in)?\s*$', flags=re.IGNORECASE)
EMPTY_AMOUNT = re.compile(r'^\s*$')

CALCULATOR_ERROR = 1e-10
CALCULATOR_REGEX_REJECT = re.compile(r'.*(%|\/\/).*')
CALCULATOR_QUERY_REPLACE = {'mod ': '%', 'div ': '//', '^': '**'}
CALCULATOR_IMAG_REPLACE = re.compile(r'([^a-z]\s*|\s+|^)i([^a-z0-9]|$)')
CALCULATOR_IMAG_REGEX_UNIT_REGEX = re.compile(r'([^a-zA-Z0-9]\s*|^\s*)j[^a-zA-Z]{0,1}')
CALCULATOR_QUERY_REPLACE = dict((re.escape(k), v) for k, v in CALCULATOR_QUERY_REPLACE.items())
CALCULATOR_REGEX_QUERY_REPLACE = re.compile("|".join(CALCULATOR_QUERY_REPLACE.keys()))

MAIN_DIR = os.path.dirname(os.path.dirname(os.path.realpath(calculate_anything.__file__)))
FLAGS = {f.split('.')[0]: f for f in os.listdir(os.path.join(MAIN_DIR, 'images/flags'))}

