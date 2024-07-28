import pytest
from selenium import webdriver
from utils.driver import get_driver
from pages.google_page import GooglePage
from utils.excel_utils import read_excel
import allure

@pytest.fixture(scope='module')
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def take_screenshot(driver, name):
    screenshot_path = f'screenshots/{name}.png'
    driver.save_screenshot(screenshot_path)

    # Uncomment the below line if you want the attach screenshot with allure report
    # allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG)

def test_google_search(driver):
    data = read_excel('../resources/data.xlsx', 'Sheet1')
    search_query = data['Search Query'][0]
    print(search_query)
    google_page = GooglePage(driver)
    google_page.open()
    take_screenshot(driver, 'google_home')
    google_page.search(search_query)
    take_screenshot(driver, 'search_results')
    assert 'sagar-maru github' in driver.title
