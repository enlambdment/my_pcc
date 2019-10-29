prompt = "Give me some tasty toppings to put on your pizza!\n(Say 'quit' to stop any time.) "

while True:
	topping = input(prompt)
	if topping == 'quit':
		break
	else:
		print("Putting some delicious " + topping.lower() + " on that pizza!")
