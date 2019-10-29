#example with positional arguments: must be given in same order as parameters

#you can give any parameter a default value:
#! for some reason, default parameters have to come last in
#! the list of parameters. it's so that python can continue
#! interpreting positional arguments correctly.
def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + " is called " + pet_name.title() + "!")

#you can instead use keyword arguments in what you pass to the function:
describe_pet(animal_type='hamster', pet_name='harry')

#this way, it will not matter what order the arguments are given in,
#unlike with positional arguments:
describe_pet(pet_name='willie', animal_type='dog')

describe_pet(pet_name='bubby')
