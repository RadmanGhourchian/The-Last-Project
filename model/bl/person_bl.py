from model.da.person_da import PersonDa
from model.entity.person import Person



class PersonBl:
    @staticmethod
    def save(person):
        person_da = PersonDa()
        person_da.save(person)

    @staticmethod
    def edit(person):
        person_da = PersonDa()
        person_da.edit(person)


    @staticmethod
    def remove(id):
        person_da = PersonDa()
        person_da.remove(id)

    @staticmethod
    def find_all(person):
        person_da = PersonDa()
        return person_da.find_all()

    @staticmethod
    def find_by_id(id):
        person_da = PersonDa()
        return person_da.find_by_id(id)