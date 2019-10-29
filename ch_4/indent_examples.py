magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)

#4-1

pizzas = ['margherita', 'onion',  'buffalo chicken']
for pizza in pizzas:
	print("I ate a delicious " + pizza + " pizza slice.")
print("I wonder if I can always eat pizza.")

#4-11

friend_pizzas = pizzas[:]
friend_pizzas.append('bacon avocado')

pizzas.append('pineapple')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)


#4-12

