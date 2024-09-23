import mysql.connector

from person import Person

class PersonDa:

	def connect(self):
		self.connection = mysql.connector.connect(host="localhost", user="root", password="r@dm@ns@r@1358", database="person")
		self.cursor = self.connection.cursor()

	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def save(self, person):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("insert into person_tbl (name, family, passw, email, num) values (%s, %s, %s, %s, %s)",[person.name, person.family, person.password, person.email, person.number])
		self.disconnect(commit = True)

	def edit(self, person):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("update person_tbl set NAME=%s, FAMILY=%s, PASSW=%s, EMAIL=%s, NUM=%s where id=%s",[person.name, person.family, person.password, person.email, person.number, person.id])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from person_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from person_tbl ")
		person_list = self.cursor.fetchall()
		self.disconnect()
		return person_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from person_tbl where id=%s", [id])
		person = self.cursor.fetchone()
		self.disconnect()
		if person:
			return Person(*person)

