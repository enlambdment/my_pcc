dream_places = {}

polling_open = True

while polling_open:
	person = input("Hello! Your name, please: ")
	place = input("If you could visit any place at all, what would it be? ")

	dream_places[person] = place

	repeat = input("Any other poll-takers? (y / n) ")
	if repeat == 'n':
		polling_open = False

print("---Dream place results---")
for person, place in dream_places.items():
	print(person + " would love to visit " + place + ".")
