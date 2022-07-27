from task3.framework.elements import BaseElement
from task3.framework.utils import wait_utils
from task3.framework.utils.logger_utils import log_info
from task3.framework.driver_utils import SingletonWebDriver as Swd


class BaseForm:
    def __init__(self, unique_element: BaseElement, page_name: str):
        self.page_name = page_name
        self.unique_element = unique_element
        self.page_handle = None

    def is_open(self):
        log_info(f"Checking if {self.page_name} is open")
        self.wait_for_page_to_load()
        return self.unique_element.is_exists()

    def wait_for_page_to_load(self):
        wait_utils.wait_for_element_to_be_present_and_visible(
            self.unique_element.locator
        )

    # TODO: move it out
    def set_handle(self):
        self.page_handle = Swd.get_driver().current_window_handle
