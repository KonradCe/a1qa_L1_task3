from selenium.webdriver.common.by import By

import task3.framework.driver_utils
import task3.framework.elements
import task3.framework.utils.test_data_utils
from task3.framework.base_form import BaseForm


class MainPage(BaseForm):
    URL = task3.framework.utils.test_data_utils.get_main_page_url()
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@class='home-banner']")
    ALERT_FRAME_WINDOW_BTN_LOC = (
        By.XPATH,
        "//div[contains(@class, 'top-card')]//h5[contains(text(),'Alerts')]",
    )

    def __init__(self):
        super().__init__(
            task3.framework.elements.UniqueElement(
                self.UNIQUE_ELEMENT_LOC, "unique element on main page"
            ),
            "main page",
        )

    def go_to_main_page(self):
        task3.framework.driver_utils.go_to_page(self.URL)

    def click_on_alert_frame_window_btn(self):
        alerts_frame_window_btn = task3.framework.elements.ButtonElement(
            self.ALERT_FRAME_WINDOW_BTN_LOC, "Alerts, Frame & Windows Button"
        )
        alerts_frame_window_btn.click()
