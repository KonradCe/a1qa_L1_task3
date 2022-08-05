from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.alert import Alert
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.button_element import ButtonElement
from task3.framework.utils.logger_utils import LoggerUtils
from task3.framework.utils.test_data_utils import TestDataUtils


class AlertsPage(BaseForm):
    __unique_element = BasicElement(
        (
            By.XPATH,
            "//div[@id='javascriptAlertsWrapper']",
        ),
        "alerts page unique header",
    )

    __alert_btn = ButtonElement(
        (By.XPATH, "//button[@id='alertButton']"), "button to trigger alert"
    )
    __confirmation_btn = ButtonElement(
        (By.XPATH, "//button[@id='confirmButton']"),
        "button to trigger confirmation box",
    )
    __positive_confirmation_msg_element = BasicElement(
        (By.XPATH, "//span[@id='confirmResult' and text()[contains(.,'Ok')]]"),
        "message after accepting confirm box",
    )
    __prompt_btn = ButtonElement(
        (By.XPATH, "//button[@id='promtButton']"), "button to trigger prompt"
    )

    def __init__(self):
        super().__init__(self.__unique_element, "alerts page")

    def click_on_alert_button(self):
        LoggerUtils.log_info(f"{self.page_name} - clicking on {self.__alert_btn.name}")
        self.__alert_btn.click()

    def click_on_confirmation_btn(self):
        LoggerUtils.log_info(
            f"{self.page_name} - clicking on {self.__confirmation_btn.name}"
        )
        self.__confirmation_btn.click()

    def click_on_prompt_btn(self):
        LoggerUtils.log_info(f"{self.page_name} - clicking on {self.__prompt_btn.name}")
        self.__prompt_btn.click()

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
        LoggerUtils.log_info(
            f"{self.page_name} - checking if positive confirmation message exist"
        )
        return self.__positive_confirmation_msg_element.is_exists()

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
