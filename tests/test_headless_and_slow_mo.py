from playwright.sync_api import Page, BrowserType

from tests.utils.constants import BASE_URL


def test_headless_and_slow_mo(browser_type:BrowserType):
    page = browser_type.launch(headless=False,slow_mo=1000)

def test_recommended_locators(page: Page):
    page.goto(BASE_URL)