#testing multiple conditions
#using multiple lists

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['olives', 'french fries']

if requested_toppings:
	for topping in requested_toppings:
		if topping in available_toppings:
			print("Adding " + topping + ".")
		else:
			print("Sorry, we don't have " + topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

