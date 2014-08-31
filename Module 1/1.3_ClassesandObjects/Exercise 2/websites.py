class Websites:

	websiteID = 0
	websiteName = ""
	websiteURL = ""

	def __init__(self, currentID):
		self.websiteID = currentID

	def setName(self, getName):
		self.websiteName = getName

	def setURL(self, getURL):
		self.websiteURL = getURL

	def getWebsiteID(self):
		return self.websiteID

	def getWebsiteName(self):
		return self.websiteName

	def getWebsiteURL(self):
		return self.websiteURL