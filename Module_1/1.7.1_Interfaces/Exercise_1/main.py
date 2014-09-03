from animals import *

def main():
	animals = [
	    Bird("Polly", "sky"),
	    Dog("Roger", "ground"),
	    Whale("Moby", "sea")
	]
	for animal in animals:
	    animal.talk()
	    animal.move()
	    animal.breathe()
	    
if(__name__ == "__main__"):
	main()