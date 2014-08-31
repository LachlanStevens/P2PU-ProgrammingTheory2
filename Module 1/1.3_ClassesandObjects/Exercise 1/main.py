from contacts import Contacts

def main():

	i = 0
	contactNumber = {}
	j = 0
	
	firstNameArray = [
		"Christopher", 
		"Elizabeth", 
		"Emma", 
		"Aaron", 
		"Cooper", 
		"Abbey", 
		"Mackenzie", 
		"Anna", 
		"Matthew", 
		"Lily"
	]

	lastNameArray = [
		"Gottshall", 
		"Holder", 
		"Culpin", 
		"Warburton", 
		"Massina", 
		"Carlile", 
		"Hinton", 
		"Feakes", 
		"Tomkinson", 
		"Bragg"
	]
	
	phoneNumberArray = [
		"(02) 6703 3231", 
		"(02) 6724 0443", 
		"(02) 6104 7918", 
		"(03) 5358 7283", 
		"(02) 9757 7570", 
		"(02) 4707 4976", 
		"(03) 5332 0290", 
		"(07) 3575 1478", 
		"(08) 8251 6570", 
		"(03) 6269 6545"
	]

	while(i < len(firstNameArray)):
		contactNumber[i] = Contacts(i)
		contactNumber[i].setFirstName(firstNameArray[i])
		contactNumber[i].setLastName(lastNameArray[i])
		contactNumber[i].setPhoneNumber(phoneNumberArray[i])
		i += 1

	while(j < len(firstNameArray)):
		currentID = contactNumber[j].getID()
		currentFirstName = contactNumber[j].getFirstName()
		currentLastName = contactNumber[j].getLastName()
		currentPhoneNumber = contactNumber[j].getPhoneNumber()
		j += 1

		print "#%s %s %s : %s" % (str(int(currentID + 1)), currentFirstName, currentLastName, currentPhoneNumber)

if __name__ == '__main__':
	main()