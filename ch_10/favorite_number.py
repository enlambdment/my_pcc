import json

def get_stored_fav_num():
	"""Try to return a stored favorite number."""
	filename = 'favorite_number.json'
	try:
		with open(filename) as f_obj:
			fav_num = json.load(f_obj)
	except FileNotFoundError:
		return None 
	else:
		return fav_num

def get_new_fav_num():
	"""Receive a favorite number as input & store it for next time."""
	filename = 'favorite_number.json'
	msg = "What is your favorite number? "
	fav_num = input(msg)
	with open(filename, 'w') as f_obj:
		json.dump(int(fav_num), f_obj)
		print("Okay, next time we'll remember that your favorite number was "
			+ str(fav_num) + ".")

def favorite_number():
	"""Retrieve & give back a favorite number if available, or else record one."""
	fav_num = get_stored_fav_num()
	if fav_num:
		print("I know your favorite number! It's " + str(fav_num) + ".")
	else:
		get_new_fav_num()

favorite_number()