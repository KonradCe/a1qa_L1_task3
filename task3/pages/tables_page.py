from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements import BasicElement, ButtonElement, WebTable, InputElement
import task3.framework.utils.wait_utils as wait_utils
from task3.pages.support_forms.registration_form import RegistrationForm


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
        web_table = WebTable(self.TABLE_LOC, "table on 'Web Tables' page")
        return web_table.is_user_in_table(user)

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
        pass

