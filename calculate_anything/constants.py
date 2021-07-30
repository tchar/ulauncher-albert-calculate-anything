'''Constants used by Calculate Anything

Constants consist of directories, global regexes etc.
If important directories do not exist, they are created here
'''

import os
import calculate_anything
from calculate_anything.appdirs import AppDirs


MAIN_DIR = os.path.dirname(os.path.dirname(
    os.path.realpath(calculate_anything.__file__)))
FLAGS = {f.split('.')[0]: f for f in os.listdir(
    os.path.join(MAIN_DIR, 'calculate_anything', 'images', 'flags'))}

APP_NAME = 'calculate_anything'
APP_DIRS = AppDirs(APP_NAME)

CACHE_DIR = APP_DIRS.user_cache_dir
LOGS_DIR = os.path.join(CACHE_DIR, 'logs')

if os.path.isfile(CACHE_DIR):
    os.remove(CACHE_DIR)
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

if os.path.isfile(LOGS_DIR):
    os.remove(LOGS_DIR)
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)


CURRENCY_DATA_FILE = os.path.join(CACHE_DIR, 'currency_data.json')
TIMEZONES_SQLITE_FILE_USER = os.path.join(CACHE_DIR, 'timezones_user.sqlite3')
TIMEZONES_SQLITE_FILE_DEFAULT = os.path.join(CACHE_DIR, 'timezones.sqlite3')
TIMEZONES_SQL_FILE = os.path.join(MAIN_DIR, 'data', 'time', 'timezones.sql')
TIMEZONES_JSON_FILE = os.path.join(MAIN_DIR, 'data', 'time', 'timezones.json')


TIME_DATETIME_FORMAT = '%A %B %d %Y %H:%M:%S'
TIME_DATETIME_FORMAT_NUMBERS = '%Y-%m-%d %H:%M'
TIME_DATE_FORMAT = '%A %B %d %Y'
TIME_TIME_FORMAT = '%H:%M:%S'
