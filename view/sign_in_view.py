import datetime
from EntryWithLabel_Class import *
import tkinter.ttk as ttk
from controller.Person_Controller import PersonController
# from Booksehlf_View import BooksehlfView
import tkinter.messagebox as msg
from controller.book_controller import BookController
from controller.bill_controller import BillController


class SignInView:
    def __init__(self):
        self.win = Tk()
        self.win.title("Sign In")
        self.win.resizable(False, False)
        self.win.geometry("500x500")

        self.name = EntryWithLabel(self.win, "Name : ", 10, 5, 140, "str")
        self.family = EntryWithLabel(self.win, "Family : ", 10, 45, 140, "str")
        self.password = EntryWithLabel(self.win, "Password : ", 10, 85, 140, "str")
        self.Email = EntryWithLabel(self.win, "Email : ", 10, 125, 140, "str")
        self.number = EntryWithLabel(self.win, "Number : ", 10, 165, 140, "str")

        Label(self.win, text="Which One Are You : ").place(x=10, y=205)
        self.Pat_Per = ttk.Combobox(self.win, values=("Patron", "Person"), state="readonly",width=17).place(x=150, y=205)

        Button(self.win, text="Sign In", width=10, command=self.SignIn_click).place(x=195, y=350)

        self.win.mainloop()

    def SignIn_click(self):
        def Do_Button():
            for i in table.get_children():
                table.delete(i)
            if self.In_Out.get() == int("1"):
                BookController().save(self.book_name.get(), self.book_id.get(), self.person_name.get(), self.language.get(),
                                      self.genre.get(), self.In_Out.get())
            elif self.In_Out.get() == int("0"):
                BookController().delete(self.Id.get())

            for i in BookController.find_all():
                table.insert("", END, values=i)
        def table_person_refresher():
            for i in table_person.get_children():
                table_person.delete(i)

            for i in PersonController.find_all():
                table_person.insert("", END, values=i)
        def table_bill_refresher():
            for i in table_bill.get_children():
                table_bill.delete(i)

            for i in BillController().find_all():
                table_bill.insert("", END, values=i)
        def table_bill_refresher_adder():
            for i in table_bill.get_children():
                table_bill.delete(i)
            BillController().save(datetime.datetime.now(), self.bill_id.get(), self.book_name.get(), self.bill_amount.get())

            for i in BillController.find_all():
                table_bill.insert("", END, values=i)
        def table_find_genra():
            for i in table.get_children():
                table.delete(i)
            for i in BookController.find_by_genre(self.genre.get()):
                table.insert("", END, values=i)
        def table_refresher_usuall():
            for i in table.get_children():
                table.delete(i)
            for i in BookController.find_all():
                table.insert("", END, values=i)

        status, person = PersonController().save(self.name.get(), self.family.get(), self.password.get(), self.Email.get(), self.number.get())
        if status:
            print(status)
            self.win.destroy()
            self.window = Tk()
            self.window.title("Library")
            self.window.geometry("1700x700")

            self.book_name = EntryWithLabel(self.window, "Book Name : ", 10, 5, 120, "str")
            self.book_id = EntryWithLabel(self.window, "Book Id : ", 10, 45, 120, "str")
            self.person_name = EntryWithLabel(self.window, "Person Name : ", 10, 85, 120, "str")
            self.language = EntryWithLabel(self.window, "Language : ", 10, 125, 120, "str")
            self.genre = EntryWithLabel(self.window, "Genre : ", 10, 165, 120, "str")
            self.In_Out = EntryWithLabel(self.window, "In or Out : ", 10, 205, 120, "bool")
            self.Id = EntryWithLabel(self.window, "Id : ", 10, 245, 120, "int")
            self.bill_id = EntryWithLabel(self.window, "Bill Id : ", 10, 285, 120, "str")
            self.bill_amount = EntryWithLabel(self.window, "Bill Amount : ", 10, 325, 120, "str")

            Button(self.window, text="Do", command=Do_Button).place(x=9, y=400)

            table = ttk.Treeview(self.window, height=20, columns=(1,2,3,4,5,6,7), show="headings")

            table.heading(1, text="Name")
            table.heading(2, text="Book Id")
            table.heading(3, text="Person Name")
            table.heading(4, text="Language")
            table.heading(5, text="Genre")
            table.heading(6, text="In or Out")
            table.heading(7, text="Id")

            table.column(1, width=100)
            table.column(2, width=100)
            table.column(3, width=100)
            table.column(4, width=100)
            table.column(5, width=100)
            table.column(6, width=100)
            table.column(7, width=100)

            table.place(x=285, y=5)

            table_refresher_usuall()

            table_person = ttk.Treeview(self.window, height=28, columns=(1,2), show="headings")

            table_person.heading(1, text="Person Name")
            table_person.heading(2, text="Family Name")

            table_person.column(1, width=100)
            table_person.column(2, width=100)

            table_person.place(x=1000, y=5)

            table_person_refresher()

            table_bill = ttk.Treeview(self.window, height=28, columns=(1,2,3,4), show="headings")

            table_bill.heading(1, text="Bill Date")
            table_bill.heading(2, text="Bill Id")
            table_bill.heading(3, text="Bill Book Name")
            table_bill.heading(4, text="Bill Amount")

            table_bill.column(1, width=100)
            table_bill.column(2, width=100)
            table_bill.column(3, width=100)
            table_bill.column(4, width=100)

            table_bill.place(x=1230, y=5)

            Button(self.window, text="Bill_Do", command=table_bill_refresher_adder).place(x=120, y=400)

            table_bill_refresher()

            Button(self.window, text="Find_Genre", command=table_find_genra).place(x=9, y=450)

            Button(self.window, text="Normal Book", command=table_refresher_usuall).place(x=120, y=450)

            self.window.mainloop()
        else:
            msg.showerror("Error", "Please Enter Correct Data!")


sgn = SignInView()