from task3.framework.elements import BaseElement
from task3.framework.utils.logger_utils import log_info


class BaseForm:
    def __init__(self, unique_element: BaseElement, page_name: str):
        self.page_name = page_name
        self.unique_element = unique_element

    def is_open(self):
        log_info(f"Checking if {self.page_name} is open")
        return self.unique_element.is_exists()
