from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from task3.framework.utils.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils.wait_utils import WaitUtils


class BaseElement:
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def _get_element(self) -> WebElement:
        return Swd.get_driver().find_element(*self.locator)

    def click(self):
        self._get_element().click()

    def move_cursor_to(self):
        pass

    def is_displayed(self) -> bool:
        return self._get_element().is_displayed()

    def is_exists(self) -> bool:
        return bool(Swd.get_driver().find_elements(*self.locator))

    def wait_for_element(self):
        return WaitUtils.wait_for_element_to_be_present_and_visible(self.locator)

    def is_gone(self, wait=False):
        if wait:
            try:
                WaitUtils.wait_for_element_to_be_gone(self.locator)
            except TimeoutException:
                return False
        try:
            self._get_element()
            return False
        except NoSuchElementException:
            return True

    def get_attribute(self, attribute_name):
        return self._get_element().get_attribute(attribute_name)
