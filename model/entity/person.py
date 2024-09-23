from model.tools.validator import Validator


class Person:
    def __init__(self, id, name, family, password, email, number):
        self.id = id
        self.name = name
        self.family = family
        self.password = password
        self.email = email
        self.number = number

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = Validator.id_validator(id, "Invalid Id")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validator.name_validator(name, "Invalid Name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validator.family_validator(family, "Invalid Family")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = Validator.password_validator(password, "Invalid Password")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = Validator.email_validator(email, "Invalid Email")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = Validator.phone_number_validator(number, "Invalid Phone Number")

    def __repr__(self):
        return f"{self.__dict__}"
