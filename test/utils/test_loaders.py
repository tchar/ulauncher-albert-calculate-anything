import json
import pytest
from calculate_anything.utils.loaders import (
    SqliteLoader,
    JsonLoader,
    CurrencyCacheLoader,
)
from calculate_anything.utils.loaders.loader import Loader
from test.tutils import temp_file, temp_filepath, osremove


test_spec_sqlite = [
    {
        # No sql file no sqlite file
        'id': '1',
        'sqlite_file': 'timezones1.sqlite3',
        'sql_file': None,
        'expected': {
            'load': False,
            'status': SqliteLoader.Status.FAIL,
            'mode': SqliteLoader.Mode.CREATE,
        },
    },
    {
        # No sql file
        'id': '2',
        'create': [('timezones2.sqlite3', '')],
        'sqlite_file': 'timezones2.sqlite3',
        'sql_file': 'timezones2.sql',
        'expected': {
            'load': True,
            'status': SqliteLoader.Status.SUCCESS,
            'mode': SqliteLoader.Mode.LOAD,
        },
    },
    {
        # No sqlite file
        'id': '3',
        'create': [('timezones3.sql', '')],
        'sqlite_file': 'timezones3.sqlite3',
        'sql_file': 'timezones3.sql',
        'expected': {
            'load': True,
            'status': SqliteLoader.Status.SUCCESS,
            'mode': SqliteLoader.Mode.CREATE,
        },
    },
    {
        # Both file sqlite more recent
        'id': '4',
        'create': [
            ('timezones4.sqlite3', ''),
            ('timezones4.sql', ''),
        ],
        'sqlite_file': 'timezones4.sqlite3',
        'sql_file': 'timezones4.sql',
        'expected': {
            'load': True,
            'status': SqliteLoader.Status.SUCCESS,
            'mode': SqliteLoader.Mode.CREATE | SqliteLoader.Mode.REMOVE,
        },
    },
    {
        # Both file sql more recent
        'id': '5',
        'create': [
            ('timezones5.sql', ''),
            ('timezones5.sqlite3', ''),
        ],
        'sqlite_file': 'timezones5.sqlite3',
        'sql_file': 'timezones5.sql',
        'expected': {
            'load': True,
            'status': SqliteLoader.Status.SUCCESS,
            'mode': SqliteLoader.Mode.LOAD,
        },
    },
    {
        # No sql file, sqlite is a directory
        'id': '6',
        'create': [
            ('timezones6.sqlite3', None),
        ],
        'sqlite_file': 'timezones6.sqlite3',
        'sql_file': 'timezones6.sql',
        'expected': {
            'load': False,
            'status': SqliteLoader.Status.FAIL
            | SqliteLoader.Status.FILE_IS_DIR,
            'mode': SqliteLoader.Mode.LOAD
            | SqliteLoader.Mode.CREATE
            | SqliteLoader.Mode.REMOVE,
        },
    },
    {
        # Sqlite is a directory
        'id': '7',
        'create': [('timezones7.sqlite3', None), ('timezones7.sql', '')],
        'sqlite_file': 'timezones7.sqlite3',
        'sql_file': 'timezones7.sql',
        'expected': {
            'load': True,
            'status': SqliteLoader.Status.SUCCESS
            | SqliteLoader.Status.FILE_IS_DIR,
            'mode': SqliteLoader.Mode.CREATE | SqliteLoader.Mode.REMOVE,
        },
    },
    {
        # Sql file giberish
        'id': '8',
        'create': [('timezones8.sql', 'INSERT INTO WHAT THE FUCK?')],
        'sqlite_file': 'timezones8.sqlite3',
        'sql_file': 'timezones8.sql',
        'expected': {
            'load': False,
            'status': SqliteLoader.Status.FAIL
            | SqliteLoader.Status.INVALID_DATA,
            'mode': SqliteLoader.Mode.CREATE,
        },
    },
    {
        # Use memory
        'id': '9',
        'create': [('timezones9.sql', 'CREATE TABLE test (id INTEGER)')],
        'mode': SqliteLoader.Mode.MEMORY,
        'sqlite_file': 'timezones9.sqlite3',
        'sql_file': 'timezones9.sql',
        'expected': {
            'load': True,
            'status': SqliteLoader.Status.SUCCESS,
            'mode': SqliteLoader.Mode.MEMORY | SqliteLoader.Mode.CREATE,
        },
    },
    {
        # Fail memory
        'id': '10',
        'mode': SqliteLoader.Mode.MEMORY,
        'sqlite_file': 'timezones10.sqlite3',
        'sql_file': 'timezones10.sql',
        'expected': {
            'load': False,
            'status': SqliteLoader.Status.FAIL,
            'mode': SqliteLoader.Mode.MEMORY | SqliteLoader.Mode.CREATE,
        },
    },
    {
        # Fail can't read sql file
        'id': '11',
        'create': [('timezones11.sql', None)],
        'sqlite_file': 'timezones11.sqlite3',
        'sql_file': 'timezones11.sql',
        'expected': {
            'load': False,
            'status': SqliteLoader.Status.FAIL,
            'mode': SqliteLoader.Mode.CREATE,
        },
    },
    {
        # Fail with no remove
        'id': '12',
        'mode': SqliteLoader.Mode.NO_REMOVE,
        'sqlite_file': 'timezones12.sqlite3',
        'sql_file': 'timezones12.sql',
        'expected': {
            'load': False,
            'status': SqliteLoader.Status.FAIL,
            'mode': SqliteLoader.Mode.CREATE | SqliteLoader.Mode.NO_REMOVE,
        },
    },
]


