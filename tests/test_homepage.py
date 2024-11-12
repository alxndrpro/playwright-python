from playwright.sync_api import Page


def test_homepage_title(page: Page):
        page.goto('http://localhost:8000/')


def test_homepage_header(page: Page):
        page.goto('http://localhost:8000/')