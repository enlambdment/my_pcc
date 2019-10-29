file_path = '/Users/jaimepiedra/Desktop/other_files/golden_ratio.txt'
with open(file_path) as file_object:
	contents = file_object.read()
	print(contents.rstrip())