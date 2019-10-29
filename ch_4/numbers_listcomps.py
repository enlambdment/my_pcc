#4-3

for value in range(1,21):
	print(value)

#4-4
#1 million = 10**6
# million_list = list(range(1,10**6))
# for value in million_list:
# 	print(value)

#4-5
million_list = list(range(1,10**6 + 1))
print(min(million_list))
print(max(million_list))
print(sum(million_list))

#4-10
def first_n_message(n):
	print("\nThe first " + str(n) + " items in the list are:")
	for value in million_list[:n]:
		print(value)
	print("\n")
first_n_message(3)

print("Three items from the middle of the list:")
for value in million_list[10:13]:
	print(value)
print("\n")

def last_n_message(n):
	print("\nThe last " + str(n) + " items in the list are:")
	for value in million_list[(-1 * n):]:
		print(value)
	print("\n")
last_n_message(3)

#4-6
odd_numbers = list(range(1,20,2))
for value in odd_numbers:
	print(value)
print("\n")

#4-7
triples = [value*3 for value in range(1,11)]
for val in triples:
	print(val)
print("\n")

#4-8, 4-9
cubes = [value**3 for value in range(1,11)]
for val in cubes:
	print(val)
