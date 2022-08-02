from selenium.webdriver.common.by import By

from task3.framework.elements.base_element import BaseElement
from task3.framework.utils import wait_utils


class SubMenu(BaseElement):
    def click_on_button_with_text(self, btn_string, wait=False):
        button = (
            super()
            ._get_element()
            .find_element(By.XPATH, f"//span[contains(text(), '{btn_string}')]")
        )
        if wait:
            wait_utils.wait_for_element_to_be_clickable(button)
        button.click()
