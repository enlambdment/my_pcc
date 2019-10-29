from ice_cream_stand import IceCreamStand

my_icecreamstand = IceCreamStand(
	'cones n stuff', 
	('vanilla', 'chocolate', 'banana'))

print(my_icecreamstand.restaurant_name)
print(my_icecreamstand.cuisine_type)	#does it work?

my_icecreamstand.describe_restaurant()
my_icecreamstand.ice_cream_flavors()