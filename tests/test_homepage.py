import pytest

from framework.driverfactory.driver_factory import DriverFactory


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_homepage(self):
        driver = DriverFactory.get_driver("Chrome")
        driver1 = DriverFactory.get_driver("Chrome")
        print(driver)
        print(driver1)
