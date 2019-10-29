import unittest
from city_functions import city_country

class AddressesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""
	def test_city_country(self):
		"""Do addresses like 'Santiago, Chile' work?"""
		formatted_address = city_country('santiago', 'chile')
		self.assertEqual(formatted_address, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Do addresses like 'Santiago, Chile - population 5000000' work?"""
		formatted_address = city_country(
			'santiago', 'chile', '5000000')
		self.assertEqual(formatted_address, 
			'Santiago, Chile - Population 5000000')

unittest.main()

