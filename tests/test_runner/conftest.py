import pytest


@pytest.fixture(scope='session', autouse=True)
def global_setup_available_everywhere():
    print('Global setup for entire test run of ALL applicable tests')