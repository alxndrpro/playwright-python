from playwright.sync_api import Page, expect


# pytest .\test_plugin_example.py -- headed --browser webkit --browser firefox --slowmo 300 --screenshot only-on-failure --base-url http://localhost:8000/

def test_simple_plugin_example(page: Page):
    page.goto('')

    page.get_by_label('First name').fill('Sofi')
    page.get_by_role('button', name='Register', exact=True).click()

    warning = page.get_by_text('Valid last name is required')
    expect(warning).not_to_be_visible()