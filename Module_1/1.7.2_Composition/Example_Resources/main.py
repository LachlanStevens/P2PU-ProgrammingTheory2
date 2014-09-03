from car import Car

def main():
	my_car = Car("1234", "blue")
	my_car.engine.engine_number = "9876"
	my_car.engine.volume = "1.6"
	my_car.steering_wheel.color = "black"
	my_car.engine.start()
	    
if(__name__ == "__main__"):
	main()