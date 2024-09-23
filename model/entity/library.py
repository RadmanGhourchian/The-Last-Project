import re
from Validator import *

class Library:
	def __init__(self, name, b_id, person_name, language, genre, In_Out):
		self.name = name
		self.b_id = b_id
		self.person_name = person_name
		self.language = language
		self.genre = genre
		self.In_Out = In_Out

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		#todo : Add Validator
		if name_validator(name):
			self._name = name

	@property
	def b_id(self):
		return self._b_id

	@b_id.setter
	def b_id(self, b_id):
		#todo : Add Validator
		if book_id(b_id):
			self._b_id = b_id

	@property
	def person_name(self):
		return self._person_name

	@person_name.setter
	def person_name(self, person_name):
		#todo : Add Validator
		if person_name_validatort(person_name):
			self._person_name = person_name

	@property
	def language(self):
		return self._language

	@language.setter
	def language(self, language):
		#todo : Add Validator
		if language_validator(language):
			self._language = language

	@property
	def genre(self):
		return self._genre

	@genre.setter
	def genre(self, genre):
		#todo : Add Validator
		if genre_validator(genre):
			self._genre = genre

	@property
	def In_Out(self):
		return self._In_Out

	@In_Out.setter
	def In_Out(self, In_Out):
		#todo : Add Validator
		self._In_Out = In_Out

	def __repr__(self):
		return f"{self.__dict__}"
