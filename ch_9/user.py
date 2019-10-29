"""A class to represent a user."""

class User():	
	"""A simple attempt to model a user."""

	def __init__(self, first_name, last_name, is_paying, is_verified):
		"""Initialize first & last names, along with other attributes."""
		self.first_name = first_name
		self.last_name = last_name
		self.is_paying = is_paying
		self.is_verified = is_verified
		self.login_attempts = 0

	def describe_user(self):
		"""Print a description summary of the user."""
		print(
			"\nUser info summary for " + self.first_name.title() 
			+ ' ' + self.last_name.title() + ': ')

		print("Paying member? " + str(self.is_paying))

		print("Verified member? " + str(self.is_verified))

	def greet_user(self):
		"""Print a greeting for the user."""
		print(
			'\nHello there, ' + self.first_name.title() 
			+ ' ' + self.last_name.title() + '!')

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0