@pytest.mark.parametrize('test_spec', test_spec_sqlite)
def test_sqlite(test_spec):
    loader = None
    create = test_spec.get('create', [])

    sqlite_fpath = test_spec['sqlite_file']
    if sqlite_fpath:
        sqlite_fpath = temp_filepath(sqlite_fpath)

    sql_fpath = test_spec['sql_file']
    if sql_fpath:
        sql_fpath = temp_filepath(sql_fpath)

    mode = test_spec.get('mode', 0)
    expected_loaded = test_spec['expected']['load']
    expected_status = test_spec['expected']['status']
    expected_mode = test_spec['expected']['mode']

    with temp_file(*create, sleep=0.01):
        loader = SqliteLoader(sqlite_fpath, sql_fpath, mode=mode)
        loaded = loader.load()
        assert expected_status == loader.status
        assert expected_mode == loader.mode
        assert expected_loaded == loaded
        loader.close()
    osremove(sqlite_fpath)
    osremove(sql_fpath)


test_spec_json = [
    {
        # No file
        'id': '1',
        'file': 'datajson1.json',
        'default_data': None,
        'expected': {
            'data': None,
            'load': False,
            'status': JsonLoader.Status.FAIL,
            'mode': JsonLoader.Mode.FALLBACK,
        },
    },
    {
        # File
        'id': '2',
        'create': ('datajson2.json', '{"some-key": "some-value"}'),
        'file': 'datajson2.json',
        'default_data': {},
        'expected': {
            'data': {'some-key': 'some-value'},
            'load': True,
            'status': JsonLoader.Status.SUCCESS,
            'mode': JsonLoader.Mode.LOAD | JsonLoader.Mode.VALIDATE,
        },
    },
    {
        # File
        'id': '3',
        'create': ('datajson3.json', None),
        'file': 'datajson3.json',
        'default_data': {'fallback': True},
        'expected': {
            'data': {'fallback': True},
            'load': True,
            'status': JsonLoader.Status.SUCCESS
            | JsonLoader.Status.DEFAULT_DATA
            | JsonLoader.Status.FILE_IS_DIR,
            'mode': JsonLoader.Mode.FALLBACK
            | JsonLoader.Mode.REMOVE
            | JsonLoader.Mode.LOAD,
        },
    },
    {
        # Junk data
        'id': '4',
        'create': ('datajson4.json', '{{invalidata}'),
        'file': 'datajson4.json',
        'default_data': {},
        'expected': {
            'data': {},
            'load': True,
            'status': JsonLoader.Status.SUCCESS
            | JsonLoader.Status.DEFAULT_DATA,
            'mode': JsonLoader.Mode.FALLBACK
            | JsonLoader.Mode.REMOVE
            | JsonLoader.Mode.LOAD,
        },
    },
    {
        # Junk data
        'id': '5',
        'file': 'datajson5.json',
        # Can't be jsoned
        'default_data': set(),
        'expected': {
            'data': None,
            'load': False,
            'status': JsonLoader.Status.FAIL
            | JsonLoader.Status.CANNOT_WRITE_FILE,
            'mode': JsonLoader.Mode.FALLBACK,
        },
    },
    {
        # No remove
        'id': '6',
        'mode': JsonLoader.Mode.NO_REMOVE,
        'create': ('datajson3.json', None),
        'file': 'datajson3.json',
        'default_data': {'fallback': True},
        'expected': {
            'data': None,
            'load': False,
            'status': JsonLoader.Status.FAIL,
            'mode': JsonLoader.Mode.NO_REMOVE | JsonLoader.Mode.LOAD,
        },
    },
]


