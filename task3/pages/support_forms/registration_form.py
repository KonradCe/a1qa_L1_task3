from selenium.webdriver.common.by import By

from task3.framework.base_form import BaseForm
from task3.framework.elements.basic_element import BasicElement
from task3.framework.elements.button_element import ButtonElement
from task3.framework.elements.input_element import InputElement


class RegistrationForm(BaseForm):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@id='registration-form-modal']")
    SUBMIT_ENTRY_BTN = (By.XPATH, "//button[@id='submit']")

    FIRST_NAME_INPUT_LOC = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME_INPUT_LOC = (By.XPATH, "//input[@id='lastName']")
    EMAIL_INPUT_LOC = (By.XPATH, "//input[@id='userEmail']")
    AGE_INPUT_LOC = (By.XPATH, "//input[@id='age']")
    SALARY_INPUT_LOC = (By.XPATH, "//input[@id='salary']")
    DEPARTMENT_INPUT_LOC = (By.XPATH, "//input[@id='department']")

    def __init__(self):
        # the wait is here to ensure the element has appeared on screen
        # WaitUtils.wait_for_element_to_be_present_and_visible(self.UNIQUE_ELEMENT_LOC)
        super().__init__(
            BasicElement(
                self.UNIQUE_ELEMENT_LOC,
                "unique element of registration form on 'Web Tables' page",
            ),
            "registration form on 'Web Tables' page",
        )

    def submit_user_data(self, user):
        first_name_input = InputElement(
            self.FIRST_NAME_INPUT_LOC, "first name input element in registration form"
        )
        last_name_input = InputElement(
            self.LAST_NAME_INPUT_LOC, "last name input element in registration form"
        )
        email_input = InputElement(
            self.EMAIL_INPUT_LOC, "email input element in registration form"
        )
        age_input = InputElement(
            self.AGE_INPUT_LOC, "age input element in registration form"
        )
        salary_input = InputElement(
            self.SALARY_INPUT_LOC, "salary input element in registration form"
        )
        department_input = InputElement(
            self.DEPARTMENT_INPUT_LOC, "department input element in registration form"
        )

        first_name_input.send_text(user["first_name"])
        last_name_input.send_text(user["last_name"])
        email_input.send_text(user["email"])
        age_input.send_text(user["age"])
        salary_input.send_text(user["salary"])
        department_input.send_text(user["department"])

        ButtonElement(
            self.SUBMIT_ENTRY_BTN, "submit entry button in registration form"
        ).click()

    def is_closed(self):
        unique_element = BasicElement(
            self.UNIQUE_ELEMENT_LOC,
            "unique element of registration form on 'Web Tables' page",
        )
        return unique_element.is_gone(wait=True)
