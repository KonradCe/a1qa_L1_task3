import selenium.webdriver.common.alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from task3.framework.utils.config_data_utils import ConfigUtils
from task3.framework.utils.driver_utils import SingletonWebDriver as Swd


class WaitUtils:
    @staticmethod
    def __get_standard_wait():
        return WebDriverWait(Swd.get_driver(), ConfigUtils.get_explicit_wait_time())

    @classmethod
    def wait_for_alert(cls) -> selenium.webdriver.common.alert.Alert:
        wait = cls.__get_standard_wait()
        alert = wait.until(EC.alert_is_present())
        return alert

    @classmethod
    def wait_for_element_to_be_present_and_visible(cls, locator):
        wait = cls.__get_standard_wait()
        element = wait.until(EC.visibility_of_element_located(locator))
        return element

    @classmethod
    def wait_for_element_to_be_gone(cls, locator):
        wait = cls.__get_standard_wait()
        wait.until(EC.invisibility_of_element(locator))

    @classmethod
    def wait_for_element_to_be_clickable(cls, button):
        wait = cls.__get_standard_wait()
        wait.until(EC.element_to_be_clickable(button))

    @classmethod
    def wait_for_new_window_to_open(cls, current_handles):
        wait = cls.__get_standard_wait()
        wait.until(EC.new_window_is_opened(current_handles))

    @classmethod
    def text_in_attribute(cls, locator, attribute, text):
        wait = WebDriverWait(Swd.get_driver(), timeout=15, poll_frequency=0.05)
        wait.until(EC.text_to_be_present_in_element_attribute(locator, attribute, text))
