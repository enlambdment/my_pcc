#working with part of a list

#in python, parts of a list are called 'slices'

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3]) #prints the list of the first 3 players on the list
print(players[1:4])
print(players[:4])
print(players[1:])
print(players[-2:])
print(players[-2:-4]) #returns an empty list because there are no elements
						#in order going *from* the 2nd to last, *to* the 4th to last
print(players[-4:-2]) #returns 4th from end, 3rd from end - excludes the final index

#looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())
