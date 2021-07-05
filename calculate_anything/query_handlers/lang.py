import os
import json
from ..utils import Singleton
from ..constants import MAIN_DIR
from ..logging_wrapper import LoggingWrapper as logging

class Language:
    def __init__(self):
        self._lang = None
        self._data = {}
        self._logger = logging.getLogger(__name__)
        self.set('en_US')

    def set(self, lang):
        if lang == self._lang:
            return
        lang_filepath = os.path.join(MAIN_DIR, 'lang', '{}.json'.format(lang))
        if not os.path.exists(lang_filepath):
            return
        try:
            with open(lang_filepath) as f:
                self._data = json.loads(f.read())
        except Exception as e:
            self._logger.error('Could not load language, falling back to en_US')
        self._lang = 'en_US'

    def translate(self, word, mode):
        word = str(word)
        return self._data.get(mode, {}).get(word, word)

    def get_translator(self, mode):
        def _translator(word):
            return self.translate(word, mode)
        return _translator


    @classmethod
    @Singleton
    def get_instance(cls):
        return cls()
