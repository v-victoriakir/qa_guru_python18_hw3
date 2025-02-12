import pytest
from selene import browser


@pytest.fixture
def browser_config():
    browser.config.window_height = 2500
    browser.config.window_width = 1400


@pytest.fixture
def browser_actions(browser_config):
    browser.open('https://duckduckgo.com')
    yield
    browser.quit()
