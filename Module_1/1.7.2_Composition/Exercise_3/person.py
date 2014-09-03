from abc import ABCMeta, abstractmethod

class Person:

	__metaclass__ = ABCMeta

	@abstractmethod
	def add(name):
		pass

	@abstractmethod
	def remove(index):
		pass

	@abstractmethod
	def list():
		pass

	@abstractmethod
	def talk(text):
		pass

	@abstractmethod
	def move(location):
		pass