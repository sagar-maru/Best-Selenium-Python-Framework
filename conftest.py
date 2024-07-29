import pytest
from utils.browser import get_driver


@pytest.fixture(scope="session")
def driver():
    driver = get_driver()
    driver.maximize_window()
    yield driver
    driver.quit()