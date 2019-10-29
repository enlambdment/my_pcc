"""A class used to represent an ice-cream stand."""

from restaurant import Restaurant

class IceCreamStand(Restaurant):
	"""
	Initialize the attributes of the parent class.
	Then initialize attributes specific to an ice cream stand.
	"""
	def __init__(self, restaurant_name, flavors_list):	
		super().__init__(restaurant_name, 'ice cream')
		self.flavors_list = flavors_list

	def ice_cream_flavors(self):
		print("\nThis ice-cream shop has the following flavors: ")
		for f in self.flavors_list:
			print("- " + f.title())
