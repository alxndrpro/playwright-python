from playwright.sync_api import sync_playwright


def test_browser_type():
    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = browser_type.launch()
            page = browser.new_page()
            page.goto('http://www.whatismybrowser.com/')
            # page.screenshot(path=f'example-{browser_type.name}.png')
            browser.close()
