from pprint import pprint
from time import sleep

from playwright.sync_api import Playwright


def test_geolocation(playwright: Playwright):
    ipad: dict = playwright.devices['iPad Pro 11']
    pprint(playwright.devices)

    ctx = playwright.chromium.launch(headless=False, slow_mo=1000).new_context(
        **ipad,
        locale='en_GB',
        geolocation={"longitude": -0.118092, "latitude": 51.509865},  # London
        permissions=["geolocation"],
        base_url='https://maps.google.com'
    )

    page = ctx.new_page()
    page.goto('')
    page.get_by_role('button', name='Accept all').click()
    page.get_by_role('button', name='Stay on web').click()
    sleep(2)
