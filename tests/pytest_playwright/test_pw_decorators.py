import pytest
from playwright.sync_api import Page, Browser

args: dict = {'locale': 'es_ES', 'timezone_id': "Europe/Madrid"}  # move to reuse


class TestThing:

    @pytest.mark.skip_browser('firefox')
    def test_one(self, page: Page):
        pass

    @pytest.mark.only_browser('firefox')
    def test_two(self, page: Page):
        pass

    @pytest.mark.browser_context_args(**args)
    def test_three(self, page: Page, browser: Browser):
        browser.new_context(**args)
        assert page.evaluate("Intl.DateTimeFormat().resolvedOptions().timeZone()") == "Europe/Madrid"
        assert page.evaluate("window.navigator.languages") == ["es-ES"]

    @pytest.mark.parametrize('arg1', ['val1',
                                      'val2'])
    @pytest.mark.browser_context_args(**args)
    @pytest.marker.smoke
    def test_four(self, page: Page): # Will run twice
        assert page.evaluate("Intl.DateTimeFormat().resolvedOptions().timeZone()") == "Europe/Madrid"
        assert page.evaluate("window.navigator.languages") == ["es-ES"]
