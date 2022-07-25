from task3.framework.utils import test_data_utils as data_utils
from task3.framework.utils.logger_utils import log_info
from task3.pages.alerts_page import AlertsPage
from task3.pages.main_page import MainPage
from task3.pages.nested_frame_page import NestedFramePage


def test_case2(driver_setup_teardown):
    log_info("start of TEST CASE 2 - IFRAME")
    # STEP 1: Navigate to main page -> main page is open
    log_info("STEP 1: navigate to main page")
    main_page = MainPage()
    main_page.go_to_main_page()
    error_message_step1 = "opening main page should result in main page being open"
    assert main_page.is_open(), error_message_step1

    # STEP 2: Click on Alerts, Frame & Windows button; In a menu click Nested Frames button
    # -> Page with Nested Frames form is open.
    # -> There are messages "Parent frame" & "Child Iframe" present on page
    main_page.click_on_alert_frame_window_btn()
    alerts_page = AlertsPage()
    alerts_page.click_on_button_from_category_in_menu(
        button_name="Nested Frames", category_name="Frame"
    )

    nested_frames_page = NestedFramePage()

    error_message_step2a = "clicking on 'Nested Frames' button in menu should result in a page with nested frames being open"
    assert nested_frames_page.is_open(), error_message_step2a

    expected_strings = data_utils.get_desired_strings_for_test_case2()
    error_message_step2b = "the parent iframe should contain text 'Parent frame'"
    assert (
        nested_frames_page.get_text_from_parent_iframe() == expected_strings["parent"]
    ), error_message_step2b
    error_message_step2c = "the child iframe should contain text 'Child Iframe'"
    assert (
        nested_frames_page.get_text_from_child_iframe() == expected_strings["child"]
    ), error_message_step2c


if __name__ == "__main__":
    test_case2(None)
