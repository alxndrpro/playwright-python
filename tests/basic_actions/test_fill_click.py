from playwright.sync_api import Page, expect

from tests.utils.constants import BASE_URL


def test_fill(page: Page):
    page.goto(BASE_URL)

    page.get_by_label('First name').fill('Alex')

    page.get_by_label('Date of birth').fill('2024-11-11')



