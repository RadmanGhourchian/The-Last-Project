import re

def name_validator(name):
    if re.match(r"^[a-zA-Z\_\-\s]{3,30}$", name):
        return True
    else:
        return False
def family_validator(family):
    if re.match(r"^[a-zA-Z]{3,30}$", family):
        return True
    else:
        return False
def book_id(book_id):
    if re.match(r"^\d{2,40}$", book_id):
        return True
    else:
        return False
def person_name_validatort(person_name):
    if re.match(r"^[a-zA-Z]{3,30}$", person_name):
        return True
    else:
        return False

def language_validator(language):
    if re.match(r"^[a-zA-Z]{5,30}$", language):
        return True
    else:
        return False
def genre_validator(genre):
    if re.match(r"^[a-zA-Z\d\s\_\-]{5,30}$", genre):
        return True
    else:
        return False

