from playwright.sync_api import Page, expect

from tests.utils.constants import BASE_URL

def test_codegen_demo(page: Page):
    page.goto(BASE_URL)
    page.get_by_label("First name").click()
    page.get_by_label("First name").fill("John")
    page.get_by_label("Last name").click()
    page.get_by_label("Last name").fill("Smith")
    page.get_by_placeholder("you@example.com").click()
    page.get_by_placeholder("you@example.com").fill("john@gmail.com")
    page.get_by_label("Date of birth (optional)").fill("1992-11-11")
    page.get_by_role("button", name="Save input").click()
