'''The language service used by Calculate Anything

The language service can be set a language and loads the
corresponding json file located at data/lang.

i.e data/lang/en_US.json
'''

import os
import json
import re
from typing import Callable
import unicodedata
from calculate_anything.utils import Singleton, multi_re, safe_operation
from calculate_anything.constants import MAIN_DIR
from calculate_anything import logging


logger = logging.getLogger(__name__)


class LanguageService(metaclass=Singleton):
    '''A language service class which acts like a Singleton.

    Attributes:
        lang (str): The language currently in use
    '''

    def __init__(self):
        self._lang = None
        self._data = {}
        self._update_callbacks = []

    @property
    def lang(self) -> str:
        return self._lang

    @staticmethod
    def strip_accents(s: str) -> str:
        '''Strips all accents from a string.

        Args:
            s (str): The string to strip accents from.

        Returns:
            str: A string with accents stripped.
        '''
        return ''.join(
            c
            for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
        )

    def set(self, lang: str) -> None:
        '''Sets the language to be used and loads the corresponding
            json file located at data/lang.

        Args:
            lang (str): The name of the language (file) to use and load
                without the '.json' extension.
        '''
        if lang == self._lang:
            return
        fallback = False
        lang_filepath = os.path.join(
            MAIN_DIR, 'data', 'lang', '{}.json'.format(lang)
        )
        if not os.path.exists(lang_filepath):
            logger.error(
                'Language file does not exist: {}'.format(lang_filepath)
            )
            fallback = True
        if not fallback:
            try:
                with open(lang_filepath, 'r', encoding='utf-8') as f:
                    self._data = json.loads(f.read())
            except Exception as e:  # pragma: no cover
                msg = 'Could not load language, falling back to en_US: {}: {}'
                msg = msg.format(lang_filepath, e)
                logger.exception(msg)
                fallback = True

        if fallback:
            if lang == 'en_US':  # pragma: no cover
                logger.error(  # pragma: no cover
                    'en_US does not exist, will not use any language '
                    'aliases: {}'.format(lang_filepath)
                )
                return  # pragma: no cover
            self.set('en_US')
            return

        self._lang = lang
        for callback in self._update_callbacks:
            with safe_operation():
                callback(lang)

    def translate(self, word: str, mode: str) -> str:
        '''Translates a word/key with the provided mode. If the word is not
        found in the translations it is returned intact.

        Args:
            word (str): A word/key to translate.
            mode (str): A mode to use form the language file
                (i.e the dict key).
        '''
        word = str(word)
        return self._data.get(mode, {}).get(word, word)

    def get_translator(self, mode: str) -> Callable[[str], str]:
        '''Get a translator function with the provided mode.

        Args:
            mode (str): A mode to use form the language file
                (i.e the dict key).

        Returns:
            callable: A translator callable which takes as input a word (str)
                and returns the translated word (str) if there is any or the
                word itself.
        '''

        def _translator(word):
            return self.translate(word, mode)

        return _translator

    def add_translation(
        self, word: str, translated_word: str, mode: str
    ) -> None:
        '''Adds a word/key to the translations in runtime (only kept in memory).

        Args:
            word (str): A word/key to translate.
            translated_word (str): The translation of the word.
            mode (str): A mode to use (i.e the dict key).
        '''
        if mode not in self._data:
            self._data[mode] = {}
        self._data[mode][word] = translated_word

    def translation_adder(self, mode: str) -> Callable[[str, str], None]:
        '''Get a translator adder function with the provided mode.

        Args:
            mode (str): A mode to use (i.e the dict key).

        Returns:
            callable: A translator adder callable which takes as input a word
            str and its translation str and puts it in the translations data to
            be used later.
        '''

        def _translation_adder(word, translated_word):
            self.add_translation(word, translated_word, mode)

        return _translation_adder

    def replace_all(
        self, string: str, mode: str, ignorecase: bool = True
    ) -> str:
        '''Replaces all substrings in the provided string with the translated
        ones if any.

        Args:
            string (str): A string to replace all substrings with translations.
            mode (str): A mode to use form the language file
                (i.e the dict key).
            ignorecase (bool, default True): ignore case when replacing.

        Returns:
            str: The provided str with all substrings replaced with
                translations (if any).
        '''
        if mode not in self._data:
            return string

        return multi_re.sub_dict(
            self._data[mode],
            string,
            sort=True,
            flags=re.IGNORECASE if ignorecase else 0,
        )

    def get_replacer(
        self, mode: str, ignorecase: bool = True
    ) -> Callable[[str], str]:
        '''Get a translator replacer function with the provided mode.

        Args:
            mode (str): A mode to use (i.e the dict key).

        Returns:
            callable: A translator replacer callable which takes as input a
                string  and replaces any substring with the corresponding
                translation.
        '''

        def _replacer(string):
            return self.replace_all(string, mode, ignorecase)

        return _replacer

    def add_update_callback(self, callback: Callable[[str], None]) -> None:
        '''Adds an update callback to call when language is changed.

        Args:
            callback (callable): A callable which takes as input a str
                (the language changed).
        '''
        self._update_callbacks.append(callback)
