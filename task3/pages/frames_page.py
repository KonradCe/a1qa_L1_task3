from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements import BasicElement, Iframe


class FramesPage(BaseForm):
    UNIQUE_ELEMENT_LOC = (
        By.XPATH,
        "//div[@class='main-header' and text()[contains(., 'Frames')] and text()[not(contains(., 'Nested'))]]",
    )
    UPPER_FRAME_LOC = (By.XPATH, "//div[@id='frame1Wrapper']//iframe")
    LOWER_FRAME_LOC = (By.XPATH, "//div[@id='frame2Wrapper']//iframe")

    def __init__(self):
        super().__init__(
            BasicElement(self.UNIQUE_ELEMENT_LOC, "Frames page unique header"),
            "frames page",
        )

    def get_text_from_upper_frame(self):
        upper_frame = Iframe(self.UPPER_FRAME_LOC, "Upper frame from frame page")
        return upper_frame.get_text()

    def get_text_from_lower_frame(self):
        lower_frame = Iframe(self.LOWER_FRAME_LOC, "Lower frame from frame page")
        return lower_frame.get_text()
