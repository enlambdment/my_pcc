filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

learning_haskell = ''
for line in lines:
	learning_haskell += line.replace('Python', 'Haskell')
print(learning_haskell)