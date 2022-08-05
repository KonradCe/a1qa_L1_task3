from task3.framework.utils.logger_utils import LoggerUtils
from task3.framework.utils.parse_utils import ParseUtils
from task3.framework.utils.test_data_utils import TestDataUtils
from task3.pages.main_page import MainPage
from task3.pages.progress_page import ProgressBarPage
from task3.pages.slider_page import SliderPage
from task3.pages.support_forms.left_pannel_menu import LeftPanelMenu


def test_slider_and_progress_bar(driver_setup_teardown):

    LoggerUtils.log_info("start of TEST CASE 5 - SLIDERS, PROGRESS BAR")
    # STEP 1: navigate to main page
    # -> main page is open
    LoggerUtils.log_info("STEP 1: navigate to main page")
    main_page = MainPage()
    main_page.go_to_main_page()
    error_message_step1 = "opening main page should result in main page being open"
    assert main_page.is_open(), error_message_step1

    # STEP 2: Click on Widgets button. In the menu on the left click Slider button
    # -> Page with Slider form is open
    LoggerUtils.log_info(
        "STEP 2: Click on Widgets button. In the menu on the left click Slider button"
    )
    main_page.click_on_widgets_btn()
    left_panel_menu = LeftPanelMenu()
    left_panel_menu.click_on_button_from_category(
        button_name="Slider", category_name="Widgets"
    )

    slider_page = SliderPage()
    error_message_step2 = "opening slider page should result in slider page being open"
    assert slider_page.is_open(), error_message_step2

    # STEP 3: Set slider to a valid randomly generated value
    # -> Value on the page near the slider is equals to the one set before
    LoggerUtils.log_info("STEP 3: Set slider to a valid randomly generated value")
    random_value = TestDataUtils.generate_random_number_in_0_100_range()
    slider_page.set_slider_value_to(random_value)
    error_message_step3 = f"slider should be set to value: {random_value}"
    assert slider_page.get_slider_value() == random_value, error_message_step3

    # STEP 4: In the left menu click Progress Bar button
    # -> Page with Progress Bar form is open
    LoggerUtils.log_info("STEP 4: In the left menu click Progress Bar button")
    left_panel_menu.click_on_button_from_category(
        button_name="Progress Bar", category_name="Widgets"
    )
    progress_bar_page = ProgressBarPage()
    error_message_step4 = "clicking on 'progress bar' button in left panel menu should result in 'progress bar page' being open"
    assert progress_bar_page.is_open(), error_message_step4

    # STEP 5: Click on Start button
    LoggerUtils.log_info("STEP 5: Click on Start button")
    progress_bar_page.start_stop_progress_bar()

    # STEP 6: Click on Stop button, when value displayed on progress bar becomes equals to your age
    # -> Value on progress bar is equal to your age (error is not higher than 2 %)
    LoggerUtils.log_info(
        "STEP 6: Click on Stop button, when value displayed on progress bar becomes equals to your age"
    )
    desired_value = TestDataUtils.get_my_age()
    progress_bar_page.stop_progress_at_value(desired_value)
    error_percentage = ParseUtils.calculate_error_percentage(
        desired_value=desired_value,
        obtained_value=progress_bar_page.get_value_from_progress_bar(),
    )
    error_message_step5 = "the difference between the desired and the obtained value from the progress bar is too high"
    assert error_percentage <= 2, error_message_step5


if __name__ == "__main__":
    test_slider_and_progress_bar(None)
