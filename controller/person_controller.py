from model.entity.person import Person
from model.da.person_da import PersonDa
from model.tools.decorators import exception_handling


class PersonController:
    person_da = PersonDa()

    @classmethod
    @exception_handling
    def save(cls, name, family, password, email, number):
        book = Person(0, name, family, password, email, number)
        cls.person_da.save(book)
        return True, f"Book {book} Saved!"

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, password, email, number):
        book = Person(id, name, family, password, email, number)
        cls.person_da.edit(book)
        return True, f"Book {book} Edited!"

    @classmethod
    @exception_handling
    def remove(cls, id):
        cls.person_da.remove(id)
        return True, f"Book {id} Deleted!"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.person_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, cls.person_da.find_by_id(id)
