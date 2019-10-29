with open('text_files/e_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())