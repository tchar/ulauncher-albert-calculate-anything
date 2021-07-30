import pytest
import os
import json
import time
from calculate_anything.utils.loaders import (
    SqliteLoader, JsonLoader, CurrencyCacheLoader
)
from calculate_anything.utils.loaders.loader import Loader


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


test_spec_sqlite = [{
    # No sql file no sqlite file
    'id': '1',
    'sqlite_file': 'timezones1.sqlite3',
    'sql_file': None,
    'expected': {
        'load': False,
        'status': SqliteLoader.Status.FAIL,
        'mode': SqliteLoader.Mode.CREATE
    }
}, {
    # No sql file
    'id': '2',
    'create': [('timezones2.sqlite3', '')],
    'sqlite_file': 'timezones2.sqlite3',
    'sql_file': 'timezones2.sql',
    'expected': {
        'load': True,
        'status': SqliteLoader.Status.SUCCESS,
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
        'status': SqliteLoader.Status.SUCCESS,
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
        'status': SqliteLoader.Status.SUCCESS,
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
        'status': SqliteLoader.Status.SUCCESS,
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
        'status': SqliteLoader.Status.FAIL | SqliteLoader.Status.FILE_IS_DIR,
        'mode': SqliteLoader.Mode.LOAD |
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
        'status': SqliteLoader.Status.SUCCESS |
        SqliteLoader.Status.FILE_IS_DIR,
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
        'status': SqliteLoader.Status.FAIL | SqliteLoader.Status.INVALID_DATA,
        'mode': SqliteLoader.Mode.CREATE
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
        'status': SqliteLoader.Status.SUCCESS,
        'mode': SqliteLoader.Mode.MEMORY | SqliteLoader.Mode.CREATE
    }
}, {
    # Fail memory
    'id': '10',
    'mode': SqliteLoader.Mode.MEMORY,
    'sqlite_file': 'timezones10.sqlite3',
    'sql_file': 'timezones10.sql',
    'expected': {
        'load': False,
        'status': SqliteLoader.Status.FAIL,
        'mode': SqliteLoader.Mode.MEMORY | SqliteLoader.Mode.CREATE
    }
}, {
    # Fail can't read sql file
    'id': '11',
    'create': [('timezones11.sql', None)],
    'sqlite_file': 'timezones11.sqlite3',
    'sql_file': 'timezones11.sql',
    'expected': {
        'load': False,
        'status': SqliteLoader.Status.FAIL,
        'mode': SqliteLoader.Mode.CREATE
    }
}, {
    # Fail with no remove
    'id': '12',
    'mode': SqliteLoader.Mode.NO_REMOVE,
    'sqlite_file': 'timezones12.sqlite3',
    'sql_file': 'timezones12.sql',
    'expected': {
        'load': False,
        'status': SqliteLoader.Status.FAIL,
        'mode': SqliteLoader.Mode.CREATE | SqliteLoader.Mode.NO_REMOVE
    }
}]


@ pytest.mark.parametrize('test_spec', test_spec_sqlite)
def test_sqlite(test_spec):
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

        mode = test_spec.get('mode', 0)

        expected_loaded = test_spec['expected']['load']
        expected_status = test_spec['expected']['status']
        expected_mode = test_spec['expected']['mode']

        name = 'Test' + _id
        loader = SqliteLoader(sqlite_fpath, sql_fpath, name=name, mode=mode)

        loaded = loader.load()
        assert expected_status == loader.status
        assert expected_mode == loader.mode
        assert expected_loaded == loaded
    finally:
        if loader is not None:
            loader.close()
        osremove(sqlite_fpath)
        osremove(sql_fpath)


