from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.iframe import Iframe
from task3.framework.utils.logger_utils import log_info


class NestedFramePage(BaseForm):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@id='framesWrapper']")
    PARENT_IFRAME_LOC = (By.XPATH, "//iframe[@id='frame1']")

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "nested frames unique header"),
            "page with nested frames",
        )

    def get_text_from_parent_iframe(self) -> str:
        parent_iframe = Iframe(self.PARENT_IFRAME_LOC, "Parent Iframe")
        log_info(f"{self.page_name} - getting text from {parent_iframe.name}")
        return parent_iframe.get_text()

    def get_text_from_child_iframe(self) -> str:
        log_info(f"{self.page_name} - getting text from nested iframe")
        parent_iframe = Iframe(self.PARENT_IFRAME_LOC, "Parent Iframe")
        nested_text = parent_iframe.get_text_from_nested_iframe()
        return nested_text
