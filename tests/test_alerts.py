from task3.pages.alerts_page import AlertsPage
from task3.pages.main_page import MainPage
from task3.framework.utils.logger_utils import log_debug


def test_case1(driver_setup_teardown):

    # STEP 1: navigate to main page
    # -> main page is open
    log_debug("STEP 1: navigate to main page")
    main_page = MainPage()
    main_page.go_to_main_page()
    error_message_step1 = "opening main page should result in main page being open"
    assert main_page.is_open(), error_message_step1

    # STEP 2: Click on Alerts, Frame & Windows button. In a menu click Alerts button.
    # -> Alerts form has appeared on page
    log_debug("STEP 2: Click on Alerts, Frame & Windows button...")
    main_page.click_on_alert_frame_window_btn()

    alerts_page = AlertsPage()
    log_debug("STEP 2: ...In a menu click Alerts button.")
    alerts_page.click_on_alert_btn_in_menu()
    error_message_step2 = (
        "clicking on alerts button in the menu should show form to test alerts"
    )
    assert alerts_page.is_alerts_form_open(), error_message_step2

    # STEP 3: Click on 'Click Button to see alert' button
    # -> Alert with text "You clicked a button" is open
    log_debug("STEP 3: Click on 'Click Button to see alert' button")
    alerts_page.click_on_alert_button()
    error_message_step3 = "clicking on alerts button should prompt an alert with 'You clicked a button' text."
    assert alerts_page.alert_with_text_is_open(
        "You clicked a button"
    ), error_message_step3

    # STEP 4: Click OK button
    # -> alert has closed
    log_debug("Click OK button")
    alerts_page.accept_alert()
    error_message_step4 = "Accepting the alert should cause alert to close"
    assert alerts_page.alert_is_closed(), error_message_step4

    # STEP 5: Click on 'On button click, confirm box will appear' button
    # -> 'Alert with text "Do you confirm action?" is open'
    log_debug("STEP 5: Click on 'On button click, confirm box will appear' button")
    alerts_page.click_on_confirmation_btn()
    error_message_step5 = (
        "clicking on 'On button click, confirm box will appear button' should prompt a "
        "confirmation box, with 'Do you confirm action?' text"
    )
    assert alerts_page.alert_with_text_is_open(
        "Do you confirm action?"
    ), error_message_step5

    # STEP 6: Click on OK button
    # -> Alert has closed
    # -> Text "You selected Ok" has appeared on page
    log_debug("STEP 6: Click on OK button")
    alerts_page.accept_alert()
    error_message_step6 = (
        "clicking accepting confirmation box should result in two things: closing of the "
        "confirmation windows, and 'you selected OK' text appearing next to the button"
    )
    assert alerts_page.alert_is_closed(), error_message_step6
    assert alerts_page.positive_confirmation_msg_exist(), error_message_step5

    # STEP 7: Click on "On button click, prompt box will appear" button
    # -> Alert with text "Please enter your name" is open
    log_debug("STEP 7: Click on 'On button click, prompt box will appear' button")
    alerts_page.click_on_prompt_btn()
    error_message_step7 = (
        "clicking on 'On button click, prompt box will appear' should trigger a "
        "prompt, with 'Please enter your name' text"
    )
    assert alerts_page.alert_with_text_is_open(
        "Please enter your name"
    ), error_message_step7

    # STEP 8: Enter randomly generated text, click OK button
    # -> Alert has closed
    # -> Appeared text equals to the one you've entered before
    log_debug("STEP 8: Enter randomly generated text, click OK button...")
    text_input = alerts_page.send_random_input_to_prompt()
    log_debug("STEP 8: ...click OK button")
    alerts_page.accept_alert()
    error_message_step8 = (
        "enetering random input and accepting the prompt should result in 2 things: "
        "closing of the prompt and a messaged with entered text next to the button"
    )
    assert alerts_page.alert_is_closed(), error_message_step8
    assert alerts_page.prompt_confirmation_msg_with_text_exist(
        text_input
    ), error_message_step8


if __name__ == "__main__":
    test_case1(None)
