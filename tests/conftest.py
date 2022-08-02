import pytest

from task3.framework.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils import config_data_utils
from task3.framework.utils import logger_utils


@pytest.fixture()
def driver_setup_teardown():
    browser_of_choice = config_data_utils.get_browser_of_choice()
    logger_utils.log_info(f"browser of choice: {browser_of_choice}")
    Swd.get_driver(browser_of_choice)
    logger_utils.log_info("driver setup finished")
    yield
    Swd.driver_quit()
    Swd.unassign_driver()
    logger_utils.log_info("driver teardown finished")


@pytest.fixture(scope="session", autouse=True)
def logger_setup():
    logger_utils.logger_setup()
    logger_utils.log_info("logger setup finished")
