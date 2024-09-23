import re


class Person:
	def __init__(self, name, family, password, email, number):
		self.name = name
		self.family = family
		self.password = password
		self.email = email
		self.number = number

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		#todo : Add Validator
		if re.match(r"^[a-zA-Z]{3,30}$", name):
			self._name = name

	@property
	def family(self):
		return self._family

	@family.setter
	def family(self, family):
		#todo : Add Validator
		if re.match(r"^[a-zA-Z]{3,30}$", family):
			self._family = family

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, password):
		#todo : Add Validator
		if re.match(r"^[a-zA-Z\d\s]{6,30}$", password):
			self._password = password

	@property
	def email(self):
		return self._email

	@email.setter
	def email(self, email):
		#todo : Add Validator
		if re.match(r"^[a-zA-Z][\.\_\da-zA-Z]{1,20}\@(gmail|yahoo|msn)\.com$", email, re.I):
			self._email = email

	@property
	def number(self):
		return self._number

	@number.setter
	def number(self, number):
		#todo : Add Validator
		if re.match(r"^(09|\+989)[0-9]{9}$", number):
			self._number = number

	def __repr__(self):
		return f"{self.__dict__}"
