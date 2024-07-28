from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, 'q')

    def open(self):
        self.driver.get('https://www.google.com')

    def search(self, query):
        self.driver.find_element(*self.search_box).send_keys(query + Keys.RETURN)
