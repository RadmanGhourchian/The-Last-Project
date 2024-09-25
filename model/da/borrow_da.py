import mysql.connector

from model.entity.borrow import Borrow

class BorrowDa:

	def connect(self):
		self.connection = mysql.connector.connect(host="localhost", user="root", password="r@dm@ns@r@1358", database="borrow")
		self.cursor = self.connection.cursor()

	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def save(self, bill):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("insert into bill_tbl (person, book, borrow_date_time, reutrn_date_time, amount) values (%s, %s, %s, %s, %s)",[bill.person, bill.book, bill.borrow_date_time, bill.return_date_time, bill.amount])
		self.disconnect(commit = True)

	def edit(self, bill):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("update bill_tbl set person = %s, book = %s, borrow_date_time = %s, reutrn_date_time = %s, amount = %s where id=%s",[bill.person, bill.book, bill.borrow_date_time, bill.return_date_time, bill.amount, bill.id])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from bill_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from bill_tbl ")
		bill_list = self.cursor.fetchall()
		self.disconnect()
		return bill_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from bill_tbl where id=%s", [id])
		bill = self.cursor.fetchone()
		self.disconnect()
		return bill

