def get_file_from_path(original_string: str, sepatator: str = "/"):
    return original_string[original_string.rfind("/") + 1 :]
