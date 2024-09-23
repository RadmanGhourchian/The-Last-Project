from Bill_Validator import *

class Bill:
	def __init__(self, date, id, book_name, amount):
		self.date = date
		self.id = id
		self.book_name = book_name
		self.amount = amount

	@property
	def date(self):
		return self._date

	@date.setter
	def date(self, date):
		#todo : Add Validator
		self._date = date

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		#todo : Add Validator
		if id_validator(id):
			self._id = id

	@property
	def book_name(self):
		return self._book_name

	@book_name.setter
	def book_name(self, book_name):
		#todo : Add Validator
		if book_name_validator(book_name):
			self._book_name = book_name
	@property
	def amount(self):
		return self._amount

	@amount.setter
	def amount(self, amount):
		if amount_validator(amount):
			self._amount = amount

	def __repr__(self):
		return f"{self.__dict__}"
