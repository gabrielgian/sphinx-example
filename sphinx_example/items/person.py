# -*- coding: utf-8 -*-
"""
**Person** module will handle its item definition and
useful methods.

@author: Gabriel
"""

class Person(object):
	"""Person class
	
	This is the person class.
	"""
	
	def __init__(self, name, age):
		"""Init method of *Person* class.
		
		Args:
			name(str): Person's name.
			age(int): Person's age.
		"""
		self.name = name
		self.age = age

	def print_info(self):
		"""Print *Person* information."""
		print self.name, self.age

