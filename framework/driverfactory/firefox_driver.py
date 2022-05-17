from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options


class FirefoxDriver:

    def __init__(self):
        options = firefox_options()
        self.driver = webdriver.Firefox(executable_path='C:\\driver\\geckodriver.exe', options=options)
