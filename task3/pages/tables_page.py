from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.button_element import ButtonElement
from task3.framework.elements.input_element import InputElement
from task3.framework.elements.table_rows import TableRows
from task3.framework.utils.logger_utils import LoggerUtils


class WebTablesPage(BaseForm):
    UNIQUE_ELEMENT_LOC = (
        By.XPATH,
        "//div[@class='main-header' and text()[contains(., 'Web Tables')]]",
    )
    WEB_TABLE_FORM_LOC = (By.XPATH, "//div[@class='web-tables-wrapper']")
    ADD_RECORD_BTN_LOC = (By.XPATH, "//button[@id='addNewRecordButton']")
    TABLE_LOC = (By.XPATH, "//div[contains(@class, 'ReactTable')]")
    SEARCH_INPUT_LOC = (By.XPATH, "//input[@id='searchBox']")

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "alerts page unique header"),
            "alerts page",
        )

    def web_pages_form_is_open(self):
        tables_form = BasicElement(self.WEB_TABLE_FORM_LOC, "web tables wrapper")
        return tables_form.is_exists()

    def click_add_btn(self):
        add_record_btn = ButtonElement(
            self.ADD_RECORD_BTN_LOC, "add records to the table button"
        )
        LoggerUtils.log_info(f"{self.page_name} - clicking on {add_record_btn.name}")
        add_record_btn.click()

    def confirm_user_in_table(self, user):
        LoggerUtils.log_info(
            f"{self.page_name} - confirming user record ({user['first_name']} {user['last_name']}) in table"
        )
        self.enter_text_into_table_searchbox(user["email"])
        table = TableRows("Table on 'Web Tables' page")
        result = table.is_user_in_table(user)
        self.clear_searchbox()
        return result

    def enter_text_into_table_searchbox(self, text):
        LoggerUtils.log_info(
            f"{self.page_name} - entering text (={text}) into searchbox"
        )
        searchbox = InputElement(
            self.SEARCH_INPUT_LOC, "searchbox input on 'Web Tables' page"
        )
        self.clear_searchbox()
        searchbox.send_text(text)

    def clear_searchbox(self):
        LoggerUtils.log_debug(f"{self.page_name} - removing input from searchbox")
        searchbox = InputElement(
            self.SEARCH_INPUT_LOC, "searchbox input on 'Web Tables' page"
        )
        searchbox.clear()

    def delete_user_entry(self, user):
        LoggerUtils.log_info(
            f"{self.page_name} - deleting user record ({user['first_name']} {user['last_name']}) from table"
        )
        self.enter_text_into_table_searchbox(user["email"])
        table = TableRows("Table on 'Web Tables' page")
        table.delete_user(user)
        self.clear_searchbox()

    def get_number_of_records(self):
        LoggerUtils.log_info(f"{self.page_name} - getting number of records in table")
        table = TableRows("Table on 'Web Tables' page")
        return table.get_number_of_records()

