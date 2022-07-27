import selenium.webdriver.common.alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from task3.framework.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils.config_data_utils import get_explicit_wait_time


def __get_standard_wait():
    return WebDriverWait(Swd.get_driver(), get_explicit_wait_time())


def wait_for_alert() -> selenium.webdriver.common.alert.Alert:
    wait = __get_standard_wait()
    alert = wait.until(EC.alert_is_present())
    return alert


def wait_for_element_to_be_present_and_visible(locator):
    wait = __get_standard_wait()
    element = wait.until(EC.visibility_of_element_located(locator))
    return element


def wait_for_element_to_be_gone(locator):
    wait = __get_standard_wait()
    wait.until(EC.invisibility_of_element(locator))


def wait_for_element_to_be_clickable(button):
    wait = __get_standard_wait()
    wait.until(EC.element_to_be_clickable(button))


def wait_for_new_window_to_open(current_hanldes):
    wait = __get_standard_wait()
    wait.until(EC.new_window_is_opened(current_hanldes))
