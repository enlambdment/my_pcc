number = input("I will tell you if your number is a multiple of 10 or not.\nGive me a number: ")
number = int(number)
if number % 10 == 0:
	print("Yep, that's a multiple of 10!")
else:
	print("Nope - not a multiple of 10.")