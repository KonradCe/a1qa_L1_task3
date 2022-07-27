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
        category_header_loc = (
            By.XPATH,
            f"//div[@class='header-text' and text()[contains(., '{category_name}')]]",
        )
        elements_in_category_list_loc = (
            By.XPATH,
            f"//div[@class='header-text' and text()[contains(., '{category_name}')]]//following::div[contains(@class, 'element-list')]",
        )

        sub_menu = SubMenu(
            elements_in_category_list_loc, f"sub menu of '{category_name}' category"
        )

        # checks if category with desired button is collapsed, if true it clicks on it to expand the category
        if not sub_menu.is_displayed():
            category_btn = BasicElement(
                category_header_loc,
                "'Alerts, Frame & Windows' category button",
            )
            category_btn.click()

        sub_menu.click_on_button_with_text(button_name, wait=True)
