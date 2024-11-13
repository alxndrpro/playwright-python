from playwright.sync_api import Page, BrowserType, Expect

from tests.utils.constants import BASE_URL

def test_filtering(page: Page, expect: Expect):
    page.goto(f'{BASE_URL}savings.html')

    rows = page.get_by_role('row')
    print(rows.count())

    row = page.get_by_role('row').filter(has_text='Competition')
    print(row.text_content())


    cell = row = page.get_by_role('row').filter(has_text='Competition').get_by_role('cell').nth(1)
    print(cell.text_content())