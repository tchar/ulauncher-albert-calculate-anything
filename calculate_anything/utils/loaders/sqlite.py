import os
import shutil

try:
    import sqlite3
except ImportError:  # pragma: no cover
    sqlite3 = None
from calculate_anything.utils.loaders.loader import Loader
from calculate_anything import logging


__all__ = ['SqliteLoader']


logger = logging.getLogger(__name__)


class SqliteLoader(Loader):
    def __init__(
        self, sqlite_filepath: str, sql_filepath: str = None, mode: int = 0
    ) -> None:
        super().__init__(Loader.Status.PENDING, mode)
        self.sqlite_filepath = sqlite_filepath
        self.sql_filepath = sql_filepath
        self._reset()

    def _reset(self) -> None:
        self.db = None
        self._sqlite_file_exists = None
        self._sql_file_exists = None
        self._sqlite_file_mtime = None
        self._sql_file_mtime = None
        self._sql_data = None
        self._sql_data_loaded = False

    @Loader.Decorators.without_status(Loader.Status.FAIL)
    def _pre_load(self) -> None:
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

        if (
            self._sqlite_file_exists
            and self._sql_file_exists
            and self._sqlite_file_mtime >= self._sql_file_mtime
        ):
            self._mode |= Loader.Mode.LOAD
        elif (
            self._sqlite_file_exists
            and self._sql_file_exists
            and self._sqlite_file_mtime < self._sql_file_mtime
        ):
            self._mode |= Loader.Mode.REMOVE
        elif not self._sqlite_file_exists:
            self._mode |= Loader.Mode.CREATE
        else:
            self._mode |= Loader.Mode.LOAD

    @Loader.Decorators.without_status(Loader.Status.FAIL)
    @Loader.Decorators.with_mode(Loader.Mode.LOAD)
    def _load(self) -> None:
        try:
            self.db = db = sqlite3.connect(
                self.sqlite_filepath,
                check_same_thread=False,
                cached_statements=500,
            )
            db.cursor().execute('PRAGMA foreign_keys = ON;').close()
            self._status |= Loader.Status.SUCCESS
            msg = 'Loaded timezone database: {}'
            msg = msg.format(self.sqlite_filepath)
            logger.info(msg)
        except Exception as e:
            msg = 'Could not read database file: {}'
            msg = msg.format(e)
            logger.exception(msg)
            self._mode |= Loader.Mode.REMOVE

    @Loader.Decorators.without_status(Loader.Status.FAIL)
    @Loader.Decorators.without_mode(Loader.Mode.NO_REMOVE)
    @Loader.Decorators.with_mode(Loader.Mode.REMOVE)
    def _remove(self) -> None:
        if os.path.isdir(self.sqlite_filepath):
            self._status |= Loader.Status.FILE_IS_DIR
            try:
                shutil.rmtree(self.sqlite_filepath)
            except Exception as e:  # pragma: no cover
                self._mode |= Loader.Mode.MEMORY
                msg = 'Could not remove directory database {}: {}'
                msg = msg.format(self.sqlite_filepath, e)
                logger.exception(msg)
                return
        else:
            try:
                os.remove(self.sqlite_filepath)
            except Exception as e:  # pragma: no cover
                self._mode |= Loader.Mode.MEMORY
                msg = 'Could not remove file database {}: {}'
                msg = msg.format(self.sqlite_filepath, e)
                logger.exception(msg)
                return

        logger.info('Found new timezones, cleared database')
        self._mode |= Loader.Mode.CREATE

    @Loader.Decorators.with_data
    @Loader.Decorators.without_status(Loader.Status.FAIL)
    def _execute_script(self) -> None:
        db = self.db
        data = self.data
        try:
            cursor = db.cursor()
            cursor.executescript(data)
            cursor.execute('PRAGMA foreign_keys = ON;')
            db.commit()
            cursor.close()
            self._status |= Loader.Status.SUCCESS
        except Exception as e:
            msg = 'Could not execute sql file {}: {}'
            msg = msg.format(self.sql_filepath, e)
            logger.exception(msg)
            self._status |= Loader.Status.FAIL
            self._status |= Loader.Status.INVALID_DATA

    @Loader.Decorators.with_data
    @Loader.Decorators.with_mode(Loader.Mode.CREATE)
    @Loader.Decorators.without_status(Loader.Status.FAIL)
    def _create(self) -> None:
        try:
            self.db = sqlite3.connect(
                self.sqlite_filepath,
                check_same_thread=False,
                cached_statements=500,
            )
            msg = 'Did not find sqlite db {}, created from scratch'
            msg = msg.format(self.sqlite_filepath)
            logger.info(msg)
        # Can't test this without huge hacks
        # In case we can't remove the file/directory
        # Use memory
        except Exception as e:  # pragma: no cover
            msg = 'Could not create database {}: {}'  # pragma: no cover
            msg = msg.format(self.sqlite_filepath, e)
            logger.exception(msg)
            self._mode |= Loader.Mode.MEMORY
            return
        self._execute_script()

    @Loader.Decorators.with_data
    @Loader.Decorators.without_status(Loader.Status.FAIL)
    @Loader.Decorators.with_mode(Loader.Mode.MEMORY)
    def _create_memory(self) -> None:
        self.db = sqlite3.connect(
            ':memory:', check_same_thread=False, cached_statements=500
        )
        logger.info('Fell back to memory')
        self._execute_script()

    @property
    @Loader.Decorators.without_status(Loader.Status.FAIL)
    def data(self) -> None:
        if self._sql_data_loaded:
            return self._sql_data
        if self.sql_filepath is None or not self._sql_file_exists:
            self._sql_data_loaded = True
            self._sql_data = None
            return None
        try:
            with open(self.sql_filepath, 'r', encoding='utf-8') as f:
                data = f.read()
        except Exception as e:
            msg = 'Could not read sql file {}: {}'
            msg = msg.format(self.sql_filepath, e)
            logger.exception(msg)
            data = None
        self._sql_data = data
        self._sql_data_loaded = True
        return data

    def load(self) -> None:
        if sqlite3 is None:
            return False  # pragma: no cover

        self._pre_load()
        self._load()
        self._remove()
        self._create()
        self._create_memory()

        # Some cleanup
        self._status &= ~Loader.Status.PENDING
        if self._mode & Loader.Mode.NO_REMOVE:
            self._mode &= ~Loader.Mode.REMOVE
        if not (self.status & Loader.Status.SUCCESS):
            self._status |= Loader.Status.FAIL
        return self.status & Loader.Status.SUCCESS == 1

    def close(self) -> None:
        if self.db is not None:
            self.db.close()
        self._reset()
