import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	filename = 'username.json'
	username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		answer = ""
		while answer != 'Y' and answer != 'N':
			msg = "Hello, am I speaking with " + username + " today?\n"
			msg += "Please answer 'Y' or 'N'.\n"
			answer = input(msg)
			if answer != 'Y' and answer != 'N':
				print("Sorry, I didn't understand that response.")
		if answer == 'Y':	
			print("Welcome back, " + username + "!")
		else:
			username = get_new_username()
			print("We'll remember you when you come back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")

greet_user()

