from playwright.sync_api import sync_playwright


def test_homepage_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://localhost:8000/')
        browser.close()


def test_homepage_header():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://localhost:8000/')
        browser.close()
