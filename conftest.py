import pytest
from selene import browser, be, have

@pytest.fixture(scope="session")
def browser_config():
    browser.config.window_height = 2500
    browser.config.window_width = 1400
    yield
    browser.quit()