import os
import json
import unicodedata
from .utils import Singleton, replace_dict_re_func
from .constants import MAIN_DIR
from .logging_wrapper import LoggingWrapper as logging

class Language(metaclass=Singleton):
    def __init__(self):
        self._lang = None
        self._data = {}
        self._logger = logging.getLogger(__name__)
        self.set('en_US')

    @staticmethod
    def strip_accents(s):
        return ''.join(
            c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
        )

    def set(self, lang):
        if lang == self._lang:
            return
        lang_filepath = os.path.join(MAIN_DIR, 'data', 'lang', '{}.json'.format(lang))
        if not os.path.exists(lang_filepath):
            self._logger.error('Language file does not exist: {}'.format(lang_filepath))
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

    def add_translation(self, word, translated_word, mode):
        if mode not in self._data:
            self._data[mode] = {}
        self._data[mode][word] = translated_word

    def get_translation_adder(self, mode):
        def _translation_adder(word, translated_word):
            self.add_translation(word, translated_word, mode)
        return _translation_adder

    def replace_all(self, string, mode, ignorecase=True):
        if mode not in self._data:
            return string
        
        return replace_dict_re_func(
            self._data[mode],
            sort=True,
            ignorecase=ignorecase
        )(string)

    def get_replacer(self, mode, ignorecase=True):
        def _replacer(string):
            return self.replace_all(string, mode, ignorecase)
        return _replacer