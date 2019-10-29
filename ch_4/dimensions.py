#tuples
#these are immutable lists

#looks like a list, except you use paren's instead of square brackets
#once defined, use an index to access an individual item, just like for lists

#looping through all values in a tuple
dimensions = (200, 50)
print("Original dimensions:")
for dim in dimensions:
	print(dim)

#if you try to change a dimension, e.g.
#dimensions[0] = 250
#gives an error -
#TypeError: 'tuple' object does not support item assignment

#writing over a tuple
#the tuple object doesn't suport re-assignment of the tuple items,
#but you *can* assign an entirely new value to a variable holding
#a tuple:
dimensions = (400, 100)
print("\nModified dimensions:")
for dim in dimensions:
	print(dim)

#use tuples when you want to store a set of values that should not
#be changed throughout the life of a program

