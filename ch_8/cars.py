def make_car(manufacturer, model_name, **car_specs):
	"""Build a dictionary containing everything we know about a car model."""
	profile = {}
	profile['manufacturer'] = manufacturer
	profile['model_name'] = model_name

	for key, value in car_specs.items():
		profile[key] = value

	return profile

my_car = make_car('honda', 'accord',
	convertible=False,
	seats=4,
	SUV=True,
	steering_wheel='left')

print(my_car)