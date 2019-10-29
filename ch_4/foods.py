#copying a list
#to make a copy of an existing list, take a slice where you omit both indices
#then assign that value to a variable for the new list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
for food in my_foods:
	print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(food)

#what happens if you leave out the slice syntax?
#the same output results ... except that these are just 2 names for the same list!

#to prove that we in fact have 2 separate lists:
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for food in my_foods:
	print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(food)
#if you leave out the slice syntax, my_foods and friend_foods just become variables
#that point to the same list! so both additions get appended




