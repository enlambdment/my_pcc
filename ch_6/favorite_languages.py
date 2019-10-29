#a dictionary of similar objects
#instead of storing different kinds of information about one object,
#you can also store one kind of information about many objects, 
#with one key per object.
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],	#good practice to include a comma after the last k-v pair
	}

print(favorite_languages)

def suffix(n):
	if n > 1:
		return "s"	
	else:
		return ""

def copula(n):
	if n > 1:
		return "are"
	else:
		return "is"

#if the helper functions have 'return's included, as mentioned above,
#then it seems to make no difference whether the values with l input are 
#wrapped with str() or not.
for name, languages in favorite_languages.items():
	l = len(languages)
	print("\n" + name.title() + "'s favorite language" + suffix(l) + " " + copula(l) + ":")
	for lang in languages:
		print("\t" + lang.title())


#a dictionary in a dictionary
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())


