buffet = ('melon', 'egg', 'bacon', 'bun', 'apple')
print("At the buffet, you can eat:")
for food in buffet:
	print(food)

#this should return an error:
#buffet[2] = 'ham'

#to edit a tuple, you have to rewrite over the entire tuple:
buffet = ('melon', 'egg', 'ham', 'croissant', 'apple')
print("\nWe changed two items. At the buffet, you can eat:")
for food in buffet:
	print(food)

