from person import Person
from person_da import PersonDa

class PersonController:
    person_da = PersonDa()

    @classmethod
    def save(cls, name, family, password, email ,number):
        try:
            book = Person(name, family, password, email, number)
            cls.person_da.save(book)
            return True, f"Book {book} Saved!"
        except Exception as e:
            return False, str(e)
    @classmethod
    def edit(cls, name, family, password, email, number):
        try:
            book = Person(name, family, password, email, number)
            cls.person_da.edit(book)
            return True, f"Book {book} Edited!"
        except Exception as e:
            print("ddd")
            return False, str(e)
    @classmethod
    def delete(cls, id):
        try:
            cls.person_da.delete(id)
            return True, f"Book {id} Deleted!"
        except Exception as e:
            print("ccc")
            return False, str(e)
    @classmethod
    def find_all(cls):
        try:
            return cls.person_da.find_all()
        except Exception as e:
            print("bbb")
            return False, str(e)
    @classmethod
    def find_by_id(cls, id):
        try:
            cls.person_da.find_by_id(id)
            return True, f"Book {id} Found!"
        except Exception as e:
            print("aaa")
            return False, str(e)
    # @classmethod
    # def find_by_genre(cls, genre):
    #     try:
    #         cls.person_da.find_by_genre(genre)
    #         return True, f"Book {genre} Found!"
    #     except Exception as e:
    #         return False, str(e)
