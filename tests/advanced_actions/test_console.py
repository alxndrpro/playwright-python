from playwright.sync_api import Page, expect

from tests.utils.constants import BASE_URL

def test_check_console(page: Page):

    page.on('console', lambda msg: print(msg.text()))

    #Listener for uncaught exceptions.
    page.on('pageerror', lambda msg: print(msg.text()))

    print('')

    page.goto(BASE_URL)

    page.get_by_role('button', name='Register').click()

