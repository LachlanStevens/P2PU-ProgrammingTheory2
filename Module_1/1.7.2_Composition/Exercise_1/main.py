from car import *

def main():

	myCar = Car("314-AEI", "lightBlue")
	myCar.engine.engine_number = "2653"
	myCar.engine.volume = "5.8"
	myCar.steering_wheel.color = "black"
	myCar.gps.currentLocation = "979,323"
	myCar.gps.endLocation = "846,264"
	myCar.gps.softwareVersion = "3.3.8"
	myCar.engine.start()

if(__name__ == "__main__"):
	main()