#sorting a list permanently with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

#sorting a list temporariliy with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars)) #a function taking the list as an argument, not a method performed on the list

print("\nHere is the original list again:")
print(cars)

#printing a list in reverse order
print("\n")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() #reverses the original order of the list
print(cars)

#finding the length of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

#index errors
empty_cars = []
#print(empty_cars[0]) #cannot take even the 1st element, because the list is empty
#print(empty_cars[-1]) #same as above, but for last element; list is empty
