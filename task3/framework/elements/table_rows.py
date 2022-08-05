from selenium.webdriver.common.by import By

from task3.framework.utils.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils.parse_utils import ParseUtils


class TableRows:
    ROWS_LOC = (By.XPATH, "//div[@role='rowgroup']")
    DELETE_BTN_LOC = (By.XPATH, "//span[contains(@id, 'delete-record')]")

    def __init__(self, name):
        self.name = name

    def get_rows(self):
        return Swd.get_driver().find_elements(*self.ROWS_LOC)

    def get_row_nb(self, row_nb):
        specific_row_loc = (By.XPATH, f"//div[@role='rowgroup'][{row_nb+1}]")
        return Swd.get_driver().find_element(*specific_row_loc)

    def get_number_of_records(self):
        # every record in table gets its own delete button - so the number of records is the same as number of delete button
        # disclaimer: this only works, when all the records in the table are displayed on the current page
        return len(Swd.get_driver().find_elements(*self.DELETE_BTN_LOC))

    def is_data_in_table(self, data):
        if self.get_row_nb_with_data(data) != -1:
            return True
        else:
            return False

    def get_row_nb_with_data(self, data) -> int:
        rows = self.get_rows()
        for row_nb, row in enumerate(rows):
            if not ParseUtils.table_row_is_empty(row.text):
                parsed_row = ParseUtils.table_row_string_to_list(row.text)
                if set(parsed_row) == set(
                    data.values()
                ):  # this makes sure that all the values match
                    return row_nb
        return -1

    def click_delete_in_row_nb(self, row_to_delete):
        delete_btn_in_specific_row_loc = (
            By.XPATH,
            f"//div[@role='rowgroup'][{row_to_delete+1}]//span[contains(@id, 'delete-record')]",
        )
        delete_btn_in_specific_row = Swd.get_driver().find_element(
            *delete_btn_in_specific_row_loc
        )
        delete_btn_in_specific_row.click()
