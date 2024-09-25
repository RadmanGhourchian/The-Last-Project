from model.da.library_da import LibraryDa
from model.entity.book import Book

class BookBl:
    @staticmethod
    def save(book):
        book_da = LibraryDa()
        book_da.save(book)

    @staticmethod
    def edit(book):
        book_da = LibraryDa()
        book_da.edit(book)

    @staticmethod
    def remove(id):
        book_da = LibraryDa()
        book_da.remove(id)

    @staticmethod
    def find_all(person):
        book_da = LibraryDa()
        return book_da.find_all()

    @staticmethod
    def find_by_id(id):
        book_da = LibraryDa()
        return book_da.find_by_id(id)