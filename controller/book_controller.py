from model.entity.book import Book
from model.da.library_da import LibraryDa
from model.tools.decorators import exception_handling


class BookController:
    library_da = LibraryDa()

    @classmethod
    @exception_handling
    def save(cls, title, author, isbn, language, genre):
        book = Book(0, title, author, isbn, language, genre)
        cls.library_da.save(book)
        return True, f"Book {book} Saved!"        

    @classmethod
    @exception_handling
    def edit(cls, id, title, author, isbn, language, genre):
        book = Book(id, title, author, isbn, language, genre)
        cls.library_da.edit(book)
        return True, f"Book {book} Edited!"        

    @classmethod
    @exception_handling
    def delete(cls, id):
        cls.library_da.remove(id)
        return True, f"Book {id} Deleted!"

    @classmethod
    @exception_handling
    def find_all(cls):
        lister = cls.library_da.find_all()
        return lister

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return cls.library_da.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_genre(cls, genre):
        return cls.library_da.find_by_genre(genre)
