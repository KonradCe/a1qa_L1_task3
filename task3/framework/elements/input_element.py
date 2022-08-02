from selenium.webdriver import Keys

from task3.framework.elements.base_element import BaseElement


class InputElement(BaseElement):
    def send_text(self, input_string):
        self._get_element().send_keys(input_string)

    def clear(self):
        self._get_element().clear()
        # as some input fields may be dynamically changing page depending on the input inside (like search box on tables
        # page),sometimes clearing the filed is not sufficient 'refresh' the content - that is what code below is about
        self._get_element().send_keys("a")
        self._get_element().send_keys(Keys.BACK_SPACE)
