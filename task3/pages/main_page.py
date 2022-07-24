from selenium.webdriver.common.by import By

import task3.framework.driver_utils
from task3.framework.elements import BasicElement
import task3.framework.utils.test_data_utils
from task3.framework.base_form import BaseForm
from task3.pages.left_pannel_menu import LeftPanelMenu


class MainPage(BaseForm):
    URL = task3.framework.utils.test_data_utils.get_main_page_url()
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@class='home-banner']")
    ALERT_FRAME_WINDOW_BTN_LOC = (
        By.XPATH,
        "//div[contains(@class, 'top-card')]//h5[contains(text(),'Alerts')]",
    )
    ALERTS_FORM_LOC = (By.XPATH, "//div[@id='javascriptAlertsWrapper']")

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "unique element on main page"),
            "main page",
        )

    def go_to_main_page(self):
        task3.framework.driver_utils.go_to_page(self.URL)

    def click_on_alert_frame_window_btn(self):
        alerts_frame_window_btn = task3.framework.elements.ButtonElement(
            self.ALERT_FRAME_WINDOW_BTN_LOC, "Alerts, Frame & Windows Button"
        )
        alerts_frame_window_btn.click()

    def click_on_alert_btn_in_menu(self):
        left_menu = LeftPanelMenu()
        left_menu.click_on_button_from_category(
            button_name="Alerts", category_name="Frame"
        )

    def is_alerts_form_open(self):
        alerts_form = BasicElement(self.ALERTS_FORM_LOC, "form to test alerts")
        return alerts_form.is_exists()
