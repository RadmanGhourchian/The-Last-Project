# from Books.Controller.Bill_Controller import BillController
# from datetime import *
from controller.person_controller import PersonController

# lib = Library("aaa", "132132", "radman", "english", "action", 1)

# LibraryDa().save(lib)
# BookController().delete(8)
# BillController().save(str(datetime.now()), "12341234", "aaa")
# BillController().save(datetime.now(), "12341234", "aaa", "1000")
# print(BillController().find_all())


PersonController.save("radman", "ghoorchian", "1234567890", "radman@gmail.com", "09178505323")