test_spec_json = [{
    # No file
    'id': '1',
    'file': 'data1.json',
    'default_data': None,
    'expected': {
        'data': None,
        'load': False,
        'status': JsonLoader.Status.FAIL,
        'mode': JsonLoader.Mode.FALLBACK
    }
}, {
    # File
    'id': '2',
    'create': ('data2.json', '{"some-key": "some-value"}'),
    'file': 'data2.json',
    'default_data': {},
    'expected': {
        'data': {'some-key': 'some-value'},
        'load': True,
        'status': JsonLoader.Status.SUCCESS,
        'mode': JsonLoader.Mode.LOAD | JsonLoader.Mode.VALIDATE
    }
}, {
    # File
    'id': '3',
    'create': ('data3.json', None),
    'file': 'data3.json',
    'default_data': {'fallback': True},
    'expected': {
        'data': {'fallback': True},
        'load': True,
        'status': JsonLoader.Status.SUCCESS | JsonLoader.Status.DEFAULT_DATA |
        JsonLoader.Status.FILE_IS_DIR,
        'mode': JsonLoader.Mode.FALLBACK | JsonLoader.Mode.REMOVE |
        JsonLoader.Mode.LOAD
    }
}, {
    # Junk data
    'id': '4',
    'create': ('data4.json', '{{invalidata}'),
    'file': 'data4.json',
    'default_data': {},
    'expected': {
        'data': {},
        'load': True,
        'status': JsonLoader.Status.SUCCESS | JsonLoader.Status.DEFAULT_DATA,
        'mode': JsonLoader.Mode.FALLBACK | JsonLoader.Mode.REMOVE |
        JsonLoader.Mode.LOAD
    }
}, {
    # Junk data
    'id': '4',
    'file': 'data4.json',
    # Can't be jsoned
    'default_data': set(),
    'expected': {
        'data': None,
        'load': False,
        'status': JsonLoader.Status.FAIL | JsonLoader.Status.CANNOT_WRITE_FILE,
        'mode': JsonLoader.Mode.FALLBACK
    }
}, {
    # No remove
    'id': '3',
    'mode': JsonLoader.Mode.NO_REMOVE,
    'create': ('data3.json', None),
    'file': 'data3.json',
    'default_data': {'fallback': True},
    'expected': {
        'data': None,
        'load': False,
        'status': JsonLoader.Status.FAIL,
        'mode': JsonLoader.Mode.NO_REMOVE | JsonLoader.Mode.LOAD
    }
}, ]


@pytest.mark.parametrize('test_spec', test_spec_json)
def test_json(test_spec):
    _id = test_spec['id']
    default_data = test_spec['default_data']
    file = test_spec['file']
    if file:
        file = os.path.join(temp_dir, file)
    create = test_spec.get('create', None)
    fname = None
    if create:
        fname, data = create
        oscreate(fname, data)
    try:
        mode = test_spec.get('mode', 0)

        expected_data = test_spec['expected']['data']
        expected_loaded = test_spec['expected']['load']
        expected_status = test_spec['expected']['status']
        expected_mode = test_spec['expected']['mode']

        name = 'Test' + _id

        loader = JsonLoader(file, default_data, name=name, mode=mode)

        loaded = loader.load()
        assert expected_status == loader.status
        assert expected_mode == loader.mode
        assert expected_data == loader.data
        assert expected_loaded == loaded
    finally:
        osremove(file)
        if fname:
            osremove(fname)


