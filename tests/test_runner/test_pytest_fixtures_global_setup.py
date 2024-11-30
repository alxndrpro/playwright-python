from playwright.sync_api import Page, expect
import pytest, requests

from tests.utils.constants import BASE_URL

@pytest.fixture(scope='module')
def once_per_module(page: Page):
    print('Run once for all tests')
    name = requests.get('https://api.github.com/users/alxndrpro').json().get('name')
    page.goto(BASE_URL)

    yield name

    # do cleanup


@pytest.fixture
def page(page: Page):
    name = requests.get('https://api.github.com/users/alxndrpro').json().get('name')
    page.goto(BASE_URL)

    yield page

    # do cleanup


def test_one(page: Page, once_per_module):
    name_input = page.get_by_label('First name')
    name_input.fill('')
    expect(name_input).to_have_value('')

    print(f'Test 1: ${once_per_module}')


def test_two(page: Page, once_per_module):
    name_input = page.get_by_label('First name')
    name_input.fill('')
    expect(name_input).to_have_value('')

    print(f'Test 2: ${once_per_module}')
