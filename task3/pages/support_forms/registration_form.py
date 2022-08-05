from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.button_element import ButtonElement
from task3.framework.elements.input_element import InputElement


class RegistrationForm(BaseForm):
    __unique_element = BasicElement(
        (By.XPATH, "//div[@id='registration-form-modal']"),
        "unique element of registration form on 'Web Tables' page",
    )
    __submit_entry_btn = ButtonElement(
        (By.XPATH, "//button[@id='submit']"), "submit entry button in registration form"
    )
    __first_name_input = InputElement(
        (By.XPATH, "//input[@id='firstName']"),
        "first name input element in registration form",
    )
    __last_name_input = InputElement(
        (By.XPATH, "//input[@id='lastName']"),
        "last name input element in registration form",
    )
    __email_input = InputElement(
        (By.XPATH, "//input[@id='userEmail']"),
        "email input element in registration form",
    )
    __age_input = InputElement(
        (By.XPATH, "//input[@id='age']"), "age input element in registration form"
    )
    __salary_input = InputElement(
        (By.XPATH, "//input[@id='salary']"),
        "salary input element in registration form",
    )
    __department_input = InputElement(
        (By.XPATH, "//input[@id='department']"),
        "department input element in registration form",
    )

    def __init__(self):
        super().__init__(
            self.__unique_element, "registration form on 'Web Tables' page"
        )

    def submit_user_data(self, user):
        self.__first_name_input.send_text(user["first_name"])
        self.__last_name_input.send_text(user["last_name"])
        self.__email_input.send_text(user["email"])
        self.__age_input.send_text(user["age"])
        self.__salary_input.send_text(user["salary"])
        self.__department_input.send_text(user["department"])

        self.__submit_entry_btn.click()

    def is_closed(self):
        return self.__unique_element.is_gone(wait=True)
