from task3.framework.elements.base_element import BaseElement
from task3.framework.utils.logger_utils import LoggerUtils
from task3.framework.utils.wait_utils import WaitUtils


class BaseForm:
    def __init__(self, unique_element: BaseElement, page_name: str):
        self.page_name = page_name
        self.unique_element = unique_element
        self.page_handle = None

    def is_open(self):
        LoggerUtils.log_info(f"Checking if {self.page_name} is open")
        self.wait_for_page_to_load()
        return self.unique_element.is_exists()

    def wait_for_page_to_load(self):
        LoggerUtils.log_debug(
            f"waiting for {self.page_name} to load - for the unique element to be present and visible"
        )
        WaitUtils.wait_for_element_to_be_present_and_visible(
            self.unique_element.locator
        )
