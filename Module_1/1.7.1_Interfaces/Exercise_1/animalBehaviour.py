from abc import ABCMeta, abstractmethod

class animalBehaviour:

	__metaclass__ = ABCMeta

	def talk(self):
		raise NotImplementedError()

	def move(self):
		raise NotImplementedError()

	def breathe(self):
		raise NotImplementedError()