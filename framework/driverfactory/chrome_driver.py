from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


class ChromeDriver:

    def __init__(self):
        options = chrome_options()
        options.add_argument('chrome')
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(executable_path='C:\\driver\\chromedriver.exe', options=options)
