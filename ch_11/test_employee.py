import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests for the class Employee"""

	def setUp(self):
		"""Set up an employee instance for use in all tests."""
		self.my_employee = Employee('John', 'Smith', 60000)

	def test_give_default_raise(self):
		"""
		If not passed a value, does give_raise() give the default 5K raise?
		"""
		self.my_employee.give_raise()
		self.assertEqual(self.my_employee.salary, 65000)

	def test_give_custom_raise(self):
		"""
		If passed a value, does give_raise() give the specified raise?
		"""
		custom_raise = 2500
		self.my_employee.give_raise(custom_raise)
		self.assertEqual(self.my_employee.salary, 62500)

unittest.main()
