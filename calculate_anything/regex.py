import re
from calculate_anything.utils import multi_re


# Replace plus with + and minus with -
PLUS_MINUS_REGEX = multi_re.compile(
    {'plus': '+', 'minus': '-'}, flags=re.IGNORECASE
)

# Unit conversion regex match
UNIT_QUERY_SPLIT_RE = re.compile(r'\sto\s', flags=re.IGNORECASE)
# Unit conversion when no target unit specified
# UNIT_REGEX_SPLIT = re.compile(r'[^\W_0-9]+')
UNIT_SPLIT_RE = re.compile(r'([A-Za-z_]+)')
UNIT_CURRENCY_RE = re.compile(r'currency_([A-Za-z]{3,})')
UNIT_ALIASES_RE = re.compile(r'^[a-zA-Z_]+$')

CURRENCY_QUERY_REGEX = re.compile(
    r'^\s*(\d+\.?\d*)?\s*(.*)\s+(?:to|in)\s+(.*)$', flags=re.IGNORECASE
)
CURRENCY_QUERY_DEFAULT_REGEX = re.compile(
    r'^\s*(\d+\.?\d*)?\s*(.*?)(?:\s+(?:to|in)?\s*$|\s*$)', flags=re.IGNORECASE
)
EMPTY_AMOUNT = re.compile(r'^\s*$')

CALCULATOR_REGEX_REJECT = re.compile(
    r'.*(%|\/\/|==|[^a-z]is[^a-z]).*', flags=re.IGNORECASE
)
CALCULATOR_QUERY_REGEX_REPLACE = multi_re.compile(
    {'mod ': '%', 'div ': '//', '^': '**', '>=': '>=', '<=': '<=', '=': '=='},
    flags=re.IGNORECASE,
)
CALCULATOR_REPLACE_LEADING_ZEROS = re.compile(r'(^|[\=\+\-\*\/\%])0+([1-9])')
CALCULATOR_QUERY_SPLIT_EQUALITIES = re.compile(r'(==|>=|<=|>|<)')

PERCENTAGES_REGEX_MATCH_NORMAL = re.compile(
    r'^\s*(.*)% of (.*)\s*$', flags=re.IGNORECASE
)
PERCENTAGES_REGEX_MATCH_INVERSE = re.compile(
    r'^\s*(.*)\s*(?:as|is what|in)\s*(?: a)?\s*'
    r'(?:%|percent(?:age)?)\s(?:of )?(.*)\s*$',
    flags=re.IGNORECASE,
)
PERCENTAGES_REGEX_CALC_MATCH = re.compile(r'^[^%]+[\+\-][^%]+%$')

TIME_QUERY_REGEX_SPLIT = re.compile(
    r'(?:^|\s+)(in?|at?|(?:un)?till?)(?:\s+|$)', flags=re.IGNORECASE
)
TIME_SUBQUERY_REGEX = re.compile(
    r'.*[^\W_0-9].*', flags=re.IGNORECASE | re.UNICODE
)
TIME_SPLIT_REGEX = re.compile(r'(\+|-)')
TIME_AGO_BEFORE_REGEX = re.compile(r'\s(ago|before)(\s|$)')
TIME_LOCATION_REPLACE_REGEX = re.compile(
    r'[\W_]+', flags=re.IGNORECASE | re.UNICODE
)
