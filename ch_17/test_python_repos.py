import unittest
import requests

# you should really just be making one request & then
# checking out things about it, as you go. I think?

# (What would be even better is if the main 'python_repos.py'
# file simply contained a function / method that gave as output
# the objects we want to test. ... but then we couldn't do too
# many tests, re-running the function / method each time, since
# we could get rate-limited.)

# SOLUTION: use setUp() method! - see Ch. 11, p. 227
# *come back to this & refactor code accordingly*

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()

class PythonReposTestCase(unittest.TestCase):
	"""Tests for 'python_repos.py'."""

	def test_get_request_successful(self):
		"""Was the request be successful?"""
		self.assertEqual(r.status_code, 200)

	# def test_get_request_complete(self):
	# 	"""Was the request complete?"""
	# 	self.assertFalse(response_dict['incomplete_results'])

	def test_number_of_items(self):
		"""Did the expected number of results come back?"""
		self.assertEqual(len(response_dict['items']), 30)

	def test_total_count(self):
		"""Is the total count reasonably high?"""
		self.assertGreater(response_dict['total_count'], 
			4000000)

unittest.main()