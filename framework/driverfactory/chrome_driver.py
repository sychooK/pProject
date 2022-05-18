from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


class ChromeDriver:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not ChromeDriver.__instance:
            ChromeDriver.__instance = object.__new__(cls)
        return ChromeDriver.__instance

    def __init__(self):
        self.options = chrome_options()
        self.options.add_argument('chrome')
        self.options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(executable_path='C:\\driver\\chromedriver.exe', options=self.options)
