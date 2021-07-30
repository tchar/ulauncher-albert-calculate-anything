import pytest
import os
import time
from calculate_anything.utils.loaders import SqliteLoader

temp_dir = '/dev/shm'


def oscreate(path, data):
    if path is None:
        return
    if not os.path.isabs(path):
        path = os.path.join(temp_dir, path)

    if os.path.exists(path):
        osremove(path)

    if not isinstance(data, str):
        os.mkdir(path)
        if data:
            data(path)
        return

    with open(path, 'w') as f:
        f.write(data)


def osremove(path):
    if path is None:
        return
    if not os.path.isabs(path):
        path = os.path.join(temp_dir, path)
    if not os.path.exists(path):
        return

    if os.path.isdir(path):
        os.rmdir(path)
    else:
        os.remove(path)


test_spec__init_db = [{
    # No sql file no sqlite file
    'id': '1',
    'sqlite_file': 'timezones1.sqlite3',
    'sql_file': None,
    'expected': {
        'load': False,
        'mode': SqliteLoader.Mode.FAIL | SqliteLoader.Mode.CREATE
    }
}, {
    # No sql file
    'id': '2',
    'create': [('timezones2.sqlite3', '')],
    'sqlite_file': 'timezones2.sqlite3',
    'sql_file': 'timezones2.sql',
    'expected': {
        'load': True,
        'mode': SqliteLoader.Mode.LOAD
    }
}, {
    # No sqlite file
    'id': '3',
    'create': [('timezones3.sql', '')],
    'sqlite_file': 'timezones3.sqlite3',
    'sql_file': 'timezones3.sql',
    'expected': {
        'load': True,
        'mode': SqliteLoader.Mode.CREATE
    }
}, {
    # Both file sqlite more recent
    'id': '4',
    'create': [('timezones4.sqlite3', ''), ('timezones4.sql', ''), ],
    'sqlite_file': 'timezones4.sqlite3',
    'sql_file': 'timezones4.sql',
    'expected': {
        'load': True,
        'mode': SqliteLoader.Mode.CREATE | SqliteLoader.Mode.REMOVE
    },
}, {
    # Both file sql more recent
    'id': '5',
    'create': [('timezones5.sql', ''), ('timezones5.sqlite3', ''), ],
    'sqlite_file': 'timezones5.sqlite3',
    'sql_file': 'timezones5.sql',
    'expected': {
        'load': True,
        'mode': SqliteLoader.Mode.LOAD
    }
}, {
    # No sql file, sqlite is a directory
    'id': '6',
    'create': [('timezones6.sqlite3', None), ],
    'sqlite_file': 'timezones6.sqlite3',
    'sql_file': 'timezones6.sql',
    'expected': {
        'load': False,
        'mode': SqliteLoader.Mode.LOAD | SqliteLoader.Mode.FAIL |
        SqliteLoader.Mode.CREATE | SqliteLoader.Mode.REMOVE
    }
}, {
    # Sqlite is a directory
    'id': '7',
    'create': [('timezones7.sqlite3', None), ('timezones7.sql', '')],
    'sqlite_file': 'timezones7.sqlite3',
    'sql_file': 'timezones7.sql',
    'expected': {
        'load': True,
        'mode': SqliteLoader.Mode.CREATE | SqliteLoader.Mode.REMOVE
    }
}, {
    # Sql file giberish
    'id': '8',
    'create': [('timezones8.sql', 'INSERT INTO WHAT THE FUCK?')],
    'sqlite_file': 'timezones8.sqlite3',
    'sql_file': 'timezones8.sql',
    'expected': {
        'load': False,
        'mode': SqliteLoader.Mode.FAIL | SqliteLoader.Mode.CREATE
    }
}, {
    # Use memory
    'id': '9',
    'create': [('timezones9.sql', 'CREATE TABLE test (id INTEGER)')],
    'mode': SqliteLoader.Mode.MEMORY,
    'sqlite_file': 'timezones9.sqlite3',
    'sql_file': 'timezones9.sql',
    'expected': {
        'load': True,
        'mode': SqliteLoader.Mode.MEMORY
    }
}, {
    # Fail memory
    'id': '10',
    'mode': SqliteLoader.Mode.MEMORY,
    'sqlite_file': 'timezones10.sqlite3',
    'sql_file': 'timezones10.sql',
    'expected': {
        'load': False,
        'mode': SqliteLoader.Mode.MEMORY | SqliteLoader.Mode.FAIL
    }
}, {
    # Fail can't read sql file
    'id': '11',
    'create': [('timezones11.sql', None)],
    'sqlite_file': 'timezones11.sqlite3',
    'sql_file': 'timezones11.sql',
    'expected': {
        'load': False,
        'mode': SqliteLoader.Mode.CREATE | SqliteLoader.Mode.FAIL
    }
}, {
    # Just fail
    'id': '12',
    'mode': SqliteLoader.Mode.CREATE | SqliteLoader.Mode.FAIL,
    'sqlite_file': 'timezones12.sqlite3',
    'sql_file': 'timezones12.sql',
    'expected': {
        'load': False,
        'mode': SqliteLoader.Mode.CREATE | SqliteLoader.Mode.FAIL
    }
}]


@ pytest.mark.parametrize('test_spec', test_spec__init_db)
def test__init_db(test_spec):
    loader = None
    try:
        _id = test_spec['id']

        create = test_spec.get('create', [])
        for i, [fname, data] in enumerate(create):
            # Sleep to have different mtime files
            if i != 0:
                time.sleep(0.01)
            oscreate(fname, data)

        sqlite_fpath = test_spec['sqlite_file']
        if sqlite_fpath:
            sqlite_fpath = os.path.join(temp_dir, sqlite_fpath)
        sql_fpath = test_spec['sql_file']
        if sql_fpath:
            sql_fpath = os.path.join(temp_dir, sql_fpath)

        mode = test_spec.get('mode')

        expected_loaded = test_spec['expected']['load']
        expected_mode = test_spec['expected']['mode']

        name = 'Test' + _id
        loader = SqliteLoader(sqlite_fpath, sql_fpath, name=name, mode=mode)

        loaded = loader.load()
        assert loader.mode == expected_mode
        assert loaded == expected_loaded
    finally:
        if loader is not None:
            loader.close()
        osremove(sqlite_fpath)
        osremove(sql_fpath)
