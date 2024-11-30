from playwright.sync_api import Page, expect
import pytest

from tests.utils.constants import BASE_URL

@pytest.fixture
def page(start_page: Page):
    page.goto(BASE_URL)
    yield page
    print('\nCleanup')


def test_single_param(start_page: Page):
    name_input = start_page.get_by_label('First name')
    name_input.fill('Sofia')
    expect(name_input).to_have_value('Sofia')

@pytest.mark.parametrize('name', ['Alex',
                                  'Sofia',
                                  'Steve'])
def test_two_params(start_page: Page, name: str):
    name_input = start_page.get_by_label('First name')
    name_input.fill(name)
    expect(name_input).to_have_value(name)