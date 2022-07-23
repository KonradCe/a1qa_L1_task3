from task3.framework.elements import BaseElement


# TODO: make abstract
class BaseForm:
    def __init__(self, unique_element: BaseElement, page_name: str):
        self.page_name = page_name
        self.unique_element = unique_element

    def is_open(self):
        return self.unique_element.is_exists()
