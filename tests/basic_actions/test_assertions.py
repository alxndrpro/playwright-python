from playwright.sync_api import Page, expect

from tests.utils.constants import BASE_URL


def assertions_cheatsheet(page: Page):
    page.goto(BASE_URL)

    textarea = page.locator('#textarea')
    expect(textarea).to_have_value('')


