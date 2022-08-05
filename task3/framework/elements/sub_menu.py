from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

from task3.framework.elements.base_element import BaseElement
from task3.framework.utils.config_data_utils import ConfigUtils
from task3.framework.utils.driver_utils import SingletonWebDriver as Swd
from task3.framework.utils.wait_utils import WaitUtils


class SubMenu(BaseElement):
    def click_on_button_with_text(self, btn_string, wait=False):
        button = (
            super()
            ._get_element()
            .find_element(By.XPATH, f"//span[contains(text(), '{btn_string}')]")
        )
        if wait:
            WaitUtils.wait_for_element_to_be_clickable(button)

        try:
            button.click()
        except ElementClickInterceptedException:
            # if the element in the menu is not clickable due to an ad at the bottom of the page, we scroll down

            # Firefox has trouble scrolling with webdriver, better to use JS to scroll instead
            if ConfigUtils.get_browser_of_choice().lower() == "firefox":
                Swd.get_driver().execute_script("window.scrollBy(0,250)", "")
            else:
                scroll_origin = ScrollOrigin.from_element(button)
                ActionChains(Swd.get_driver()).scroll_from_origin(
                    scroll_origin, 0, 200
                ).perform()

            if wait:
                WaitUtils.wait_for_element_to_be_clickable(button)
            button.click()
