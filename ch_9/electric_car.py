"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery():
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)

	def upgrade_battery(self):
		"""Check the battery size & set it to 85, if it isn't already."""
		if self.battery_size != 85:
			self.battery_size = 85
			print("The battery size has been upgraded!")
		else:
			print("We can't upgrade the battery any further.")

# my_battery = Battery(65)
# my_battery.describe_battery()

class ElectricCar(Car):
	"""
	Initialize attributes of the parent class.
	Then initialize attributes specific to an electric car.
	"""
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()	#right now, every electric car
									#will get a default instance
									#of the Battery class - we do
									#not let an instance of ElectricCar
									#be created with the battery_size
									#given as argument

	#overriding methods from the parent class
	def fill_gas_tank(self):
		"""Electric cars don't have gas tanks."""
		print("This car doesn't need a gas tank!")