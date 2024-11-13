from playwright.sync_api import Page, expect

from tests.utils.constants import BASE_URL


def test_homepage_title(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title('Credit Association')
    expect(page).to_have_url(BASE_URL)


def test_homepage_header(page: Page):
    page.goto(BASE_URL)
    header = page.locator('h4')
    expect(header).to_be_visible()
    expect(header).to_contain_text('Register to become a member')


def test_homepage_copyright(page: Page):
    page.goto(BASE_URL)
    copyright = page.get_by_test_id('copyright')
    expect(copyright).to_contain_text('© 2024')
