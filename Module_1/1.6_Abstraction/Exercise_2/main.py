from contact import *

def main():

	currentCompany = {}
	currentClient = {}

	companyArray = [
		"AMP LIMITED,(07) 5313 8878,84 Boland Drive", 
		"AUSTRALIA AND NEW ZEALAND BANKING GROUP LIMITED,(07) 4070 1615,78 Creedon Street", 
		"BHP BILLITON LIMITED,(07) 4599 1986,65 Cassinia Street", 
		"BRAMBLES LIMITED,(07) 3526 6840,12 Derry Street", 
		"COMMONWEALTH BANK OF AUSTRALIA,(02) 6749 7668,41 Ocean Pde", 
		"CSL LIMITED,(02) 6192 8301,87 Pipeclay Road", 
		"INSURANCE AUSTRALIA GROUP LIMITED,(02) 4974 8386,27 Peterho Boulevard", 
		"MACQUARIE GROUP LIMITED,(02) 6704 6190,32 Roseda-Tinamba Road", 
		"NATIONAL AUSTRALIA BANK LIMITED,(08) 9317 2930,10 Hill Street", 
		"ORIGIN ENERGY LIMITED,(02) 6777 3123,73 Fitzroy Street"
	]

	clientArray = [
		"Christopher,Gottshall,(02) 6703 3231 2087,24 Goebels Road", 
		"Elizabeth,Holder,(02) 6724 0443,76 Whitehaven Crescent", 
		"Emma,Culpin,(02) 6104 7918,49 McRock Street", 
		"Aaron,Warburton,(03) 5358 7283,84 Chapman Avenue", 
		"Cooper,Massina,(02) 9757 7570,64 Hunter Street", 
		"Abbey,Carlile,(02) 4707 4976,93 Masthead Drive", 
		"Mackenzie,Hinton,(03) 5332 0290,88 Norton Street", 
		"Anna,Feakes,(07) 3575 1478,66 Baker Street", 
		"Matthew,Tomkinson,(08) 8251 6570,52 Argyle Street", 
		"Lily,Bragg,(03) 6269 6545,57 Peterho Boulevard"
	]

	i = 0
	while(i < len(companyArray)):
		
		currentLine = companyArray[i].split(',')

		currentCompany[i] = CompanyContact(i)
		currentCompany[i].companyName = currentLine[0]
		currentCompany[i].phoneNumber = currentLine[1]
		currentCompany[i].address = currentLine[2]

		i += 1

	l = 0
	while(l < len(clientArray)):

		currentLine = clientArray[l].split(',')

		currentClient[l] = IndividualContact(l)
		currentClient[l].firstName = currentLine[0]
		currentClient[l].lastName = currentLine[1]
		currentClient[l].phoneNumber = currentLine[2]
		currentClient[l].address = currentLine[3]

		l += 1

	print "-----------"
	print "|COMPANIES|"
	print "-----------"
	print ""
	i = 0
	while(i < len(companyArray)):

		currentCompany[i].printSummary()
		print ""
		
		i += 1

	print "---------"
	print "|CLIENTS|"
	print "---------"
	print ""
	l = 0
	while(l < len(clientArray)):

		currentClient[l].printSummary()
		print ""

		l += 1

if __name__ == '__main__':
	main()