prompt = "Need a ticket price? I'll tell you: just give me the patron's age: " + "\n(Say 'quit' to exit any time.) "

#this loop has no exit condition:
while True:
	age = input(prompt)

	if age == 'quit':
		break

	age = int(age)
	if age < 3:
		print("Free entry for patrons under three!\n")
	elif age < 12:
		print("Ten dollars, please.\n")
	else:
		print("Fifteen dollars, please.\n")