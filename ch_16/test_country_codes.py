import unittest								# 1. import the unittest module
from country_codes import get_country_code	# ... and the function
											# you want to test.
'''
We wish to verify that the function returns results such as the following:

print(get_country_code('Andorra'))					# == 'ad'
print(get_country_code('United Arab Emirates'))		# == 'ae'
print(get_country_code('Afghanistan'))				# == 'af'

while also working with countries whose name isn't formatted exactly as in
the 'COUNTRIES' object, e.g.:

print(get_country_code('Venezuela, RB'))			# == 've'
'''

# 2. Create a class that inherits from unittest.TestCase, thus
# creating a *test case*. To this, you will add individual *unit tests*.
class CountryCodesTestCase(unittest.TestCase):
	"""Tests for 'country_codes.py'."""

	# 3. Write a series of methods to test different aspects of
	# your function's behavior.

	def test_country_name_in_countries(self):
		"""Do country names like 'Andorra' work?"""
		country_code = get_country_code('Andorra')
		self.assertEqual(country_code, 'ad')

	def test_country_name_not_in_countries(self):
		"""Do country names like 'Venezuela, RB' work?"""
		country_code = get_country_code('Venezuela, RB')
		self.assertEqual(country_code, 've')

unittest.main()	
# Any method that starts with 'test_' in the name will be run automatically
# when we run the file containing it.
