from task3.framework.utils.logger_utils import LoggerUtils
from task3.pages.frames_page import FramesPage
from task3.pages.main_page import MainPage
from task3.pages.nested_frame_page import NestedFramePage
from task3.pages.support_forms.left_pannel_menu import LeftPanelMenu


def test_getting_data_from_frames(driver_setup_teardown):
    desired_string_parent_frame = "Parent frame"
    desired_string_nested_frame = "Child Iframe"

    LoggerUtils.log_info("start of TEST CASE 2 - IFRAME")
    # STEP 1: Navigate to main page -> main page is open
    LoggerUtils.log_info("STEP 1: navigate to main page")
    main_page = MainPage()
    main_page.go_to_main_page()
    error_message_step1 = "opening main page should result in main page being open"
    assert main_page.is_open(), error_message_step1

    # STEP 2: Click on Alerts, Frame & Windows button; In a menu click Nested Frames button
    # -> Page with Nested Frames form is open.
    # -> There are messages "Parent frame" & "Child Iframe" present on page
    LoggerUtils.log_info("STEP 2: Click on Alerts, Frame & Windows button...")
    main_page.click_on_alert_frame_window_btn()
    LoggerUtils.log_info("STEP 2: ...In a menu click Nested Frames button")
    left_menu = LeftPanelMenu()
    left_menu.click_on_button_from_category(
        button_name="Nested Frames", category_name="Frame"
    )
    nested_frames_page = NestedFramePage()

    error_message_step2a = "clicking on 'Nested Frames' button in menu should result in a page with nested frames being open"
    assert nested_frames_page.is_open(), error_message_step2a

    error_message_step2b = "the parent iframe should contain text 'Parent frame'"
    assert (
        nested_frames_page.get_text_from_parent_iframe() == desired_string_parent_frame
    ), error_message_step2b

    error_message_step2c = "the child iframe should contain text 'Child Iframe'"
    assert (
        nested_frames_page.get_text_from_child_iframe() == desired_string_nested_frame
    ), error_message_step2c

    # STEP 3: Select Frames option in a left menu
    # -> Page with Frames form is open.
    # -> Message from upper frame is equal to the message from lower frame
    LoggerUtils.log_info("STEP 3: Select Frames option in a left menu")
    left_menu.click_on_button_from_category(
        button_name="Frames", category_name="Alerts, Frame"
    )
    frames_page = FramesPage()
    error_message_step3a = "clicking on 'Frames' button in menu should result in a page with frames being open"
    assert frames_page.is_open(), error_message_step3a

    upper_frame_text = frames_page.get_text_from_upper_frame()
    lower_frame_text = frames_page.get_text_from_lower_frame()
    error_message_step3b = (
        "text from upper frame should be equal to the text form bottom frame"
    )
    assert upper_frame_text == lower_frame_text, error_message_step3b


if __name__ == "__main__":
    test_case2(None)
