prompt = "Give me two numbers, and I'll add them."

while True:
	first_number = input("First number: ")
	second_number = input("Second number: ")
	try:
		result = int(first_number) + int(second_number)
	except ValueError:
		msg = "Sorry, one of the values you provided wasn't a number."
		print(msg)
	else:
		print(result)
