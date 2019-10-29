filename = 'learning_python.txt'

with open(filename) as file_object:
	contents = file_object.read()
	print(contents)

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

with open(filename) as file_object:
	lines = file_object.readlines()

lessons = ''
for line in lines:
	lessons += line
print(lessons)
