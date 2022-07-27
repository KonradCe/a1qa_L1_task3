import pytest

from task3.framework.utils import test_data_utils as data_utils
from task3.framework.utils.logger_utils import log_info
from task3.pages.main_page import MainPage
from task3.pages.support_forms.left_pannel_menu import LeftPanelMenu
from task3.pages.support_forms.registration_form import RegistrationForm
from task3.pages.tables_page import WebTablesPage


@pytest.mark.parametrize("user", data_utils.get_user_data())
def test_case3(driver_setup_teardown, user):
    # STEP 1: Navigate to main page
    # -> main page is open
    log_info("start of TEST CASE 3 - TABLES")
    log_info("STEP 1: navigate to main page")
    main_page = MainPage()
    main_page.go_to_main_page()
    error_message_step1 = "opening main page should result in main page being open"
    assert main_page.is_open(), error_message_step1

    # STEP 2: Click on Elements button; In the menu click a Web Tables button
    # -> Page with Web Tables form is open
    main_page.click_on_elements_btn()
    left_menu = LeftPanelMenu()
    left_menu.click_on_button_from_category(
        button_name="Web Tables", category_name="Elements"
    )
    tables_page = WebTablesPage()
    error_message_step2 = (
        "clicking on 'Web Tables' button in the menu should open 'Web Tables' page"
    )
    assert tables_page.is_open(), error_message_step2

    # STEP 3: Click on Add button
    # -> Registration Form has appeared on page
    tables_page.click_add_btn()
    error_message_step3 = "clicking 'add' button should show registration from on page"
    registration_form = RegistrationForm()
    assert registration_form.is_open(), error_message_step3

    # STEP 4: Enter data for User № from the table and then click Submit button
    # -> Registration form has closed.
    # -> Data of User № has appeared in a table
    registration_form.submit_user_data(user)
    error_message_step4a = "after clicking submit registration form should close"
    assert registration_form.is_closed(), error_message_step4a

    error_message_step4b = "submitted user data should appear in table"
    assert tables_page.confirm_user_in_table(user), error_message_step4b

    # STEP 5: Click Delete button in a row which contains data of User
    # -> Number of records in table has changed
    # -> Data of User has been deleted from table
    nb_of_records_before_deletion = tables_page.get_number_of_records()
    tables_page.delete_user_entry(user)
    nb_of_records_after_deletion = tables_page.get_number_of_records()
    error_message_step5 = "number of records before deleting the user, should be higher then the number of records after deletion"
    assert (
        nb_of_records_before_deletion > nb_of_records_after_deletion
    ), error_message_step5


if __name__ == "__main__":
    temp_user = data_utils.get_user_data()[0]
    test_case3(None, temp_user)
