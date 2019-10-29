filename = 'guest_book.txt'

prompt = "\nHello, my guest! What is your name? "
prompt += "\nEnter 'quit' to end the program. "

guest_name = ""
with open(filename, 'a') as file_object:
	while guest_name != 'quit':
		guest_name = input(prompt)
		if guest_name != 'quit':
			print("Thanks, " + guest_name + "! I'll write it in the guest book.")
			file_object.write(guest_name + "\n")
