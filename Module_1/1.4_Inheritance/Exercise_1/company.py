class Company:

	currentID = 0
	phoneNumber = 0
	isType = ""
	address = ""

	def __init__(self, recievedID):
		self.currentID = recievedID

	def print_summary(self):
		if(self.isType == "Supplier"):
			print "Type: %s" % (self.isType)
			print "Company Name: %s" % (self.companyName)
			print "Company Address: %s" % (self.address)
			print "Telephone: %s" % (self.phoneNumber)
			print "Company ID: %s" % (str(int(self.currentID) + 1))
		elif(self.isType == "Client"):
			print "Type: %s" % (self.isType)
			print "First Name: %s" % (self.firstName)
			print "Last Name: %s" % (self.lastName)
			print "Address: %s" % (self.address)
			print "Telephone: %s" % (self.phoneNumber)
			print "Customer ID: %s" % (str(int(self.currentID) + 1))
		else:
			print "No subclass specified"

class Supplier(Company):

	companyName = ""
	isType = "Supplier"

class Client(Company):

	firstName = ""
	lastName = ""
	isType = "Client"