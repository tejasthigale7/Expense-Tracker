import re
from datetime import datetime


def is_valid_date(date_string):
    pattern = r"^\d{4}-\d{2}-\d{2}$"

    if not re.fullmatch(pattern, date_string):
        return False

    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except:
        return False
