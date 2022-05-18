from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options


class FirefoxDriver:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not FirefoxDriver.__instance:
            FirefoxDriver.__instance = object.__new__(cls)
        return FirefoxDriver.__instance

    def __init__(self):
        self.options = firefox_options()
        self.driver = webdriver.Firefox(executable_path='C:\\driver\\geckodriver.exe', options=self.options)
