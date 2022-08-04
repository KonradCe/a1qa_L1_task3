from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.alert import Alert
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.button_element import ButtonElement
from task3.framework.utils.test_data_utils import TestDataUtils
from task3.framework.utils.logger_utils import LoggerUtils


class AlertsPage(BaseForm):
    UNIQUE_ELEMENT_LOC = (
        By.XPATH,
        "//div[@id='javascriptAlertsWrapper']",
    )

    ALERT_BTN_LOC = (By.XPATH, "//button[@id='alertButton']")
    CONFIRMATION_BTN_LOC = (By.XPATH, "//button[@id='confirmButton']")
    POSITIVE_CONFIRMATION_MSG_LOC = (
        By.XPATH,
        "//span[@id='confirmResult' and text()[contains(.,'Ok')]]",
    )
    PROMPT_BTN_LOC = (By.XPATH, "//button[@id='promtButton']")

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "alerts page unique header"),
            "alerts page",
        )

    def click_on_alert_button(self):
        alert_button = ButtonElement(self.ALERT_BTN_LOC, "button to trigger alert")
        LoggerUtils.log_info(f"{self.page_name} - clicking on {alert_button.name}")
        alert_button.click()

    def click_on_confirmation_btn(self):
        confirmation_btn = ButtonElement(
            self.CONFIRMATION_BTN_LOC, "button to trigger confirmation box"
        )
        LoggerUtils.log_info(f"{self.page_name} - clicking on {confirmation_btn.name}")
        confirmation_btn.click()

    def click_on_prompt_btn(self):
        prompt_btn = ButtonElement(self.PROMPT_BTN_LOC, "button to trigger prompt")
        LoggerUtils.log_info(f"{self.page_name} - clicking on {prompt_btn.name}")
        prompt_btn.click()

    def alert_with_text_is_open(self, text):
        LoggerUtils.log_info(
            f"{self.page_name} - checking if alert with text: '{text}' is open"
        )
        alert = Alert()
        return alert.get_text() == text

    def accept_alert(self):
        LoggerUtils.log_info(f"{self.page_name} - accepting alert")
        Alert().accept()

    def alert_is_closed(self):
        LoggerUtils.log_info(f"{self.page_name} - checking if alert is closed")
        return not Alert().is_alert_present()

    def positive_confirmation_msg_exist(self):
        confirmation_msg = BasicElement(
            self.POSITIVE_CONFIRMATION_MSG_LOC, "message after accepting confirm box"
        )
        LoggerUtils.log_info(
            f"{self.page_name} - checking if positive confirmation message exist"
        )
        return confirmation_msg.is_exists()

    def send_random_input_to_prompt(self) -> str:
        text_to_enter = TestDataUtils.generate_random_string()
        LoggerUtils.log_info(
            f"{self.page_name} - sending random input to prompt; random input = {text_to_enter}"
        )
        prompt = Alert()
        prompt.send_input(text_to_enter)
        return text_to_enter

    def prompt_confirmation_msg_with_text_exist(self, text_in_message):
        LoggerUtils.log_info(
            f"{self.page_name} - checking for postive confirmation message, containing previously entered random input"
        )
        prompt_confirmation_msg_loc = (
            By.XPATH,
            f"//span[@id='promptResult' and contains(text(), {text_in_message})]",
        )
        confirmation_msg = BasicElement(
            prompt_confirmation_msg_loc, "message after accepting prompt"
        )
        return confirmation_msg.is_exists()
