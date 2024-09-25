from model.entity.borrow import Borrow
from model.da.borrow_da import BorrowDa
from model.tools.decorators import exception_handling

class BorrowController:
    bill_da = BorrowDa()

    @classmethod
    @exception_handling
    def save(cls, person, book, borrow_date_time, return_date_time, amount):
        bill = Borrow(0, person, book, borrow_date_time, return_date_time, amount)
        cls.bill_da.save(bill)
        return True, f"Book {bill} Saved!"
    @classmethod
    @exception_handling
    def edit(cls, id, person, book, borrow_date_time, return_date_time, amount):
        book = Borrow(id, person, book, borrow_date_time, return_date_time, amount)
        cls.bill_da.edit(book)
        return True, f"Book {book} Edited!"
    @classmethod
    @exception_handling
    def delete(cls, id):
        cls.bill_da.remove(id)
        return True, f"Book {id} Deleted!"
    @classmethod
    @exception_handling
    def find_all(cls):
        return cls.bill_da.find_all()
    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return cls.bill_da.find_by_id(id)
    # @classmethod
    # def find_by_genre(cls, genre):
    #     try:
    #         cls.person_da.find_by_genre(genre)
    #         return True, f"Book {genre} Found!"
    #     except Exception as e:
    #         return False, str(e)
