import os
import re
import calculate_anything
from .utils import replace_dict_re_func

XDG_FALLBACK = os.getenv('HOME')
if XDG_FALLBACK is None:
    XDG_FALLBACK = os.path.expanduser('~')
XDG_FALLBACK = os.path.join(XDG_FALLBACK, '.cache')
XDG_CACHE = os.getenv('XDG_CACHE_HOME', XDG_FALLBACK)
CACHE_DIR = os.path.join(XDG_CACHE,  'extension_calculate_anything')
DATA_FILE = os.path.join(CACHE_DIR, 'data.json')

# Replace plus with + and minus with -
PLUS_MINUS_REGEX_REPLACE_FUNC = replace_dict_re_func(
    {'plus': '+', 'minus': '-'}, flags=re.IGNORECASE)

# Unit conversion regex match
UNIT_QUERY_REGEX = re.compile(r'(.*?)\s+(?:to|in)\s+(.*)', flags=re.IGNORECASE)
# Unit conversion when no target unit specified
# UNIT_REGEX_SPLIT = re.compile(r'[^\W_0-9]+')
UNIT_SPLIT_RE = re.compile(r'([A-Za-z_]+)')
UNIT_CURRENCY_RE = re.compile(r'currency_([A-Za-z]{3})')
UNIT_ALIASES_RE = re.compile(r'^[a-zA-Z_]+$')

CURRENCY_QUERY_REGEX = re.compile(
    r'^\s*(\d+\.?\d*)?\s*(.*)\s+(?:to|in)\s+(.*)$', flags=re.IGNORECASE)
CURRENCY_QUERY_DEFAULT_REGEX = re.compile(
    r'^\s*(\d+\.?\d*)?\s*(.*?)(?:\s+(?:to|in)?\s*$|\s*$)', flags=re.IGNORECASE)
CURRENCY_REGEX = re.compile(r'^[a-z]{3}$', flags=re.IGNORECASE)
EMPTY_AMOUNT = re.compile(r'^\s*$')

CALCULATOR_ERROR = 1e-10
CALCULATOR_REGEX_REJECT = re.compile(r'.*(%|\/\/|==|[^A-Za-z]is[^A-Za-z]).*')
CALCULATOR_IMAG_REPLACE = re.compile(r'([^a-zA-Z]\s*|\s+|^)i([^a-zA-Z0-9]|$)')
CALCULATOR_QUERY_REGEX_REPLACE_FUNC = replace_dict_re_func({
    'mod ': '%', 'div ': '//', '^': '**',
    '>=': '>=', '<=': '<=', '=': '=='
}, flags=re.IGNORECASE)
CALCULATOR_REPLACE_LEADING_ZEROS = re.compile(r'(^|[\=\+\-\*\/\%])0+([1-9])')
CALCULATOR_QUERY_SPLIT_EQUALITIES = re.compile(r'(==|>=|<=|>|<)')

PERCENTAGES_REGEX_MATCH_NORMAL = re.compile(
    r'^\s*(.*)% of (.*)\s*$', flags=re.IGNORECASE)
PERCENTAGES_REGEX_MATCH_INVERSE = re.compile(
    r'^\s*(.*)\s*(?:as|is what|in)\s*(?: a)?\s*(?:%|percent(?:age)?)\s(?:of )?(.*)\s*$', flags=re.IGNORECASE)
PERCENTAGES_REGEX_CALC_MATCH = re.compile(r'^\s*(.*)\s*(\+|-)\s*(.*)\s*%\s*$')

TIME_QUERY_REGEX = re.compile(r'\s*(now|time)', flags=re.IGNORECASE)
TIME_QUERY_REGEX_SPLIT = re.compile(
    r'\s(in?|at?|(?:un)?till?)(?:\s|$)', flags=re.IGNORECASE)
TIME_SUBQUERY_REGEX = re.compile(
    r'.*[^\W_0-9].*', flags=re.IGNORECASE | re.UNICODE)
TIME_SUBQUERY_DIGITS = re.compile(r'\d+\.?\d*')
TIME_SPLIT_REGEX = re.compile(r'(\+|-)')
# TIME_PROHIBITTED_CALC = re.compile(
    # r'(next|last|previous|following|yesterday|tomorrow)[^\+\-\s]+[a-z]', flags=re.IGNORECASE)
TIME_LOCATION_REPLACE_REGEX = re.compile(
    r'[\W_]+', flags=re.IGNORECASE | re.UNICODE)
TIME_DATETIME_FORMAT = '%A %-d %B %Y %H:%M:%S'
TIME_DATETIME_FORMAT_NUMBERS = '%Y-%m-%-d %H:%M'
TIME_DATE_FORMAT = '%A %-d %B %Y'
TIME_TIME_FORMAT = '%H:%M:%S'

MAIN_DIR = os.path.dirname(os.path.dirname(
    os.path.realpath(calculate_anything.__file__)))
FLAGS = {f.split('.')[0]: f for f in os.listdir(
    os.path.join(MAIN_DIR, 'images/flags'))}
