from playwright.sync_api import Page, BrowserType, Expect

from tests.utils.constants import BASE_URL


def test_headless_and_slow_mo(browser_type:BrowserType):
    page = browser_type.launch(headless=False,slow_mo=1000)

def test_recommended_locators(page: Page, expect: Expect):
    page.goto(BASE_URL)

    first_name = page.get_by_label('First name')
    first_name.fill('Sofia')
    first_name.clear()

    page.get_by_role('button', name='Register', exact=True).click()

    warning = page.get_by_text('Valid last name is required')
    expect(warning).to_be_visible()