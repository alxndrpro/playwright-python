from playwright.sync_api import Page, expect

from tests.utils.constants import BASE_URL

name = 'Sofia'


def test_dialog_default_handling(page: Page):
    page.goto(BASE_URL)

    name_input = page.get_by_label('First name')
    name_input.fill(name)
    expect(name_input).to_have_value(name)

    page.get_by_role('button', name='Clear').click()
    expect(name_input).to_have_value(name)


def test_dialog_ok_or_dismiss(page: Page):
    page.on('dialog', lambda popup: popup.accept())
    # page.once('dialog', lambda popup: popup.accept())

    page.goto(BASE_URL)

    name_input = page.get_by_label('First name')
    name_input.fill(name)

    page.get_by_role('button', name='Clear').click()
    expect(name_input).to_have_value('')
