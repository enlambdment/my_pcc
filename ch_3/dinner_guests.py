#3-4

dinner_guests = ["Tutankhamun","Le Petomaine","Friedrich Engels"]
print(dinner_guests[0] + ", would you join us for a light three-course meal?")
print(dinner_guests[1] + ", please be on your best behavior at dinner.")
print(dinner_guests[2] + ", you and our French guest will no doubt make polite conversation on political economy.")

#3-5

print("\n" + dinner_guests[1] + " has unfortunately blown out an intestine at his latest performance.")
dinner_guests[1] = "Karl Marx"
print(dinner_guests)
print(dinner_guests[0] + ", you need no longer fear any rude noises from any of our dinner guests.")
print(dinner_guests[1] + ", I hardly need to introduce you to " + dinner_guests[2] + "; " + dinner_guests[0] + " is an ancient friend.")
print(dinner_guests[2] + ", you and our German guest will no doubt make polite conversation on political economy.")

#3-6

alex = "Alexander the Great"
ivan = "Ivan the Terrible"
adam = "Adam"

print("\nI am pleased to inform everyone that I've located more ample seating.")
dinner_guests.insert(0, alex)
print(dinner_guests)
dinner_guests.insert(2, ivan)
print(dinner_guests)
dinner_guests.append(adam)
print(dinner_guests)
print(dinner_guests[0] + ", there is nothing left here for you to conquer except the breadsticks.")
print(dinner_guests[2] + ", it's too bad they only have the '86 vintage, but do try to be more agreeable.")
print(dinner_guests[5] + ", you're probably the oldest friend among everyone here.")

#3-7

print("\nThe movers who were bringing the new dinner table got jugged for it, I'm afraid.")
print("\nI can only invite 2 people now. I cannot invite all " + str(len(dinner_guests)) + " people.")
popped = dinner_guests.pop()
print("Sorry, " + popped + "!")
popped = dinner_guests.pop()
print("Too bad, " + popped + ".")
popped = dinner_guests.pop()
print("Mille regrets, " + popped + "!")
popped = dinner_guests.pop()
print("Better luck next time, " + popped + "...")
print("\nI will invite these " + str(len(dinner_guests)) + " guests to dinner.")
print(dinner_guests[0] + ", I never got to dine with a conqueror before.")
print(dinner_guests[-1] + ", how long did it take for them to wrap you up like that?")

del dinner_guests[0]
del dinner_guests[-1] #by now, -1'th element is the same as the 0'th since there's only one left
print(dinner_guests)