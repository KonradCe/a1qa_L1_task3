import pytest

from framework.driver_utils import SingletonWebDriver
import framework.utils.config_data as config_utils


@pytest.fixture()
def driver_setup_teardown():
    browser_of_choice = config_utils.get_browser_of_choice()
    driver = SingletonWebDriver().get_driver(browser_of_choice)
    driver.get("https://store.steampowered.com/")
    yield driver
    driver.quit()
    SingletonWebDriver().unassign_driver()