@pytest.mark.parametrize('test_spec', test_spec_json)
def test_json(test_spec):
    default_data = test_spec['default_data']

    file = test_spec['file']
    if file:
        file = temp_filepath(file)

    create = test_spec.get('create')

    mode = test_spec.get('mode', 0)
    expected_data = test_spec['expected']['data']
    expected_loaded = test_spec['expected']['load']
    expected_status = test_spec['expected']['status']
    expected_mode = test_spec['expected']['mode']
    with temp_file(create):
        loader = JsonLoader(file, default_data, mode=mode)
        loaded = loader.load()
        assert expected_status == loader.status
        assert expected_mode == loader.mode
        assert expected_data == loader.data
        assert expected_loaded == loaded
    osremove(file)


test_spec_json_currency = [
    {
        # Test simple
        'create': (
            'datajsoncurrency1.json',
            {'exchange_rates': {}, 'last_update_timestamp': 0},
        ),
        'file': 'datajsoncurrency1.json',
        'expected': {
            'data': {'exchange_rates': {}, 'last_update_timestamp': 0},
            'load': True,
            'status': CurrencyCacheLoader.Status.SUCCESS,
            'mode': CurrencyCacheLoader.Mode.VALIDATE
            | CurrencyCacheLoader.Mode.LOAD,
        },
    },
    {
        # Test valid
        'create': (
            'datajsoncurrency8.json',
            {
                'exchange_rates': {
                    'EUR': {'rate': 1, 'timestamp_refresh': 0},
                    'BTC': {'rate': 1000, 'timestamp_refresh': 0},
                    'CAD': {'rate': 0.75, 'timestamp_refresh': 0},
                    'RON': {'rate': 0.20, 'timestamp_refresh': 0},
                },
                'last_update_timestamp': 0,
            },
        ),
        'file': 'datajsoncurrency8.json',
        'expected': {
            'data': {
                'exchange_rates': {
                    'EUR': {'rate': 1, 'timestamp_refresh': 0},
                    'BTC': {'rate': 1000, 'timestamp_refresh': 0},
                    'CAD': {'rate': 0.75, 'timestamp_refresh': 0},
                    'RON': {'rate': 0.20, 'timestamp_refresh': 0},
                },
                'last_update_timestamp': 0,
            },
            'load': True,
            'status': CurrencyCacheLoader.Status.SUCCESS,
            'mode': CurrencyCacheLoader.Mode.VALIDATE
            | CurrencyCacheLoader.Mode.LOAD,
        },
    },
    {
        # Test invalid 1
        'create': ('datajsoncurrency2.json', 'Invalid data'),
        'file': 'datajsoncurrency2.json',
        'expected': {
            'data': {'exchange_rates': {}, 'last_update_timestamp': 0},
            'load': True,
            'status': CurrencyCacheLoader.Status.INVALID_DATA
            | CurrencyCacheLoader.Status.SUCCESS
            | CurrencyCacheLoader.Status.DEFAULT_DATA,
            'mode': CurrencyCacheLoader.Mode.VALIDATE
            | CurrencyCacheLoader.Mode.FALLBACK
            | CurrencyCacheLoader.Mode.LOAD,
        },
    },
    {
        # Test invalid 2
        'create': (
            'datajsoncurrency3.json',
            {
                'exchange-rates': 'some invalid rates',
                'last_update_timestamp': 0,
            },
        ),
        'file': 'datajsoncurrency3.json',
        'expected': {
            'data': {'exchange_rates': {}, 'last_update_timestamp': 0},
            'load': True,
            'status': CurrencyCacheLoader.Status.INVALID_DATA
            | CurrencyCacheLoader.Status.SUCCESS
            | CurrencyCacheLoader.Status.DEFAULT_DATA,
            'mode': CurrencyCacheLoader.Mode.VALIDATE
            | CurrencyCacheLoader.Mode.FALLBACK
            | CurrencyCacheLoader.Mode.LOAD,
        },
    },
    {
        # Test invalid 3
        'create': (
            'datajsoncurrency4.json',
            {'exchange_rates': {}, 'last_update_timestamp': 'invalid'},
        ),
        'file': 'datajsoncurrency4.json',
        'expected': {
            'data': {'exchange_rates': {}, 'last_update_timestamp': 0},
            'load': True,
            'status': CurrencyCacheLoader.Status.INVALID_DATA
            | CurrencyCacheLoader.Status.SUCCESS
            | CurrencyCacheLoader.Status.DEFAULT_DATA,
            'mode': CurrencyCacheLoader.Mode.VALIDATE
            | CurrencyCacheLoader.Mode.FALLBACK
            | CurrencyCacheLoader.Mode.LOAD,
        },
    },
    {
        # Test invalid 4
        'create': (
            'datajsoncurrency5.json',
            {'exchange_rates': {'rate': 1}, 'last_update_timestamp': 0},
        ),
        'file': 'datajsoncurrency5.json',
        'expected': {
            'data': {'exchange_rates': {}, 'last_update_timestamp': 0},
            'load': True,
            'status': CurrencyCacheLoader.Status.INVALID_DATA
            | CurrencyCacheLoader.Status.SUCCESS
            | CurrencyCacheLoader.Status.DEFAULT_DATA,
            'mode': CurrencyCacheLoader.Mode.VALIDATE
            | CurrencyCacheLoader.Mode.FALLBACK
            | CurrencyCacheLoader.Mode.LOAD,
        },
    },
    {
        # Test invalid 5
        'create': (
            'datajsoncurrency6.json',
            {
                'exchange_rates': {
                    'EUR': {'rate': 'a', 'timestamp_refresh': 0}
                },
                'last_update_timestamp': 0,
            },
        ),
        'file': 'datajsoncurrency6.json',
        'expected': {
            'data': {'exchange_rates': {}, 'last_update_timestamp': 0},
            'load': True,
            'status': CurrencyCacheLoader.Status.INVALID_DATA
            | CurrencyCacheLoader.Status.SUCCESS
            | CurrencyCacheLoader.Status.DEFAULT_DATA,
            'mode': CurrencyCacheLoader.Mode.VALIDATE
            | CurrencyCacheLoader.Mode.FALLBACK
            | CurrencyCacheLoader.Mode.LOAD,
        },
    },
    {
        # Test invalid 6
        'create': (
            'datajsoncurrency7.json',
            {
                'exchange_rates': {
                    'EUR': {'rate': 1, 'timestamp_refresh': 'a'}
                },
                'last_update_timestamp': 0,
            },
        ),
        'file': 'datajsoncurrency7.json',
        'expected': {
            'data': {'exchange_rates': {}, 'last_update_timestamp': 0},
            'load': True,
            'status': CurrencyCacheLoader.Status.INVALID_DATA
            | CurrencyCacheLoader.Status.SUCCESS
            | CurrencyCacheLoader.Status.DEFAULT_DATA,
            'mode': CurrencyCacheLoader.Mode.VALIDATE
            | CurrencyCacheLoader.Mode.FALLBACK
            | CurrencyCacheLoader.Mode.LOAD,
        },
    },
]


