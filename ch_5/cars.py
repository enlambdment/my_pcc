cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper()) #because BMW is an acronym
	else:
		print(car.title())

requested_toppings = ['mushrooms', 'onions', 'pineapple']
#print('mushrooms' in requested_toppings) #this usage of in corresponds to a test, not a statement like with 'for' loop

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.x")