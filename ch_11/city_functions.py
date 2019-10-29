def city_country(city, country, population=''):
	"""Returns a formatted city & country address."""
	if population:
		address = city + ', ' + country + ' - population ' + str(population)
	else:
		address = city + ', ' + country
	return address.title()