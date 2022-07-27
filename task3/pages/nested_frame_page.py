from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements import BasicElement, Iframe


class NestedFramePage(BaseForm):
    UNIQUE_ELEMENT_LOC = (
        By.XPATH,
        "//div[@class='main-header' and text()[contains(., 'Nested Frames')]]",
    )
    PARENT_IFRAME_LOC = (By.XPATH, "//iframe[@id='frame1']")
    NESTED_FRAMES_FORM_LOC = (By.XPATH, "//div[@id='framesWrapper']")

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "nested frames unique header"),
            "page with nested frames",
        )

    def is_nested_frames_form_open(self):
        nested_frames_form = BasicElement(
            self.NESTED_FRAMES_FORM_LOC, "form to test alerts"
        )
        return nested_frames_form.is_exists()

    def get_text_from_parent_iframe(self) -> str:
        parent_iframe = Iframe(self.PARENT_IFRAME_LOC, "Parent Iframe")
        return parent_iframe.get_text()

    def get_text_from_child_iframe(self) -> str:
        parent_iframe = Iframe(self.PARENT_IFRAME_LOC, "Parent Iframe")
        nested_text = parent_iframe.get_text_from_nested_iframe()
        return nested_text
