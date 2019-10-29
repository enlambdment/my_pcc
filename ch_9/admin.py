"""A set of classes to represent an admin & the privileges they can have."""

from user import User 

class Privileges():
	"""A simple attempt to model a set of privileges."""

	def __init__(self, privileges):
		"""Initialize the privileges' attributes."""
		self.privileges = privileges

	def show_privileges(self):
		"""Print out the privileges contained in the list."""
		for privilege in self.privileges:
			print("- " + privilege)

class Admin(User):

	def __init__(self, first_name, last_name, privileges):
		"""
		Initialize attributes of the parent class. 
		We're going to suppose that an admin is always a paying, verified member.
		Then initialize attributes of the child class.
		"""
		super().__init__(first_name, last_name, True, True)
		self.privileges = privileges
			#! name the instance of the class passed to 
			#! parameters 'privileges': DON'T create
			#! a new instance by passing 'privileges' 
			#! as argument (which is nonsensical)