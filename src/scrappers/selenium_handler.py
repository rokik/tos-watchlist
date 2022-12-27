from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SeleniumHandler:

    def __init__(self):
        self.options = Options()
        self.driver = webdriver.Chrome(options=self.options)

    @property
    def get_webdriver(self):
        return self.driver

    def close(self):
        self.get_webdriver.close()
