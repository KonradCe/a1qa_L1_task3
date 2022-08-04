import pytest

from task3.framework.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils.config_data_utils import ConfigUtils
from task3.framework.utils.logger_utils import LoggerUtils


@pytest.fixture()
def driver_setup_teardown():
    browser_of_choice = ConfigUtils.get_browser_of_choice()
    LoggerUtils.log_info(f"browser of choice: {browser_of_choice}")
    Swd.get_driver(browser_of_choice)
    LoggerUtils.log_info("driver setup finished")
    yield
    Swd.driver_quit()
    Swd.unassign_driver()
    LoggerUtils.log_info("driver teardown finished")


@pytest.fixture(scope="session", autouse=True)
def logger_setup():
    LoggerUtils.logger_setup()
    LoggerUtils.log_info("logger setup finished")
