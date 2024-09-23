import re


class Validator:
    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def username_validator(cls, username, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @classmethod
    def password_validator(cls, password, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,16}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def family_validator(cls, family, message):
        if re.match(r"^[a-zA-Z]{3,30}$", family):
            return family
        else:
            raise ValueError(message)

    @classmethod
    def id_validator(cls, id, message):
        if type(id) == int and id >= 0:
            return id
        else:
            raise ValueError(message)

    @classmethod
    def language_validator(cls, language, message):
        if re.match(r"^[a-zA-Z]{5,30}$", language):
            return language
        else:
            raise ValueError(message)

    @classmethod
    def genre_validator(cls, genre, message):
        if re.match(r"^[a-zA-Z\d\s_\-]{5,30}$", genre):
            return genre
        else:
            raise ValueError(message)

    @classmethod
    def amount_validator(cls, amount, message):
        if type(amount) == int and amount >= 0:
            return True
        else:
            raise ValueError(message)

    @classmethod
    def phone_number_validator(cls, phone_number, message):
        if type(phone_number) == str and re.match(r"^.*$", phone_number):
            return True
        else:
            raise ValueError(message)

    @classmethod
    def email_validator(cls, email, message):
        if type(email) == str  and re.match(r"^.*$", email):
            return email
        else:
            raise ValueError(message)
