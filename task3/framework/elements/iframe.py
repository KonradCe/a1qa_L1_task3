from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from task3.framework.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils.logger_utils import log_debug, log_info


class Iframe:
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def _get_element(self) -> WebElement:
        return Swd.get_driver().find_element(*self.locator)

    def switch_into(self):
        iframe = self._get_element()
        log_debug(f"{self.name} - switching into the frame")
        Swd.get_driver().switch_to.frame(iframe)
        return iframe

    def switch_out_of(self):
        log_debug(f"{self.name} - switching out of the frame")
        Swd.get_driver().switch_to.default_content()

    def get_text(self):
        log_info(f"{self.name} - getting text from the frame")
        self.switch_into()
        iframe_text = Swd.get_driver().find_element(By.XPATH, "//body").text
        self.switch_out_of()
        return iframe_text

    def get_text_from_nested_iframe(self):
        log_debug(f"{self.name} - getting text from nested frame")
        self.switch_into()
        nested_iframe = Iframe((By.XPATH, "//iframe"), "nested iframe")
        text_from_nested_iframe = nested_iframe.get_text()
        self.switch_out_of()
        return text_from_nested_iframe
