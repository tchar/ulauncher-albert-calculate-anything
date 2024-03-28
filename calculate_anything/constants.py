'''Constants used by Calculate Anything

Constants consist of directories, global regexes etc.
If important directories do not exist, they are created here
'''

import os
import calculate_anything
from calculate_anything.appdirs import AppDirs

APP_NAME = 'com.github.tchar.calculate-anything'
APP_AUTHOR = 'tchar'

APP_DIRS = AppDirs(APP_NAME, APP_AUTHOR)

if os.path.isfile(APP_DIRS.user_cache_dir):
    os.remove(APP_DIRS.user_cache_dir)
if not os.path.exists(APP_DIRS.user_cache_dir):
    os.makedirs(APP_DIRS.user_cache_dir)

if os.path.isfile(APP_DIRS.user_log_dir):
    os.remove(APP_DIRS.user_log_dir)
if not os.path.exists(APP_DIRS.user_log_dir):
    os.makedirs(APP_DIRS.user_log_dir)


MAIN_DIR = os.path.dirname(
    os.path.dirname(os.path.realpath(calculate_anything.__file__))
)
FLAGS = {
    f.split('.')[0]: f
    for f in os.listdir(
        os.path.join(MAIN_DIR, 'calculate_anything', 'images', 'flags')
    )
}


CURRENCY_DATA_FILE = os.path.join(APP_DIRS.user_cache_dir, 'currency_data.json')
TIMEZONES_SQLITE_FILE_USER = os.path.join(
    APP_DIRS.user_cache_dir, 'timezones_user.sqlite3'
)
TIMEZONES_SQLITE_FILE_DEFAULT = os.path.join(
    APP_DIRS.user_cache_dir, 'timezones.sqlite3'
)
TIMEZONES_SQL_FILE = os.path.join(MAIN_DIR, 'data', 'time', 'timezones.sql')
TIMEZONES_JSON_FILE = os.path.join(MAIN_DIR, 'data', 'time', 'timezones.json')

TIME_DATETIME_FORMAT = '%A %B %d %Y %H:%M:%S'
TIME_DATETIME_FORMAT_NUMBERS = '%Y-%m-%d %H:%M'
TIME_DATE_FORMAT = '%A %B %d %Y'
TIME_TIME_FORMAT = '%H:%M:%S'

CALCULATOR_ERROR = 1e-10
