import mysql.connector

from bill import Bill

class BillDa:

	def connect(self):
		self.connection = mysql.connector.connect(host="localhost", user="root", password="r@dm@ns@r@1358", database="bill")
		self.cursor = self.connection.cursor()

	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def save(self, bill):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("insert into bill_tbl (datte, bill_id, book_name, amount) values (%s, %s, %s, %s)",[bill.date, bill.id, bill.book_name, bill.amount	])
		self.disconnect(commit = True)

	# def edit(self, bill):
	# 	self.connect()
	# 	#todo : complete sql command and parameters
	# 	self.cursor.execute("update bill_tbl set  where id=%s",[])
	# 	self.disconnect(commit = True)

	# def remove(self, id):
	# 	self.connect()
	# 	self.cursor.execute("delete from bill_tbl where id=%s",[id])
	# 	self.disconnect(commit = True)

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
		if bill:
			return Bill(*bill)

