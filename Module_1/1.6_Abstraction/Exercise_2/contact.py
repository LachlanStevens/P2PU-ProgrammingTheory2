from abc import ABCMeta, abstractmethod

class contact:

	__metaclass__ = ABCMeta

	currentID = 0
	phoneNumber = 0
	isType = ""
	address = ""

	def __init__(self, recievedID):
		self.currentID = recievedID

	@abstractmethod
	def printSummary():
		pass

class CompanyContact(contact):

	companyName = ""

	def printSummary(self):
		print "Type: %s" % ("Company")
		print "Company Name: %s" % (self.companyName)
		print "Company Address: %s" % (self.address)
		print "Telephone: %s" % (self.phoneNumber)
		print "Company ID: %s" % (str(int(self.currentID) + 1))

class IndividualContact(contact):

	firstName = ""
	lastName = ""

	def printSummary(self):
		print "Type: %s" % (self.isType)
		print "First Name: %s" % (self.firstName)
		print "Last Name: %s" % (self.lastName)
		print "Address: %s" % (self.address)
		print "Telephone: %s" % (self.phoneNumber)
		print "Customer ID: %s" % (str(int(self.currentID) + 1))