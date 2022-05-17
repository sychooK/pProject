from framework.driverfactory.chrome_driver import ChromeDriver

from framework.driverfactory.firefox_driver import FirefoxDriver


class DriverFactory:

    def __init__(self):
        super

    @staticmethod
    def get_driver(browser):
        if browser == 'Chrome':
            return ChromeDriver()
        elif browser == 'Firefox':
            return FirefoxDriver()
