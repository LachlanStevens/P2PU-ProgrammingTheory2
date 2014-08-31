class Contacts:

	contactID = 0
	firstName = ""
	lastName = ""
	phoneNumber = 0


	def __init__(self, currentID):
		self.contactID = currentID

	def setFirstName(self, getFirstName):
		self.firstName = getFirstName

	def setLastName(self, getLastName):
		self.lastName = getLastName

	def setPhoneNumber(self, getPhoneNumber):
		self.phoneNumber = getPhoneNumber

	def getID(self):
		return self.contactID

	def getFirstName(self):
		return self.firstName

	def getLastName(self):
		return self.lastName

	def getPhoneNumber(self):
		return self.phoneNumber