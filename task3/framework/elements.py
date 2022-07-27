from selenium.common.exceptions import (
    NoAlertPresentException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from task3.framework.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils import parse_utils
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

    def wait_for_element(self):
        return wait_utils.wait_for_element_to_be_present_and_visible(self.locator)

    def is_gone(self, wait=False):
        if wait:
            try:
                wait_utils.wait_for_element_to_be_gone(self.locator)
            except TimeoutException:
                return False
        try:
            self._get_element()
            return False
        except NoSuchElementException:
            return True


class ButtonElement(BaseElement):
    def get_text(self):
        btn_element = super()._get_element()
        print(btn_element.text)


class BasicElement(BaseElement):
    pass


class InputElement(BaseElement):
    def send_text(self, input_string):
        self._get_element().send_keys(input_string)

    def clear(self):
        self._get_element().clear()
        # as some input fields may be dynamically changing page depending on the input inside (like search box on tables
        # page),sometimes clearing the filed is not sufficient 'refresh' the content - that is what code below is about
        self._get_element().send_keys("a")
        self._get_element().send_keys(Keys.BACK_SPACE)


class SubMenu(BaseElement):
    def click_on_button_with_text(self, btn_string, wait=False):
        button = (
            super()
            ._get_element()
            .find_element(By.XPATH, f"//span[contains(text(), '{btn_string}')]")
        )
        if wait:
            wait_utils.wait_for_element_to_be_clickable(button)
        button.click()


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


class Iframe:
    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def _get_element(self) -> WebElement:
        return Swd.get_driver().find_element(*self.locator)

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


class TableRows:
    ROWS_LOC = (By.XPATH, "//div[@role='rowgroup']")
    DELETE_BTN_LOC = (By.XPATH, "//span[contains(@id, 'delete-record')]")

    def __init__(self, name):
        self.name = name

    def __get_rows(self):
        return Swd.get_driver().find_elements(*self.ROWS_LOC)

    def __get_row_nb(self, row_nb):
        specific_row_loc = (By.XPATH, f"//div[@role='rowgroup'][{row_nb+1}]")
        return Swd.get_driver().find_element(*specific_row_loc)

    def is_user_in_table(self, user):
        if self.get_row_nb_with_user(user) != -1:
            return True
        else:
            return False

    def get_row_nb_with_user(self, user) -> int:
        rows = self.__get_rows()
        for row_nb, row in enumerate(rows):
            if not parse_utils.table_row_is_empty(row.text):
                parsed_row = parse_utils.table_row_string_to_list(row.text)
                if set(parsed_row) == set(
                    user.values()
                ):  # this makes sure that all the values match
                    return row_nb
        return -1

    def get_number_of_records(self):
        # every record in table gets its own delete button - so the number of records is the same as number of delete button
        # disclaimer: this only works, when all the records in the table are displayed on the current page
        return len(Swd.get_driver().find_elements(*self.DELETE_BTN_LOC))

    def delete_user(self, user):
        row_to_delete = self.get_row_nb_with_user(user)
        if row_to_delete == -1:
            # TODO: raise an exception or maybe log a warning here
            pass
        delete_btn_in_specific_row_loc = (
            By.XPATH,
            f"//div[@role='rowgroup'][{row_to_delete+1}]//span[contains(@id, 'delete-record')]",
        )
        delete_btn_in_specific_row = Swd.get_driver().find_element(
            *delete_btn_in_specific_row_loc
        )
        delete_btn_in_specific_row.click()
