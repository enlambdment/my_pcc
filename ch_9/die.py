"""A class for representing a die with a given number of sides."""

from random import randint

class Die():
	"""A simple attempt to model a die with a given number of sides."""

	def __init__(self, sides=6):
		"""Initialize the die with some number of sides, or the default value thereof."""
		self.sides = sides

	def roll_die(self):
		"""Rolls the die by returning a random integer, based on the number of sides."""
		x = randint(1,self.sides)
		print(x)




