class ParseUtils:
    @staticmethod
    def table_row_string_to_list(row_text):
        return row_text.split("\n")

    @staticmethod
    def table_row_is_empty(row_text: str):
        if len(row_text.strip()) == 0:
            return True

    @staticmethod
    def calculate_error_percentage(desired_value, obtained_value):
        return round((abs(obtained_value - desired_value) / abs(desired_value)) * 100)
