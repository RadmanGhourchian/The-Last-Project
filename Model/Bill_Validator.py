import re

def id_validator(id):
    if re.match(r"^[\d\_\-]{2,18}$", id):
        return True
    else:
        return False
def book_name_validator(book_name):
    if re.match(r"^[a-zA-Z\d\s\d]{3,25}$", book_name):
        return True
    else:
        return False
def amount_validator(amount):
    if re.match(r"^[\d]{1,8}$", amount):
        return True
    else:
        return False