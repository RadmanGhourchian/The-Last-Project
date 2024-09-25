import datetime
from commponent import *
import tkinter.ttk as ttk
from controller.person_controller import PersonController
# from Booksehlf_View import BooksehlfView
import tkinter.messagebox as msg
from controller.book_controller import BookController
from controller.borrow_controller import BorrowController


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

            BookController().save(self.book_title.get(), self.book_author.get(), self.book_isbn.get(), self.language.get(), self.genre.get())
            for i in BookController.find_all():
                table.insert("", END, values=i)

            for i in table_person.get_children():
                table_person.delete(i)
            PersonController().save(self.name.get(), self.family.get(), self.password.get(), self.Email.get(), self.number.get())

            for i in PersonController().find_all():
                table_person.insert("", END, values=i)

            for i in table_bill.get_children():
                table_bill.delete(i)
            BorrowController().save(self.person_name.get(), self.book_title.get(), self.borrow_date_time.get(), self.return_date_time.get(), self.amount.get())

            for i in BorrowController().find_all():
                table_bill.insert("", END, values=i)


        def Remove_Button():
            for i in table.get_children():
                table.delete(i)
            BookController().delete(self.id.get())
            for i in BookController.find_all():
                table.insert("", END, values=i)

            for i in table_bill.get_children():
                table_bill.delete(i)
            BorrowController().delete(self.id.get())

            for i in BorrowController().find_all():
                table_bill.insert("", END, values=i)
        def Borrow_Button():
            for i in table.get_children():
                table.delete(i)
            BookController().delete(self.id.get())
            for i in BookController.find_all():
                table.insert("", END, values=i)

            for i in table_bill.get_children():
                table_bill.delete(i)
            BorrowController().delete(self.id.get())

            for i in BorrowController().find_all():
                table_bill.insert("", END, values=i)
        def Find_All_Button():
            for i in table.get_children():
                table.delete(i)

            for i in BookController().find_all():
                table.insert("", END, values=i)
        def Find_By_Id_Button():
            for i in table.get_children():
                table.delete(i)

            for i in BookController().find_by_id(self.id.get()):
                table.insert("", END, values=i)
        def Find_By_Genre_Button():
            for i in table.get_children():
                table.delete(i)

            for i in BookController().find_by_genre(self.genre.get()):
                table.insert("", END, values=i)
        def Find_All_Person_Button():
            for i in table_person.get_children():
                table_person.delete(i)

            for i in PersonController().find_all():
                table_person.insert("", END, values=i)
        def Find_By_Id_Person_Button():
            for i in table_person.get_children():
                table_person.delete(i)

            print(PersonController().find_by_id(self.id.get()))

            for i in PersonController().find_by_id(self.id.get()):
                table_person.insert("", END, values=i)
        def Find_All_Borrows_Button():
            for i in table_bill.get_children():
                table_bill.delete(i)

            for i in BorrowController().find_all():
                table_bill.insert("", END, values=i)
        def Find_By_Id_Borrows_Button():
            for i in table_bill.get_children():
                table_bill.delete(i)

            for i in BorrowController().find_by_id(self.id.get()):
                table_bill.insert("", END, values=i)
        def Edit_Books():
            for i in table.get_children():
                table.delete(i)
            BookController().edit(self.id.get(), self.book_title.get(), self.book_author.get(), self.book_isbn.get(), self.language.get(), self.genre.get())

            for i in BookController().find_all():
                table.insert("", END, values=i)
        def Edit_People():
            for i in table_person.get_children():
                table_person.delete(i)

            PersonController().edit(self.id.get(), self.person_name.get(), self.person_family.get(), self.person_password.get(), self.person_email.get(), self.person_number.get())
            for i in PersonController().find_all():
                table_person.insert("", END, values=i)
        def Edit_Borrows():
            for i in table_bill.get_children():
                table_bill.delete(i)
            BorrowController().edit(self.id.get(), self.person_name.get(), self.book_title.get(), self.borrow_date_time.get(), self.return_date_time.get(), self.amount.get())

            for i in BorrowController().find_all():
                table_bill.insert("", END, values=i)
        def Remove_Person_Button():
            for i in table_person.get_children():
                table_person.delete(i)
            PersonController().remove(self.id.get())

            for i in PersonController().find_all():
                table_person.insert("", END, values=i)
        def table_person_refresher():
            for i in table_person.get_children():
                table_person.delete(i)

            for i in PersonController.find_all():
                table_person.insert("", END, values=i)
        def table_bill_refresher():
            for i in table_bill.get_children():
                table_bill.delete(i)

            for i in BorrowController().find_all():
                table_bill.insert("", END, values=i)
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
            self.window.geometry("1700x2000")

            self.book_title = EntryWithLabel(self.window, "Book Title : ", 10, 5, 120, "str")
            self.book_author = EntryWithLabel(self.window, "Book Author : ", 10, 45, 120, "str")
            self.book_isbn = EntryWithLabel(self.window, "Book ISBN : ", 10, 85, 120, "int")
            self.language = EntryWithLabel(self.window, "Language : ", 10, 125, 120, "str")
            self.genre = EntryWithLabel(self.window, "Genre : ", 10, 165, 120, "str")
            self.person_name = EntryWithLabel(self.window, "Person Name : ", 10, 205, 120, "str")
            self.person_family = EntryWithLabel(self.window, "Person Family : ", 10, 245, 120, "str")
            self.person_password = EntryWithLabel(self.window, "Person Password : ", 10, 285, 120, "str")
            self.person_email = EntryWithLabel(self.window, "Person Email : ", 10, 325, 120, "str")
            self.person_number = EntryWithLabel(self.window, "Person Number : ", 10, 365, 120, "str")
            self.borrow_date_time = EntryWithLabel(self.window, "Borrow Date Time : ", 10, 405, 120, "str")
            self.return_date_time = EntryWithLabel(self.window, "Return Date Time : ", 10, 445, 120, "str")
            self.amount = EntryWithLabel(self.window, "Amount : ", 10, 485, 120, "int")
            self.id = EntryWithLabel(self.window, "Id : ", 10, 525, 120, "int")

            Button(self.window, text="Save", command=Do_Button).place(x=9, y=600)

            Button(self.window, text="Remove", command=Remove_Button).place(x=120, y=600)

            Button(self.window, text="Borrow", command=Borrow_Button).place(x=9, y=650)

            Button(self.window, text="Find All Books", command=Find_All_Button).place(x=120, y=650)

            Button(self.window, text="Find By Id Books", command=Find_By_Id_Button).place(x=9, y=700)

            Button(self.window, text="Find By Genre Books", command=Find_By_Genre_Button).place(x=120, y=700)

            Button(self.window, text="Find All Person", command=Find_All_Person_Button).place(x=9, y=750)

            Button(self.window, text="Find By Id Person", command=Find_By_Id_Person_Button).place(x=120, y=750)

            Button(self.window, text="Find All Borrows", command=Find_All_Borrows_Button).place(x=9, y=800)

            Button(self.window, text="Find By Id Borrows", command=Find_By_Id_Borrows_Button).place(x=120, y=800)

            Button(self.window, text="Edit Books", command=Edit_Books).place(x=9, y=850)

            Button(self.window, text="Edit People", command=Edit_People).place(x=120, y=850)

            Button(self.window, text="Edit Borrows", command=Edit_Borrows).place(x=9, y=900)

            Button(self.window, text="Remove Person", command=Remove_Person_Button).place(x=120, y=900)

            table = ttk.Treeview(self.window, height=20, columns=(1,2,3,4,5,6), show="headings")

            table.heading(1, text="Id")
            table.heading(2, text="Title")
            table.heading(3, text="Author")
            table.heading(4, text="ISBN")
            table.heading(5, text="Language")
            table.heading(6, text="Genre")

            table.column(1, width=70)
            table.column(2, width=80)
            table.column(3, width=80)
            table.column(4, width=80)
            table.column(5, width=90)
            table.column(6, width=80)

            table.place(x=265, y=5)

            table_refresher_usuall()

            table_person = ttk.Treeview(self.window, height=28, columns=(1,2,3,4,5,6), show="headings")

            table_person.heading(1, text="Id")
            table_person.heading(2, text="Person Name")
            table_person.heading(3, text="Family Name")
            table_person.heading(4, text="Password")
            table_person.heading(5, text="Email")
            table_person.heading(6, text="Number")

            table_person.column(1, width=70)
            table_person.column(2, width=100)
            table_person.column(3, width=100)
            table_person.column(4, width=100)
            table_person.column(5, width=100)
            table_person.column(6, width=100)

            table_person.place(x=760, y=5)

            table_person_refresher()

            table_bill = ttk.Treeview(self.window, height=28, columns=(1,2,3,4,5,6), show="headings")

            table_bill.heading(1, text="Id")
            table_bill.heading(2, text="Person Name")
            table_bill.heading(3, text="Book Name")
            table_bill.heading(4, text="Borrow Date Time")
            table_bill.heading(5, text="Return Date Time")
            table_bill.heading(6, text="Amount")


            table_bill.column(1, width=70)
            table_bill.column(2, width=100)
            table_bill.column(3, width=100)
            table_bill.column(4, width=100)
            table_bill.column(5, width=100)
            table_bill.column(6, width=80)

            table_bill.place(x=1350, y=5)

            # Button(self.window, text="Bill_Do", command=table_bill_refresher_adder).place(x=120, y=600)

            table_bill_refresher()

            # Button(self.window, text="Find_Genre", command=table_find_genra).place(x=9, y=650)

            # Button(self.window, text="Normal Book", command=table_refresher_usuall).place(x=120, y=650)

            self.window.mainloop()
        else:
            msg.showerror("Error", "Please Enter Correct Data!")


sgn = SignInView()