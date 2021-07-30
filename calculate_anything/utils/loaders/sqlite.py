import os
import shutil
from functools import wraps
from enum import IntFlag
try:
    import sqlite3
except ImportError:  # pragma: no cover
    sqlite3 = None  # pragma: no cover
from calculate_anything import logging


__all__ = ['SqliteLoader']


class SqliteLoader:
    class Mode(IntFlag):
        LOAD = 1
        CREATE = LOAD << 1
        REMOVE = LOAD << 2
        MEMORY = LOAD << 3
        FAIL = LOAD << 4

    class Decorators:
        def with_sql_data(func):
            @wraps(func)
            def _wrapper(self, *args, **kwargs):
                if self.sql_data is None:
                    self._mode |= SqliteLoader.Mode.FAIL
                    return
                return func(self, *args, **kwargs)
            return _wrapper

        def with_no_fail(func):
            @wraps(func)
            def _wrapper(self, *args, **kwargs):
                if self._mode & SqliteLoader.Mode.FAIL:
                    return
                return func(self, *args, **kwargs)
            return _wrapper

    def __init__(self, sqlite_filepath,
                 sql_filepath=None, name=None, mode=None):
        self.sqlite_filepath = sqlite_filepath
        self.sql_filepath = sql_filepath
        self._mode = mode
        self._logger = logging.getLogger(__name__)
        if name is not None:
            self._logger = self._logger.getChild(name)
        self._reset()

    def _reset(self):
        self.db = None
        self._sqlite_file_exists = None
        self._sql_file_exists = None
        self._sqlite_file_mtime = None
        self._sql_file_mtime = None
        self._sql_data = None
        self._sql_data_loaded = False

    def _pre_load(self):
        self._sqlite_file_exists = False
        if self.sqlite_filepath is not None:
            self._sqlite_file_exists = os.path.exists(self.sqlite_filepath)
        if self._sqlite_file_exists:
            self._sqlite_file_mtime = os.path.getmtime(self.sqlite_filepath)
        else:
            self._sqlite_file_mtime = 0

        self._sql_file_exists = False
        if self.sql_filepath is not None:
            self._sql_file_exists = os.path.exists(self.sql_filepath)
        if self._sql_file_exists:
            self._sql_file_mtime = os.path.getmtime(self.sql_filepath)
        else:
            self._sql_file_mtime = 0

        if self._sqlite_file_exists and self._sql_file_exists and \
                self._sqlite_file_mtime >= self._sql_file_mtime:
            mode = SqliteLoader.Mode.LOAD
        elif self._sqlite_file_exists and self._sql_file_exists and \
                self._sqlite_file_mtime < self._sql_file_mtime:
            mode = SqliteLoader.Mode.REMOVE
        elif not self._sqlite_file_exists:
            mode = SqliteLoader.Mode.CREATE
        else:
            mode = SqliteLoader.Mode.LOAD

        self._mode = mode if self._mode is None else self._mode

    @Decorators.with_no_fail
    def _load(self):
        try:
            self.db = db = sqlite3.connect(
                self.sqlite_filepath,
                check_same_thread=False,
                cached_statements=500
            )
            db.cursor().execute('PRAGMA foreign_keys = ON;').close()
            msg = 'Loaded timezone database: {}'
            msg = msg.format(self.sqlite_filepath)
            self._logger.info(msg)
        except Exception as e:
            msg = 'Could not read database file: {}'
            msg = msg.format(e)
            self._logger.exception(e)
            self._mode |= SqliteLoader.Mode.REMOVE

    @Decorators.with_no_fail
    def _remove(self):
        try:
            if os.path.isdir(self.sqlite_filepath):
                shutil.rmtree(self.sqlite_filepath)
            else:
                os.remove(self.sqlite_filepath)
            self._logger.info('Found new timezones, cleared database')
            self._mode |= SqliteLoader.Mode.CREATE
        # Can't test this without huge hacks
        # In case we can't remove the file/directory
        # Use memory
        except Exception as e:  # pragma: no cover
            msg = 'Exception when removing database {}: {}'  # pragma: no cover
            msg = msg.format(self.sqlite_filepath, e)  # pragma: no cover
            self._logger.exception(msg)  # pragma: no cover
            self._mode |= SqliteLoader.Mode.MEMORY  # pragma: no cover

    @Decorators.with_no_fail
    def _execute_script(self, data):
        db = self.db
        try:
            cursor = db.cursor()
            cursor.executescript(data)
            cursor.execute('PRAGMA foreign_keys = ON;')
            db.commit()
            cursor.close()
        except Exception as e:
            msg = 'Could not execute sql file {}: {}'
            msg = msg.format(self.sql_filepath, e)
            self._logger.exception(msg)
            self._mode |= SqliteLoader.Mode.FAIL

    @Decorators.with_sql_data
    @Decorators.with_no_fail
    def _create(self):
        data = self.sql_data
        try:
            self.db = sqlite3.connect(
                self.sqlite_filepath,
                check_same_thread=False,
                cached_statements=500
            )
            msg = 'Did not find sqlite db {}, created from scratch'
            msg = msg.format(self.sqlite_filepath)
            self._logger.info(msg)
        # Can't test this without huge hacks
        # In case we can't remove the file/directory
        # Use memory
        except Exception as e:  # pragma: no cover
            msg = 'Could not create database {}: {}'  # pragma: no cover
            msg = msg.format(self.sqlite_filepath, e)  # pragma: no cover
            self._logger.exception(msg)  # pragma: no cover
            self._mode |= SqliteLoader.Mode.MEMORY  # pragma: no cover
            return  # pragma: no cover
        self._execute_script(data)

    @Decorators.with_sql_data
    @Decorators.with_no_fail
    def _create_memory(self):
        data = self.sql_data
        self.db = sqlite3.connect(
            ':memory:',
            check_same_thread=False,
            cached_statements=500
        )
        self._logger.info('Fell back to memory')
        self._execute_script(data)

    @property
    @Decorators.with_no_fail
    def sql_data(self):
        if self._sql_data_loaded:
            return self._sql_data
        if self.sql_filepath is None or not self._sql_file_exists:
            self._sql_data_loaded = True
            self._sql_data = None
            return None
        try:
            with open(self.sql_filepath, 'r') as f:
                data = f.read()
        except Exception as e:
            msg = 'Could not read sql file {}: {}'
            msg = msg.format(self.sql_filepath, e)
            self._logger.exception(msg)
            data = None
        self._sql_data = data
        self._sql_data_loaded = True
        return data

    @property
    def mode(self):
        return self._mode

    def load(self):
        if sqlite3 is None:
            return False  # pragma: no cover

        self._pre_load()
        if self.mode & SqliteLoader.Mode.LOAD:
            self._load()

        if self.mode & SqliteLoader.Mode.REMOVE:
            self._remove()

        if self.mode & SqliteLoader.Mode.CREATE:
            self._create()

        if self.mode & SqliteLoader.Mode.MEMORY:
            self._create_memory()

        return not (self.mode & SqliteLoader.Mode.FAIL)

    def close(self):
        if self.db is not None:
            self.db.close()
        self._reset()
