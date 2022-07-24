from task3.framework.elements import BaseElement
from task3.framework.utils.logger_utils import log_debug


# TODO: make abstract
class BaseForm:
    def __init__(self, unique_element: BaseElement, page_name: str):
        self.page_name = page_name
        self.unique_element = unique_element

    def is_open(self):
        log_debug(f"Checking if {self.page_name} is open")
        return self.unique_element.is_exists()
