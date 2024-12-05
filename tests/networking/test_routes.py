from playwright.sync_api import Page, expect, Browser

from tests.utils.constants import BASE_URL


def disable_js(browser: Browser):
    browser.new_context(java_script_enabled=False)


def test_route_report(page: Page):
    page.route('**/*.js', lambda route: route.abort())

    page.goto(f'{BASE_URL}savings.html')
    page.get_by_test_id('deposit').fill('10')
    expect(page.get_by_test_id('result')).not_to_be_visible()


def test_route_with_condition(page: Page):
    page.route('**/*', lambda route: route.abort()
    if route.request.resource_type == 'script' else route.continue_())


def test_route_fulfill(page: Page):
    page.route('*/**.pdf', lambda route: route.fulfill(
        status=404,
        contentType='text/plain',
        body='Not Found'
    ))

    page.goto(f'{BASE_URL}saving.html')

    page.get_by_text('Download Our Offer').click()

    page.screenshot(path='route.png')
    page.wait_for_url('**/*.pdf')

    body = page.locator('body')
    expect(body).to_contain_text('Not Found')
