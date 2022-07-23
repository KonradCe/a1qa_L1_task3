import pytest

import task3.framework.utils.config_data_utils as config_utils
from task3.framework.driver_utils import SingletonWebDriver


@pytest.fixture()
def driver_setup_teardown():
    browser_of_choice = config_utils.get_browser_of_choice()
    driver = SingletonWebDriver().get_driver(browser_of_choice)
    yield driver
    driver.quit()
    SingletonWebDriver().unassign_driver()