test_spec_json_currency = [{
    # Test simple
    'create': (
        'data1.json',
        {'exchange_rates': {}, 'last_update_timestamp': 0}
    ),
    'file': 'data1.json',
    'expected': {
        'data':  {'exchange_rates': {}, 'last_update_timestamp': 0},
        'load': True,
        'status': CurrencyCacheLoader.Status.SUCCESS,
        'mode': CurrencyCacheLoader.Mode.VALIDATE |
        CurrencyCacheLoader.Mode.LOAD
    }
}, {
    # Test valid
    'create': (
        'data8.json',
        {'exchange_rates': {
            'EUR': {'rate': 1, 'timestamp_refresh': 0},
            'BTC': {'rate': 1000, 'timestamp_refresh': 0},
            'CAD': {'rate': 0.75, 'timestamp_refresh': 0},
            'RON': {'rate': 0.20, 'timestamp_refresh': 0},
        }, 'last_update_timestamp': 0}
    ),
    'file': 'data8.json',
    'expected': {
        'data':  {'exchange_rates': {
            'EUR': {'rate': 1, 'timestamp_refresh': 0},
            'BTC': {'rate': 1000, 'timestamp_refresh': 0},
            'CAD': {'rate': 0.75, 'timestamp_refresh': 0},
            'RON': {'rate': 0.20, 'timestamp_refresh': 0},
        }, 'last_update_timestamp': 0},
        'load': True,
        'status': CurrencyCacheLoader.Status.SUCCESS,
        'mode': CurrencyCacheLoader.Mode.VALIDATE |
        CurrencyCacheLoader.Mode.LOAD
    }
}, {
    # Test invalid 1
    'create': (
        'data2.json',
        'Invalid data'
    ),
    'file': 'data2.json',
    'expected': {
        'data':  {'exchange_rates': {}, 'last_update_timestamp': 0},
        'load': True,
        'status': CurrencyCacheLoader.Status.INVALID_DATA |
        CurrencyCacheLoader.Status.SUCCESS |
        CurrencyCacheLoader.Status.DEFAULT_DATA,
        'mode': CurrencyCacheLoader.Mode.VALIDATE |
        CurrencyCacheLoader.Mode.FALLBACK |
        CurrencyCacheLoader.Mode.LOAD
    }
}, {
    # Test invalid 2
    'create': (
        'data3.json',
        {'exchange-rates': 'some invalid rates', 'last_update_timestamp': 0}
    ),
    'file': 'data3.json',
    'expected': {
            'data':  {'exchange_rates': {}, 'last_update_timestamp': 0},
            'load': True,
            'status': CurrencyCacheLoader.Status.INVALID_DATA |
            CurrencyCacheLoader.Status.SUCCESS |
            CurrencyCacheLoader.Status.DEFAULT_DATA,
            'mode': CurrencyCacheLoader.Mode.VALIDATE |
            CurrencyCacheLoader.Mode.FALLBACK |
            CurrencyCacheLoader.Mode.LOAD
    }
}, {
    # Test invalid 3
    'create': (
        'data4.json',
        {'exchange_rates': {}, 'last_update_timestamp': 'invalid'}
    ),
    'file': 'data4.json',
    'expected': {
            'data':  {'exchange_rates': {}, 'last_update_timestamp': 0},
            'load': True,
            'status': CurrencyCacheLoader.Status.INVALID_DATA |
            CurrencyCacheLoader.Status.SUCCESS |
            CurrencyCacheLoader.Status.DEFAULT_DATA,
            'mode': CurrencyCacheLoader.Mode.VALIDATE |
            CurrencyCacheLoader.Mode.FALLBACK |
            CurrencyCacheLoader.Mode.LOAD
    }
}, {
    # Test invalid 4
    'create': (
        'data5.json',
        {'exchange_rates': {'rate': 1}, 'last_update_timestamp': 0}
    ),
    'file': 'data5.json',
    'expected': {
            'data':  {'exchange_rates': {}, 'last_update_timestamp': 0},
            'load': True,
            'status': CurrencyCacheLoader.Status.INVALID_DATA |
            CurrencyCacheLoader.Status.SUCCESS |
            CurrencyCacheLoader.Status.DEFAULT_DATA,
            'mode': CurrencyCacheLoader.Mode.VALIDATE |
            CurrencyCacheLoader.Mode.FALLBACK |
            CurrencyCacheLoader.Mode.LOAD
    }
}, {
    # Test invalid 5
    'create': (
        'data6.json',
        {'exchange_rates': {
            'EUR': {'rate': 'a', 'timestamp_refresh': 0}
        }, 'last_update_timestamp': 0}
    ),
    'file': 'data6.json',
    'expected': {
            'data':  {'exchange_rates': {}, 'last_update_timestamp': 0},
            'load': True,
            'status': CurrencyCacheLoader.Status.INVALID_DATA |
            CurrencyCacheLoader.Status.SUCCESS |
            CurrencyCacheLoader.Status.DEFAULT_DATA,
            'mode': CurrencyCacheLoader.Mode.VALIDATE |
            CurrencyCacheLoader.Mode.FALLBACK |
            CurrencyCacheLoader.Mode.LOAD
    }
}, {
    # Test invalid 7
    'create': (
        'data8.json',
        {'exchange_rates': {
            'EUR': {'rate': 1, 'timestamp_refresh': 'a'}
        }, 'last_update_timestamp': 0}
    ),
    'file': 'data8.json',
    'expected': {
            'data':  {'exchange_rates': {}, 'last_update_timestamp': 0},
            'load': True,
            'status': CurrencyCacheLoader.Status.INVALID_DATA |
            CurrencyCacheLoader.Status.SUCCESS |
            CurrencyCacheLoader.Status.DEFAULT_DATA,
            'mode': CurrencyCacheLoader.Mode.VALIDATE |
            CurrencyCacheLoader.Mode.FALLBACK |
            CurrencyCacheLoader.Mode.LOAD
    }
}, ]


@pytest.mark.parametrize('test_spec', test_spec_json_currency)
def test_json_currency(test_spec):
    file = test_spec['file']
    if file:
        file = os.path.join(temp_dir, file)
    create = test_spec.get('create', None)
    fname = None
    if create:
        fname, data = create
        if data is not None:
            data = json.dumps(data)
        oscreate(fname, data)
    try:
        expected_data = test_spec['expected']['data']
        expected_loaded = test_spec['expected']['load']
        expected_status = test_spec['expected']['status']
        expected_mode = test_spec['expected']['mode']

        loader = CurrencyCacheLoader(file)

        loaded = loader.load()
        assert expected_status == loader.status
        assert expected_mode == loader.mode
        assert expected_data == loader.data
        assert expected_loaded == loaded
    finally:
        osremove(file)
        if fname:
            osremove(fname)


class MockLoader(Loader):
    @Loader.Decorators.without_status(Loader.Status.PENDING)
    def without_pending(self):
        assert False

    @Loader.Decorators.with_status(Loader.Status.PENDING)
    def with_pending(self):
        assert False


def test_coverage():
    loader = MockLoader(status=Loader.Status.PENDING, mode=0)
    loader.without_pending()
    with pytest.raises(AssertionError):
        loader.with_pending()

    loader = MockLoader()
    loader.with_pending()
    with pytest.raises(AssertionError):
        loader.without_pending()
