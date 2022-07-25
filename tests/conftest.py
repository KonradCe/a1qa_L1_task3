import pytest

import task3.framework.driver_utils as driver_utils
import task3.framework.utils.config_data_utils as config_utils
import task3.framework.utils.logger_utils
from task3.framework.driver_utils import SingletonWebDriver as Swd


@pytest.fixture()
def driver_setup_teardown():
    browser_of_choice = config_utils.get_browser_of_choice()
    Swd.get_driver(browser_of_choice)
    yield
    driver_utils.driver_quit()
    driver_utils.unassing_driver()


@pytest.fixture(scope="session", autouse=True)
def logger_setup():
    task3.framework.utils.logger_utils.logger_setup()
