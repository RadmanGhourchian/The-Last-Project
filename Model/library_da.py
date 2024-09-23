import mysql.connector

from library import Library

class LibraryDa:

	def connect(self):
		self.connection = mysql.connector.connect(host="localhost", user="root", password="r@dm@ns@r@1358", database="library_bookshelf")
		self.cursor = self.connection.cursor()

	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def save(self, library):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("insert into library_tbl (name, b_id, person_name, lang, genre, In_Out) values (%s, %s, %s, %s, %s, %s)",[library.name, library.b_id, library.person_name, library.language, library.genre, library.In_Out])
		self.disconnect(commit = True)

	def edit(self, library):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("update library_tbl set person_name = %s where id=%s",[library.person_name, library.id])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from library_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from library_tbl ")
		library_list = self.cursor.fetchall()
		self.disconnect()
		return library_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from library_tbl where id=%s", [id])
		library = self.cursor.fetchone()
		self.disconnect()
		if library:
			return Library(*library)
	def find_by_genre(self, genre):
		self.connect()
		self.cursor.execute("select * from library_tbl where genre=%s", [genre])
		library = self.cursor.fetchall()
		self.disconnect()
		return library

