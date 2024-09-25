from model.tools.validator import Validator

class Borrow:
    def __init__(self, id, person, book, borrow_date_time, return_date_time, amount):
        self.id = id
        self.person = person
        self.book = book
        self.borrow_date_time = borrow_date_time
        self.return_date_time = return_date_time
        self.amount = amount

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, person):
        self._person = Validator.person_validator(person, "Invalid person")

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        self._book = Validator.book_name_validator(book, "Invalid book name")

    @property
    def borrow_date_time(self):
        return self._borrow_date_time

    @borrow_date_time.setter
    def borrow_date_time(self, borrow_date_time):
        self._borrow_date_time = Validator.borrow_date_time_validator(borrow_date_time, "Invalid borrow date")

    @property
    def return_date_time(self):
        return self._return_date_time

    @return_date_time.setter
    def return_date_time(self, return_date_time):
        if Validator.borrow_date_time_validator(self.borrow_date_time, "Invalid borrow date") == Validator.borrow_date_time_validator(return_date_time, "Invalid return date"):
            raise ValueError("Dates Can Not Be The Same!")
        else:
            self._return_date_time = Validator.borrow_date_time_validator(return_date_time, "Invalid return date")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = Validator.amount_validator(amount, "Invalid amount")