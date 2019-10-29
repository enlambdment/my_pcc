def print_pets(filename):
	"""Print the pet names stored in a file."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
	else:
		print(contents)

petnames_list = ['cats.txt', 'dogs.txt']
for petnames in petnames_list:
	print_pets(petnames)