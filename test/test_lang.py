from queue import Queue
from calculate_anything.lang import LanguageService
from test.tutils import reset_instance, extra_translations


def test_main():
    translations = {'some': 'some2'}
    translations_add = {'other': 'other2'}
    with reset_instance(LanguageService):
        LanguageService().set('en_US')
        LanguageService().set('en_US')
        LanguageService().set('invalidLanguage')
        assert LanguageService().lang == 'en_US'

        string = 'άέίόήύΆΈΊΌΉΎ'
        stripped = LanguageService.strip_accents(string)
        assert stripped == 'αειοηυΑΕΙΟΗΥ'
        with extra_translations('testing1', translations):
            tr_adder = LanguageService().translation_adder('testing2')
            for k, v in translations_add.items():
                tr_adder(k, v)

            translator1 = LanguageService().get_translator('testing1')
            assert translator1('some') == 'some2'

            translator2 = LanguageService().get_translator('testing2')
            assert translator2('other') == 'other2'

            replacer1 = LanguageService().get_replacer('testing1', False)
            assert replacer1('Some other') == 'Some other'
            assert replacer1('some other') == 'some2 other'

            replacer2 = LanguageService().get_replacer('testing2', True)
            assert replacer2('some Other') == 'some other2'
            assert replacer2('some other') == 'some other2'

            replacer_extra = LanguageService().get_replacer('invalidmode')
            assert replacer_extra('abcdefg') == 'abcdefg'


def test_callback():
    def callback(lang):
        queue.put_nowait(lang)

    queue = Queue()
    with reset_instance(LanguageService):
        LanguageService().add_update_callback(callback)
        LanguageService().set('en_US')
        assert queue.get_nowait() == 'en_US'
