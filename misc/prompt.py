#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

if os.getcwd() not in sys.path:
    sys.path.append(os.getcwd())
from calculate_anything.currency import CurrencyService
from calculate_anything.query.handlers import (
    TimeQueryHandler,
    Base10QueryHandler,
    Base16QueryHandler,
    Base2QueryHandler,
    Base8QueryHandler,
    UnitsQueryHandler,
    CalculatorQueryHandler,
    PercentagesQueryHandler,
)
from calculate_anything.query.handlers import MultiHandler
from calculate_anything.lang import LanguageService
from calculate_anything import logging
from calculate_anything.preferences import Preferences
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.validation import Validator
from prompt_toolkit.patch_stdout import patch_stdout
from prompt_toolkit import HTML, PromptSession
from prompt_toolkit.styles import Style


# Setup Calculate Anything (Order is important)
# Comment this line to get log messages (use patch stdout in such case)
logging.disable_file_handler()
logging.disable_stdout_handler()

# Set the language
preferences = Preferences()
preferences.language.set('en_US')

# Set some default currencies
preferences.currency.set_default_currencies(['USD', 'EUR', 'CAD', 'BTC'])

# Enable currency service and cache and run every day
preferences.currency.enable_cache(60 * 60 * 24)

# Set default cities for timezone conversion
preferences.time.set_default_cities('London GB,Athens GR,Tokyo JP')

preferences.commit()
# End setup

# Define keywords, change dictionary keys to whatever you want
keywords = {
    'time': {
        'kw': 'time',  # Calculate anything's internal keyword
        'mode': 'time',
        'mode_description': 'Time Converter',
        'handlers': [TimeQueryHandler],
    },
    'dec': {
        'kw': 'dec',  # Calculate anything's internal keyword
        'mode': 'dec',
        'mode_description': 'Decimal Calculator',
        'handlers': [Base10QueryHandler],
    },
    'hex': {
        'kw': 'hex',  # Calculate anything's internal keyword
        'mode': 'hex',
        'mode_description': 'Hex Calculator',
        'handlers': [Base16QueryHandler],
    },
    'bin': {
        'kw': 'bin',  # Calculate anything's internal keyword
        'mode': 'bin',
        'mode_description': 'Binary Calculator',
        'handlers': [Base2QueryHandler],
    },
    'oct': {
        'kw': 'oct',  # Calculate anything's internal keyword
        'mode': 'oct',
        'mode_description': 'Octal Calculator',
        'handlers': [Base8QueryHandler],
    },
    '=': {
        'kw': '=',  # Calculate anything's internal keyword
        'mode': 'calculator',
        'mode_description': 'Calculator and Unit converter',
        'handlers': [
            CalculatorQueryHandler,
            PercentagesQueryHandler,
            UnitsQueryHandler,
        ],
    },
}

style = Style.from_dict(
    {
        'bottom-toolbar': 'fg:#282a36 bg:#f8f8f2 reverse',
    }
)


bindings = KeyBindings()


class Program(Validator):
    """Some simple prompt_toolkit code to make this run"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reset()

    def reset(self):
        self._kw = ''
        self._query = ''
        self._results = ''

    def _process_results(self, results):
        pad = ' ' * 400
        results_strs = []
        str_fmt = (
            '<b><style bg="#22242e" fg="#7d4bc4">❯  {}{}</style></b>\n'
            '<style bg="#d1d1d1" >   ⮞ {}</style>'
        )
        for result in results:
            results_strs.append(
                str_fmt.format(result.name, pad, result.description)
            )
        return '\n'.join(results_strs)

    def validate(self, document):
        text = document.text
        self._kw = text.strip().split(' ', 1)[0]
        self._query = text[len(self._kw) :]
        if self._kw in keywords and self._query != '':
            handlers = keywords[self._kw]['handlers']
            results = MultiHandler().handle(self._kw + self._query, *handlers)
            self._results = self._process_results(results)
        else:
            self._results = ''

    def handle_c_a(self, event):
        pos = event.current_buffer.cursor_position
        while event.current_buffer.cursor_position > 0:
            event.current_buffer.cursor_left()

        event.current_buffer.start_selection()
        while event.current_buffer.cursor_position < pos:
            event.current_buffer.cursor_right()

    def rprompt(self):
        key = self._kw
        if key not in keywords:
            mode = 'No mode selected'
        else:
            mode = keywords[key]['mode_description']
        return HTML(
            '<style bg="#ff5555" fg="#282a36"> {} </style>'.format(mode)
        )

    def bottom_toolbar(self):
        if self._kw not in keywords:
            keystr = ', '.join(map('"{}"'.format, keywords))
            # tb_str = '<style fg="ansiblue">{}</style>'
            tb_str = '  Use one of the keywords followed by space\n  - [{}]'
            tb_str = tb_str.format(keystr)
            return [('class:bottom-toolbar', tb_str)]

        results = self._results
        if self._query.strip() == '' and not self._results:
            results = '  {} \n  {}'.format(
                LanguageService().translate('no-result', 'misc'),
                LanguageService().translate(
                    'no-result-{}-description'.format(
                        keywords[self._kw]['mode']
                    ),
                    'misc',
                ),
            )
        elif not self._results:
            results = '\n'
        return HTML(results)


# Some hacks when creating demos, don't put this in your code
if os.environ.get('RECORD', '').lower() == 'true':
    sys.stdin = open('/dev/tty', 'r')

program = Program()
bindings.add('c-a')(program.handle_c_a)
session = PromptSession(
    key_bindings=bindings,
    rprompt=program.rprompt,
    bottom_toolbar=program.bottom_toolbar,
    validator=program,
    validate_while_typing=True,
    wrap_lines=True,
    # refresh_interval=0.01,
    style=style,
)

try:
    with patch_stdout():
        while True:
            session.prompt('❯ ')
            program.reset()
except KeyboardInterrupt as e:
    print(e)
finally:
    CurrencyService().stop()
