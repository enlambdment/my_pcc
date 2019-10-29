#6-1
person_info = {
	'first_name': 'Craigford',
	'last_name': 'Agassiz',
	'age': 55,
	'city': 'Walla Walla',
}

for key, value in person_info.items(): #items() method returns list of key-value pairs
	print("\n" + key.title() + ": " + str(value).title())

#6-2
favorite_numbers = {
	'jennison': 38,
	'amerigo': 6,
	'zaider': 57,
	'evelina': 345,
}

for key, value in favorite_numbers.items():
	print("\n" + key.title() + "'s favorite number is: " + str(value))

#6-3, 6-4
programming_words = {
	'list': 'an ordered sequence of values that you can individually access & edit',
	'tuple': 'an ordered sequence of values that cannot individually be edited',
	'for loop': 'an instruction to carry out certain actions for each item in a sequence',
	'dictionary': 'an unordered collection of key-value pairs that you can individually access & edit',
}

for k, v in programming_words.items():
	print(
		"\n" + k.title() + ":\n" +
		"\t" + v)


#6-5
rivers = {
	'nile': 'egypt',
	'yangtze': 'china',
	'itapocu': 'brazil',
}

for k, v in rivers.items():
	print("The " + k.title() + " runs through " + v.title() + ".")
print("\n")

print("Rivers in the dictionary:")
for k in rivers: #or rivers.keys() to be explicit
	print(k.title())
print("\n")

print("Countries in the dictionary:")
for v in rivers.values():
	print(v.title())
