from playwright.sync_api import Page, expect, StorageState

from tests.utils.constants import BASE_URL

name = "Sofia"


def test_storage_ui_perspective(page: Page):
    page.goto(BASE_URL)

    name_input = page.get_by_label('First name')
    name_input.fill(name)
    page.reload()
    expect(name_input).to_have_value('')

    name_input.fill(name)
    page.get_by_role('button', name='Save Input').click()
    page.reload()
    expect(name_input).to_have_value(name)


def test_local_storage(page: Page):
    page.goto(BASE_URL)
    page.get_by_label('First name').fill(name)
    page.get_by_role('button', name='Save Input').click()

    storage: StorageState = page.context.storage_state()

    print('')
    print(storage['cookies'])
    print(storage['origins'][0]['localStorage'])
