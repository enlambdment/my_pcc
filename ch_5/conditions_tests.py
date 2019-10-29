car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#number examples
ints_1_to_30 = list(range(0,31))
for val in ints_1_to_30:
	if (val % 2 != 0) or (val % 3 != 0):
		print("Is " + str(val) + " divisible by 6? I predict False.")
	else:
		print("Is " + str(val) + " divisible by 6? I predict True.")
	print(val % 6 == 0)