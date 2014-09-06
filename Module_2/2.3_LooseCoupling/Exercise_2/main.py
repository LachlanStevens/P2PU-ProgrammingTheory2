def concatenate(string1, string2):
	full_string = "%s %s" % (string1, string2) 
	return full_string

def main():
	string1 = raw_input("Enter in a string: ") 
	string2 = raw_input("Enter another string: ") 

	print "Answer: %s" % (concatenate(string1,string2))

if(__name__ == "__main__"):
	main()