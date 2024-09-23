class Borrow:
    def __init__(self, id, person, book, borrow_date_time, return_date_time, amount):
        self.id = id
        self.person = person
        self.book = book
        self.borrow_date_time = borrow_date_time
        self.return_date_time = return_date_time
        self.amount = amount