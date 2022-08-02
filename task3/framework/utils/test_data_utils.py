import json
import random
import string
from pathlib import Path

test_data_file_path = Path(__file__).resolve().parents[2] / "data" / "test_data.json"
user_data_file_path = Path(__file__).resolve().parents[2] / "data" / "user_data.json"


def get_main_page_url() -> str:
    with open(test_data_file_path) as f:
        j = json.load(f)
    return j["main_page_url"]


def get_desired_strings_for_test_case2() -> dict:
    with open(test_data_file_path) as f:
        j = json.load(f)
    return j["test_case_2_result_strings"]


def get_user_data() -> list[dict]:
    with open(user_data_file_path) as f:
        j = json.load(f)
    return j["users"]


def generate_random_string() -> str:
    letters = string.ascii_letters
    length = random.randrange(3, 20)
    random_list = [random.choice(letters) for i in range(length)]
    return "".join(random_list)
