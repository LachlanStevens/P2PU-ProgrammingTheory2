class SteeringWheel:

  color = ""
  material = ""
  make = ""

  def turn(self, direction):
  	pass

class Engine:

  engine_number = ""
  volume = ""

  def start(self):
  	print "Started"

  def stop(self):
  	pass

class Windshield:

  thickness = ""
  area_size = ""

class Car:

  registration_number = ""
  color = ""
  steering_wheel = SteeringWheel()
  engine = Engine()
  wind_shield = Windshield()

  def __init__(self, registration_number, color):

    self.registration_number = registration_number
    self.color = color