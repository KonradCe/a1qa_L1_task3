from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements import BasicElement, SubMenu


class LeftPanelMenu(BaseForm):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@class='left-pannel']")

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "left menu panel unique element"),
            "left menu panel",
        )

    def click_on_button_from_category(self, button_name, category_name):
        alerts_frame_windows_category_btn_loc = (
            By.XPATH,
            f"//div[@class='header-text' and text()[contains(., '{category_name}')]]",
        )
        alerts_frame_windows_element_list_loc = (
            By.XPATH,
            f"//div[@class='header-text' and text()[contains(., '{category_name}')]]//following::div[contains(@class, 'element-list')]",
        )

        alerts_frame_windows_sub_menu = SubMenu(
            alerts_frame_windows_element_list_loc, "'Alerts, Frame & Windows' sub menu"
        )

        # checks if category with desired button is collapsed, if true it clicks on it to expand the category
        if not alerts_frame_windows_sub_menu.is_displayed():
            category_btn = BasicElement(
                alerts_frame_windows_category_btn_loc,
                "'Alerts, Frame & Windows' category button",
            )
            category_btn.click()

        alerts_frame_windows_sub_menu.click_on_button_with_text(button_name)