@pytest.mark.parametrize('test_spec', test_spec_json_currency)
def test_json_currency(test_spec):
    file = test_spec['file']
    if file:
        file = temp_filepath(file)
    create = test_spec.get('create', None)
    if create:
        fname, data = create
        data = json.dumps(data)
        create = (fname, data)

    expected_data = test_spec['expected']['data']
    expected_loaded = test_spec['expected']['load']
    expected_status = test_spec['expected']['status']
    expected_mode = test_spec['expected']['mode']
    with temp_file(create):
        loader = CurrencyCacheLoader(file)
        loaded = loader.load()

        assert expected_status == loader.status
        assert expected_mode == loader.mode
        assert expected_data == loader.data
        assert expected_loaded == loaded
    osremove(file)


class MockLoader(Loader):
    @Loader.Decorators.without_status(Loader.Status.PENDING)
    def without_pending(self):
        assert False

    @Loader.Decorators.with_status(Loader.Status.PENDING)
    def with_pending(self):
        assert False

    def load(self) -> None:
        pass

    @property
    def data(self) -> None:
        return None


def test_coverage():
    loader = MockLoader(status=Loader.Status.PENDING, mode=0)
    loader.without_pending()
    with pytest.raises(AssertionError):
        loader.with_pending()

    loader = MockLoader()
    loader.with_pending()
    with pytest.raises(AssertionError):
        loader.without_pending()
