from framework.driverfactory.chrome_driver import ChromeDriver

from framework.driverfactory.firefox_driver import FirefoxDriver


class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser == 'Chrome':
            return ChromeDriver().driver
        elif browser == 'Firefox':
            return FirefoxDriver().driver
