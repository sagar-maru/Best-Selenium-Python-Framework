from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from utils.config import read_config
from utils.chrome_driver import setup_chrome_driver


def get_chrome_driver(headless=False):
    chrome_driver_path = setup_chrome_driver()
    chrome_options = ChromeOptions()
    if headless:
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=ChromeService(chrome_driver_path), options=chrome_options)
    return driver


def get_firefox_driver(headless=False):
    firefox_options = FirefoxOptions()
    if headless:
        firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    return driver


def get_driver():
    config = read_config()
    browser_name = config.get('browser', 'chrome')
    headless = config.getboolean('headless', False)

    if browser_name.lower() == "firefox":
        return get_firefox_driver(headless)
    return get_chrome_driver(headless)
