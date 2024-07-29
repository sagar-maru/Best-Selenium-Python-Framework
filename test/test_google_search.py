import os
import pytest
from selenium import webdriver

from utils.browser import get_driver
from pages.google_page import GooglePage
from utils.excel_utils import read_excel
from pathlib import Path
import allure

project_root = Path(__file__).parent.parent.resolve()

# Commented the below function As Added the below code in conftest.py file
# Added in in conftest.py file with @pytest.fixture(scope='session')
# @pytest.fixture(scope='module')
# def driver():
#     driver = get_driver()
#     driver.maximize_window()
#     yield driver
#     driver.quit()

def take_screenshot(driver, name):
    screenshot_path = os.path.join(os.path.join(project_root,'screenshots'),f'{name}.png')
    driver.save_screenshot(screenshot_path)
    # Uncomment the below line if you want the attach screenshot with allure report
    # allure.attach.file(screenshot_path, attachment_type=allure.attachment_type.PNG)

def test_google_search(driver):
    data = read_excel(os.path.join(os.path.join(project_root,'resources'),'data.xlsx'), 'Sheet1')
    search_query = data['Search Query'][0]
    google_page = GooglePage(driver)

    ## Open the Google Page in the Browser
    google_page.open()
    take_screenshot(driver, 'google_home')

    ## Search Query in Google
    google_page.search(search_query)
    driver.implicitly_wait(5)
    take_screenshot(driver, 'search_results')
    assert 'sagar-maru github' in driver.title
