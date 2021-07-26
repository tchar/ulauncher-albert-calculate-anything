import os
import json
import re
from typing import Callable
import unicodedata
from calculate_anything.utils.singleton import Singleton
from calculate_anything.utils.misc import safe_operation
from calculate_anything.utils import multi_re
from calculate_anything.constants import MAIN_DIR
import calculate_anything.log as logging


class LanguageService(metaclass=Singleton):
    def __init__(self):
        self._lang = None
        self._data = {}
        self._update_callbacks = []
        self._logger = logging.getLogger(__name__)

    @staticmethod
    def strip_accents(s):
        return ''.join(
            c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
        )

    def set(self, lang):
        if lang == self._lang:
            return
        fallback = False
        lang_filepath = os.path.join(
            MAIN_DIR, 'data', 'lang', '{}.json'.format(lang))
        if not os.path.exists(lang_filepath):
            self._logger.error(
                'Language file does not exist: {}'.format(lang_filepath))
            fallback = True
        if not fallback:
            try:
                with open(lang_filepath) as f:
                    self._data = json.loads(f.read())
            except Exception as e:
                self._logger.error(
                    'Could not load language, falling back to en_US')
                fallback = True

        if fallback:
            if lang == 'en_US':
                self._logger.error(
                    'en_US does not exist, will not use any language aliases: {}'.format(lang_filepath))
                return
            return self.set('en_US')

        self._lang = lang
        for callback in self._update_callbacks:
            with safe_operation():
                callback(lang)

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

        return multi_re.sub_dict(
            self._data[mode],
            string,
            flags=re.IGNORECASE if ignorecase else 0,
            sort=True
        )

    def get_replacer(self, mode, ignorecase=True):
        def _replacer(string):
            return self.replace_all(string, mode, ignorecase)
        return _replacer

    def add_update_callback(self, callback: Callable[[str], None]) -> None:
        self._update_callbacks.append(callback)
