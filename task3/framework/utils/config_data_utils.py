import json
from pathlib import Path


class ConfigUtils:

    config_data_file_path = (
        Path(__file__).resolve().parents[2] / "data" / "config_data.json"
    )

    @classmethod
    def get_explicit_wait_time(cls):
        with open(cls.config_data_file_path) as f:
            j = json.load(f)
            wait_time = j["explicit_wait_time"]
        return wait_time

    @classmethod
    def get_browser_of_choice(cls):
        with open(cls.config_data_file_path) as f:
            j = json.load(f)
            browser = j["browser"]
        return browser

    @classmethod
    def get_chrome_params(cls) -> list:
        with open(cls.config_data_file_path) as f:
            j = json.load(f)
            chrome_parameters = [*j["chrome_params"]]
        return chrome_parameters

    @classmethod
    def get_firefox_options_params(cls) -> list:
        with open(cls.config_data_file_path) as f:
            j = json.load(f)
            options_params = [*j["firefox_options_params"]]
        return options_params

    @classmethod
    def get_firefox_options_prefs(cls) -> dict:
        with open(cls.config_data_file_path) as f:
            j = json.load(f)
            profile_prefs = j["firefox_profile_prefs"]
        return profile_prefs
