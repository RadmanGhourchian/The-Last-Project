from model.da.library_da import LibraryDa
from model.entity.book import Book
from model.entity.borrow import Borrow
from model.da.borrow_da import BorrowDa
from model.entity.person import Person
from model.da.person_da import PersonDa
from model.bl.borrow_bl import BorrowBl
from model.bl.book_bl import BookBl
from model.bl.person_bl import PersonBl
from controller.borrow_controller import BorrowController
from controller.book_controller import BookController
from controller.person_controller import PersonController




PersonController().save("Radman", "Ghourchian", "123456789", "ghourchian@gmail.com", "09126337315")
# BookController().save(1, "LORD OF MOUNTAINS", "radman", 1325364, "english", "acation")
# person = Person(3, "Radman", "Ghourchianaaaa", "12345678", "ghourchian@gmail.com", "09126337314")
# PersonBl().save(person)
# PersonDa().edit(person)
# print(PersonDa().find_by_id(2))

# borrow = Borrow(1, "Radman", "Lord Of Rings 3", "2024-8-10", "2024-11-10", 15)
# print(BorrowController().find_by_id(5))
# BorrowBl().save(borrow)
# print(BorrowDa().find_by_id(2))

# book = Book(3, "Harry Potter 5", "J-K-Roling--", 15246, "german", "action")
# BookBl().save(book)
# LibraryDa().edit(bowok)
# LibraryDa().save(book)