from playwright.sync_api import Page, expect
import pytest

from tests.utils.constants import BASE_URL



@pytest.mark.parametrize('name', ['Alex',
                                  'Sofia',
                                  'Steve'])
def test_single_param(page: Page, name: str):
    page.goto(BASE_URL)

    name_input = page.get_by_label('First name')
    name_input.fill(name)
    expect(name_input).to_have_value(name)


@pytest.mark.parametrize('name, last_name', [('Alex', 'Smith'),
                                             ('Sofia', 'Adams'),
                                             ('John', 'Dow')
                                             ])
def test_two_params(page: Page, name: str, last_name: str):
    page.goto(BASE_URL)

    name_input = page.get_by_label('First name')
    name_input.fill(name)
    expect(name_input).to_have_value(name)

    name_input = page.get_by_label('Last name')
    name_input.fill(last_name)
    expect(name_input).to_have_value(last_name)
