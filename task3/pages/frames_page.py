from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.iframe import Iframe


class FramesPage(BaseForm):
    __unique_element = BasicElement(
        (
            By.XPATH,
            "//div[@class='main-header' and text()[contains(., 'Frames')] and text()[not(contains(., 'Nested'))]]",
        ),
        "Frames page unique header",
    )
    __upper_frame = Iframe(
        (By.XPATH, "//div[@id='frame1Wrapper']//iframe"), "Upper frame from frame page"
    )
    __lower_frame = Iframe(
        (By.XPATH, "//div[@id='frame2Wrapper']//iframe"), "Lower frame from frame page"
    )

    def __init__(self):
        super().__init__(self.__unique_element, "frames page")

    def get_text_from_upper_frame(self):
        return self.__upper_frame.get_text()

    def get_text_from_lower_frame(self):
        return self.__lower_frame.get_text()
