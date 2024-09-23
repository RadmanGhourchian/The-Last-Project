from model.entity.library import Library
from model.da.library_da import LibraryDa

class BookController:
    library_da = LibraryDa()

    @classmethod
    def save(cls, name, b_id, person_name, language, genre, In_Out=True):
        try:
            book = Library(name, b_id, person_name, language, genre, In_Out)
            cls.library_da.save(book)
            return True, f"Book {book} Saved!"
        except Exception as e:
            return False, str(e)
    @classmethod
    def edit(cls, name, b_id, person_name, language, genre, In_Out=True):
        try:
            book = Library(name, b_id, person_name, language, genre, In_Out)
            cls.library_da.edit(book)
            return True, f"Book {book} Edited!"
        except Exception as e:
            return False, str(e)
    @classmethod
    def delete(cls, id):
        try:
            cls.library_da.remove(id)
            return True, f"Book {id} Deleted!"
        except Exception as e:
            return False, str(e)
    @classmethod
    def find_all(cls):
        try:
            lister = cls.library_da.find_all()
            return lister
        except Exception as e:
            return False, str(e)
    @classmethod
    def find_by_id(cls, id):
        try:
            cls.library_da.find_by_id(id)
            return True, f"Book {id} Found!"
        except Exception as e:
            return False, str(e)
    @classmethod
    def find_by_genre(cls, genre):
        try:
            return cls.library_da.find_by_genre(genre)
        except Exception as e:
            return False, str(e)
