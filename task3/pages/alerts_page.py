import selenium.common.exceptions
from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements import BasicElement, ButtonElement
from task3.framework.utils import wait_utils, test_data_utils
from task3.pages.left_pannel_menu import LeftPanelMenu


class AlertsPage(BaseForm):
    UNIQUE_ELEMENT_LOC = (
        By.XPATH,
        "//div[@class='main-header' and contains(text(), 'Alerts')]",
    )
    ALERTS_FORM_LOC = (By.XPATH, "//div[@id='javascriptAlertsWrapper']")
    ALERT_BTN_LOC = (By.XPATH, "//button[@id='alertButton']")
    CONFIRMATION_BTN_LOC = (By.XPATH, "//button[@id='confirmButton']")
    POSITIVE_CONFIRMATION_MSG_LOC = (
        By.XPATH,
        "//span[@id='confirmResult' and contains(text(), Ok)]",
    )
    PROMPT_BTN_LOC = (By.XPATH, "//button[@id='promtButton']")

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "alerts header"), "alerts page"
        )

    def click_on_alert_btn_in_menu(self):
        left_menu = LeftPanelMenu()
        left_menu.click_on_button_from_category(
            button_name="Alerts", category_name="Frame"
        )

    def is_alerts_form_open(self):
        alerts_form = BasicElement(self.ALERTS_FORM_LOC, "form to test alerts")
        return alerts_form.is_exists()

    def click_on_alert_button(self):
        alert_button = ButtonElement(self.ALERT_BTN_LOC, "button to trigger alert")
        alert_button.click()

    def click_on_confirmation_btn(self):
        confirmation_btn = ButtonElement(
            self.CONFIRMATION_BTN_LOC, "button to trigger confirmation box"
        )
        confirmation_btn.click()

    def click_on_prompt_btn(self):
        prompt_btn = ButtonElement(self.PROMPT_BTN_LOC, "button to trigger prompt")
        prompt_btn.click()

    def alert_with_text_is_open(self, text):
        alert = wait_utils.wait_for_alert()
        return alert.text == text

    def accept_alert(self):
        alert = wait_utils.wait_for_alert()
        alert.accept()

    def alert_is_closed(self):
        try:
            wait_utils.wait_for_alert_to_close()
        except selenium.common.exceptions.TimeoutException:
            return False
        else:
            return True

    def positive_confirmation_msg_exist(self):
        confirmation_msg = BasicElement(
            self.POSITIVE_CONFIRMATION_MSG_LOC, "message after accepting confirm box"
        )
        return confirmation_msg.is_exists()

    def send_random_input_to_prompt(self) -> str:
        text_to_enter = test_data_utils.generate_random_string()
        prompt = wait_utils.wait_for_alert()
        prompt.send_keys(text_to_enter)
        return text_to_enter

    def prompt_confirmation_msg_with_text_exist(self, text_in_message):
        prompt_confirmation_msg_loc = (
            By.XPATH,
            f"//span[@id='promptResult' and contains(text(), {text_in_message})]",
        )
        confirmation_msg = BasicElement(
            prompt_confirmation_msg_loc, "message after accepting prompt"
        )
        return confirmation_msg.is_exists()
