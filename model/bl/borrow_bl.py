from model.da.borrow_da import BorrowDa
from model.entity.borrow import Borrow

class BorrowBl:
    @staticmethod
    def save(borrow):
        borrow_da = BorrowDa()
        borrow_da.save(borrow)

    @staticmethod
    def edit(borrow):
        borrow_da = BorrowDa()
        borrow_da.edit(borrow)

    @staticmethod
    def remove(id):
        borrow_da = BorrowDa()
        borrow_da.remove(id)

    @staticmethod
    def find_all(person):
        borrow_da = BorrowDa()
        return borrow_da.find_all()

    @staticmethod
    def find_by_id(id):
        borrow_da = BorrowDa()
        return borrow_da.find_by_id(id)