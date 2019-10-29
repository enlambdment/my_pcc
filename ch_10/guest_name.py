filename = 'guest.txt'

guest_name = input("Hello, my guest? What is your name? ")
with open(filename, 'w') as file_object:
	file_object.write(guest_name)