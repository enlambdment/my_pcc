class Employee():

	def __init__(self, first_name, last_name, salary):
		"""
		Initialize an employee with first name, last name, & annual salary.
		"""
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary

	def give_raise(self, raise_amount=5000):
		"""
		Give an employee a raise, by a specified amount. 
		Default raise is 5k, if none is given.
		"""
		self.salary += raise_amount