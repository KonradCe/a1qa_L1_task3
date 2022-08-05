from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.button_element import ButtonElement
from task3.framework.elements.input_element import InputElement
from task3.framework.elements.table_rows import TableRows
from task3.framework.utils.logger_utils import LoggerUtils


class WebTablesPage(BaseForm):
    __unique_element = BasicElement(
        (By.XPATH, "//div[@class='main-header' and text()[contains(., 'Web Tables')]]"),
        "alerts page unique header",
    )
    __web_table_form = BasicElement(
        (By.XPATH, "//div[@class='web-tables-wrapper']"), "web tables wrapper"
    )
    __add_record_btn = ButtonElement(
        (By.XPATH, "//button[@id='addNewRecordButton']"),
        "add records to the table button",
    )
    __search_input = InputElement(
        (By.XPATH, "//input[@id='searchBox']"), "searchbox input on 'Web Tables' page"
    )

    def __init__(self):
        super().__init__(
            self.__unique_element,
            "alerts page",
        )

    def click_add_btn(self):
        LoggerUtils.log_info(
            f"{self.page_name} - clicking on {self.__add_record_btn.name}"
        )
        self.__add_record_btn.click()

    def confirm_user_in_table(self, user):
        LoggerUtils.log_info(
            f"{self.page_name} - confirming user record ({user['first_name']} {user['last_name']}) in table"
        )
        self.enter_text_into_table_searchbox(user["email"])
        table = TableRows("Table on 'Web Tables' page")
        result = table.is_data_in_table(user)
        self.clear_searchbox()
        return result

    def enter_text_into_table_searchbox(self, text):
        LoggerUtils.log_info(
            f"{self.page_name} - entering text (={text}) into searchbox"
        )
        self.clear_searchbox()
        self.__search_input.send_text(text)

    def clear_searchbox(self):
        LoggerUtils.log_debug(f"{self.page_name} - removing input from searchbox")
        self.__search_input.clear()

    def delete_user_entry(self, user):
        LoggerUtils.log_info(
            f"{self.page_name} - deleting user record ({user['first_name']} {user['last_name']}) from table"
        )
        self.enter_text_into_table_searchbox(user["email"])

        table = TableRows("Table on 'Web Tables' page")
        row_to_delete = table.get_row_nb_with_data(user)
        if row_to_delete == -1:
            LoggerUtils.log_warning(
                f"No user - {user['first_name']} {user['last_name']} - in table)"
            )
        table.click_delete_in_row_nb(row_to_delete)
        self.clear_searchbox()

    def get_number_of_records(self):
        LoggerUtils.log_info(f"{self.page_name} - getting number of records in table")
        table = TableRows("Table on 'Web Tables' page")
        return table.get_number_of_records()
