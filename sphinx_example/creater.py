# -*- coding: utf-8 -*-
"""
Module to create Person's object.
"""
from sphinx_example.items.person import Person

class Creater(object):
	"""Creater class"""

	def __init__(self, name, age):
		"""Init method of creater"""
		self.person = Person()

	def report(self):
		"""Report person's information"""
		self.person.print_info()

	def set_values(self, name, age):
		"""Function to set Person's information

		Args:
			name(str): Person's name.
			age(int): Person's age.
		"""
		self.person.name = name
		self.person.age = age



# UNIT TEST
if __name__ == '__main__':
	creater = Creater()
	creater.set_values(name='Gabriel Tessaroli', age=22)
	creater.report()

