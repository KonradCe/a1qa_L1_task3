from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.iframe import Iframe
from task3.framework.utils.logger_utils import LoggerUtils


class NestedFramePage(BaseForm):
    __unique_element = BasicElement(
        (By.XPATH, "//div[@id='framesWrapper']"), "nested frames unique header"
    )
    __parent_iframe = Iframe((By.XPATH, "//iframe[@id='frame1']"), "Parent Iframe")

    def __init__(self):
        super().__init__(
            self.__unique_element,
            "page with nested frames",
        )

    def get_text_from_parent_iframe(self) -> str:
        LoggerUtils.log_info(
            f"{self.page_name} - getting text from {self.__parent_iframe.name}"
        )
        return self.__parent_iframe.get_text()

    def get_text_from_child_iframe(self) -> str:
        LoggerUtils.log_info(f"{self.page_name} - getting text from nested iframe")
        nested_text = self.__parent_iframe.get_text_from_nested_iframe()
        return nested_text
