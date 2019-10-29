"""A class used to represent a restaurant with a given cuisine type."""

class Restaurant():
	"""A simple attempt to model a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize restaurant name & cuisine type attributes."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Print the description of a restaurant."""
		print(
			"\nWelcome to " + self.restaurant_name.title() +
			", serving " + self.cuisine_type.title() + ".")

	def open_restaurant(self):
		"""Print a message saying the restaurant is open."""
		print(
			"\n" + self.restaurant_name.title() + " is open!")

	def set_number_served(self, number):
		self.number_served = number

	def increment_number_served(self, incr):
		self.number_served += incr




