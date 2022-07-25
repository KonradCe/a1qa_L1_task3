from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from task3.framework.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils import wait_utils


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


class BasicElementWithText(BasicElement):
    def get_text(self):
        btn_element = super()._get_element()
        print(btn_element.text)
        return btn_element.text


class SubMenu(BaseElement):
    def click_on_button_with_text(self, btn_string):
        super()._get_element().find_element(
            By.XPATH, f"//span[contains(text(), '{btn_string}')]"
        ).click()


class Alert:
    def __get_alert(self):
        return wait_utils.wait_for_alert()

    def accept(self):
        self.__get_alert().accept()

    def dismiss(self):
        self.__get_alert().dismiss()

    def send_input(self, message):
        self.__get_alert().send_keys(message)

    def get_text(self):
        return self.__get_alert().text

    def is_alert_present(self):
        try:
            Swd.get_driver().switch_to.alert
            return True
        except NoAlertPresentException:
            return False


class Iframe(BaseElement):
    def switch_into(self):
        iframe = self._get_element()
        Swd.get_driver().switch_to.frame(iframe)
        return iframe

    def switch_out_of(self):
        Swd.get_driver().switch_to.default_content()

    def get_text(self):
        self.switch_into()
        iframe_text = Swd.get_driver().find_element(By.XPATH, "//body").text
        self.switch_out_of()
        return iframe_text

    def get_text_from_nested_iframe(self):
        self.switch_into()
        nested_iframe = Iframe((By.XPATH, "//iframe"), "nested iframe")
        text_from_nested_iframe = nested_iframe.get_text()
        self.switch_out_of()
        return text_from_nested_iframe
