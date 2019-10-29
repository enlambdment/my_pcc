#if-elif-else chain
#admission for anyone age < 4 is free, $0
#admission for anyone 4 <= age < 18 is $5
#admission for anyone else is $10

age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
# else:
# 	price = 5
elif age >= 65: #can also omit the 'else' block, make final condition explicit
	price = 5

print("Your admission cost is $" + str(price) + ".")

