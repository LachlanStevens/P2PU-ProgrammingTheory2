from websites import Websites

def main():

	i = 0
	currentWebsite = {}

	websiteNameArray = [
		"Google", 
		"Gizmodo", 
		"Makeuseof", 
		"Lifehacker", 
		"P2PU", 
		"GitHub", 
		"CollegeHumor", 
		"Firefox", 
		"Facebook", 
		"DigitalOcean"
	]

	URLArray = [
		"https://www.google.com.au/", 
		"http://www.gizmodo.com.au/", 
		"http://www.makeuseof.com/", 
		"http://www.lifehacker.com.au/", 
		"https://p2pu.org/en/", 
		"https://github.com/", 
		"http://www.collegehumor.com/", 
		"https://www.mozilla.org/en-US/", 
		"https://www.facebook.com/", 
		"https://www.digitalocean.com/"
	]

	while(i < len(websiteNameArray)):
		currentWebsite[i] = Websites(i)
		currentWebsite[i].setName(websiteNameArray[i])
		currentWebsite[i].setURL(URLArray[i])
		i += 1

	k = 0
	while(k < len(websiteNameArray)):
		websiteID = currentWebsite[k].getWebsiteID()
		websiteName = currentWebsite[k].getWebsiteName()
		websiteURL = currentWebsite[k].getWebsiteURL()

		print "#%s %s: %s" % (str(int(websiteID) + 1), websiteName, websiteURL)
		k += 1

if __name__ == '__main__':
	main()