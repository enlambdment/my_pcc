#dictionaries

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#working with dictionaries
#a dictionary is a collection of key-value pairs
#each key is connected to a value; you can use the key to access the value associated with it
#any object that you can create in python can be used as a value in a dictionary

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!\n")

#adding new key-value pairs
#dictionaries are dynamic structures: new key-value pairs can be added
#at any time.

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#python doesn't care about the order in which key-value pairs are stored;
#so they need not be displayed in the same order as they were entered in.

#starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#modifying values in a dictionary
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".\n")

###
###
###

#tracking the position of an alien that can move at different speeds
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']) + "\n")

#Move the alien to the right.
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

#The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']) + "\n")

#removing key-value pairs
#all that a del statement needs is the name of the dictionary & the key that you want to remove
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

#nesting
#sometimes you want to store a set of dictionaries in a list, 
#or store a list of items as a value in a dictionary.
#there are many kinds of nesting to choose from, e.g.:

#nesting dictionaries within a list
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens_list = [alien_0, alien_1, alien_2]

for alien in aliens_list:
	print(alien)
print("\n")

#a more realistic example: appending together a list of automatically generated aliens,
#all patterned after the same alien_0 type:

#empty list for storing aliens
aliens = []

#make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

#this time, edit the first 3 aliens in the list
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

#show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

#show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))
print("\n")
#can i cycle through each of the 3 alien types exactly once?
#*can't* do this by name, because once you create the list 'aliens',
#the list stores the values themselves, without the labels having 
#anything to do with it.
# aliens_cycle = []

# for number in range(30):
# 	aliens_cycle.append(aliens[number % 3])

# #show the first 6 aliens.
# for alien in aliens_cycle[:6]:
# 	print(alien)
# print("...")

# #show how many aliens have been created
# print("Total number of aliens: " + str(len(aliens_cycle)))

#a list in a dictionary
#store information about a pizza being ordered. 
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

#summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
	"with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

