def getExponent(num, exponent):
	answer = pow(num, exponent) 
	return answer

def main():
	num = int(raw_input("Enter in a number: ")) 
	exponent = int(raw_input("Raise the number to the power of: "))

	print "Answer: %d" % (getExponent(num, exponent))

if(__name__ == "__main__"):
	main()