import os
import json
import logging
from ..utils import Singleton
import __main__

class Language:
    def __init__(self):
        self._lang = None
        self._data = {}
        self._logger = logging.getLogger(__name__)
        self.set('en_US')

    def set(self, lang):
        if lang == self._lang:
            return
        main_dir = os.path.dirname(os.path.realpath(__main__.__file__))
        lang_filepath = os.path.join(main_dir, 'lang', '{}.json'.format(lang))
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
