from restaurant import Restaurant

my_restaurant = Restaurant('casa luigi', 'italian')

my_restaurant.describe_restaurant()

my_restaurant.open_restaurant()

my_restaurant.set_number_served(36)
print(my_restaurant.number_served)