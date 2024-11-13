from playwright.sync_api import Page, BrowserType, Expect

from tests.utils.constants import BASE_URL

def test_generic_locators(page: Page, expect: Expect):
    page.goto(BASE_URL)

    page.locator('.needs-validation label[for="firstName"]').fill("Tom")
    page.locator('//form//button[2]').click()

    expect(page.get_by_text('Valid last name is required')).to_be_visible()