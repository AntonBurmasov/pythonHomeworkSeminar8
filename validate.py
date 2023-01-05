import re


def check_phone(phone):
    if re.fullmatch('\+?[1-9]\d{6,12}', phone):
        return True
    return False
