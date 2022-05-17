import pytest

from framework.driverfactory.driver_factory import DriverFactory


@pytest.fixture(scope='function')
def setup(request):
    driver = DriverFactory.get_driver(browser='Firefox').driver
    url = 'https://demoqa.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
