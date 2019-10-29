#making numerical lists

#using the 'range()' function

for value in range(1,5):
	print(value)

#*note* how this only prints from the 1st number to the penultimate number;
#the range() function stops when it reaches the 2nd value provided

#so, for example:
def count_from_1_through_n(n):
	for value in range(1,n+1):
		print(value)

count_from_1_through_n(6)

#using range() to make a list of numbers
numbers = list(range(1,6))
print(numbers)

#can also tell python to skip numbers in a given range
even_numbers = list(range(2,11,2))
print(even_numbers)
#this should have the same output as the previous even_numbers
even_numbers_2 = list(range(2,12,2))
print(even_numbers)

#putting the first 10 square numbers into a list:
squares = []
for value in range(1,11):
	squares.append(value ** 2)

print(squares)

#simple statistics with a list of numbers
#a few python functions are specific to lists of numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehensions
#the following uses a list comprehension to create a list
#of the first 10 squares, in just 1 line:
squares = [value**2 for value in range(1,11)]
print(squares)