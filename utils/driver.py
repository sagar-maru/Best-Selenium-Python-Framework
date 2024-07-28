import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.config import BROWSER, HEADLESS

def get_driver():
    if BROWSER == 'chrome':
        options = webdriver.ChromeOptions()
        if HEADLESS:
            options.add_argument('--headless')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif BROWSER == 'firefox':
        options = webdriver.FirefoxOptions()
        if HEADLESS:
            options.add_argument('--headless')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        raise ValueError("Unsupported browser!")
    return driver
