#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

from copy import deepcopy
from randomid import randomID

### Data sub-object definition ###

# data structure
# used in both Node and Edge objects
# for optional parameters

class Data:
	def __init__(self, dictionary={} ):
		self.__dict__.update( deepcopy(dictionary) )
		if not self.owns('id'):
			self.id = randomID()

	def owns(self, key1, key2=None, key3=None):
		if key2 is None:
			return key1 in self.__dict__.keys()
		if key3 is None:
			return self.owns(key1) and self.owns(key2)
		return self.owns(key1) and self.owns(key2) and self.owns(key3)

	def exportDICT(self):
		me = deepcopy(self.__dict__)
		del me['id']
		return me

