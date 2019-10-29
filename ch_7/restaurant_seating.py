number = input("How many people will be dining in your group? ")

number = int(number)

if number > 8:
	print("You will have to wait to be seated.")
else:
	print("Your table is ready!")