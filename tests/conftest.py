import pytest
from selene.support.shared import browser


@pytest.fixture()
def browser_config():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.hold_browser_open = True


