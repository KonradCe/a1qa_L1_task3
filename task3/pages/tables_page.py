from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements import (
    BasicElement,
    ButtonElement,
    TableRows,
    InputElement,
)


class WebTablesPage(BaseForm):
    UNIQUE_ELEMENT_LOC = (
        By.XPATH,
        "//div[@class='main-header' and text()[contains(., 'Web Tables')]]",
    )
    ADD_RECORD_BTN_LOC = (By.XPATH, "//button[@id='addNewRecordButton']")
    TABLE_LOC = (By.XPATH, "//div[contains(@class, 'ReactTable')]")
    SEARCH_INPUT_LOC = (By.XPATH, "//input[@id='searchBox']")

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "alerts page unique header"),
            "alerts page",
        )

    def click_add_btn(self):
        add_record_btn = ButtonElement(
            self.ADD_RECORD_BTN_LOC, "add records to the table button"
        )
        add_record_btn.click()

    def confirm_user_in_table(self, user):
        self.enter_text_into_table_searchbox(user["email"])
        table = TableRows("Table on 'Web Tables' page")
        result = table.is_user_in_table(user)
        self.clear_searchbox()
        return result

    def enter_text_into_table_searchbox(self, text):
        searchbox = InputElement(
            self.SEARCH_INPUT_LOC, "searchbox input on 'Web Tables' page"
        )
        self.clear_searchbox()
        searchbox.send_text(text)

    def clear_searchbox(self):
        searchbox = InputElement(
            self.SEARCH_INPUT_LOC, "searchbox input on 'Web Tables' page"
        )
        searchbox.clear()

    def delete_user_entry(self, user):
        self.enter_text_into_table_searchbox(user["email"])
        table = TableRows("Table on 'Web Tables' page")
        table.delete_user(user)
        self.clear_searchbox()

    def get_number_of_records(self):
        table = TableRows("Table on 'Web Tables' page")
        return table.get_number_of_records()
