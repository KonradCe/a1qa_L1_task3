import json
import random
import string
from pathlib import Path

from typing import List


class TestDataUtils:
    test_data_file_path = (
        Path(__file__).resolve().parents[2] / "data" / "test_data.json"
    )
    user_data_file_path = (
        Path(__file__).resolve().parents[2] / "data" / "user_data.json"
    )

    @classmethod
    def get_main_page_url(cls) -> str:
        with open(cls.test_data_file_path) as f:
            j = json.load(f)
        return j["main_page_url"]

    @classmethod
    def get_desired_strings_for_test_case2(cls) -> dict:
        with open(cls.test_data_file_path) as f:
            j = json.load(f)
        return j["test_case_2_result_strings"]

    @classmethod
    def get_user_data(cls) -> List[dict]:
        with open(cls.user_data_file_path) as f:
            j = json.load(f)
        return j["users"]

    @classmethod
    def generate_random_string(cls) -> str:
        letters = string.ascii_letters
        length = random.randrange(3, 20)
        random_list = [random.choice(letters) for i in range(length)]
        return "".join(random_list)
