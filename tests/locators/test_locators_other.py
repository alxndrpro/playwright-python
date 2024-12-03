from playwright.sync_api import Page, expect

from tests.utils.constants import BASE_URL


def test_multiple_matches_fail(page: Page):

    page.goto(BASE_URL)
    page.check('#heard-about')
    page.fill('#textarea', 'So I was thinking the other day ...')

