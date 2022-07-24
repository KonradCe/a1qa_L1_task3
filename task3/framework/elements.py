from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from task3.framework.driver_utils import SingletonWebDriver as Swd


# TODO: make abstract
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


class ButtonElement(BaseElement):
    def get_text(self):
        btn_element = super()._get_element()
        print(btn_element.text)


class BasicElement(BaseElement):
    pass


class SubMenu(BaseElement):
    def click_on_button_with_text(self, btn_string):
        super()._get_element().find_element(
            By.XPATH, f"//span[contains(text(), '{btn_string}')]"
        ).click()
