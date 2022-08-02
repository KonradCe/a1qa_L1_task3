from task3.framework.elements.base_element import BaseElement


class ButtonElement(BaseElement):
    def get_text(self):
        btn_element = super()._get_element()
        print(btn_element.text)
