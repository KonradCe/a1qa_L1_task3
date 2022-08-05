from task3.framework.elements.base_element import BaseElement
from task3.framework.utils.wait_utils import WaitUtils


class ProgressBarElement(BaseElement):
    PROGRESS_BAR_VALUE_ATTRIBUTE = "aria-valuenow"

    def wait_for_value(self, value):
        WaitUtils.text_in_attribute(
            locator=self.locator,
            attribute=self.PROGRESS_BAR_VALUE_ATTRIBUTE,
            text=value,
        )

    def get_value(self):
        return int(self.get_attribute(self.PROGRESS_BAR_VALUE_ATTRIBUTE))
