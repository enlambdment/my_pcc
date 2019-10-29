from die import Die 

cube = Die() #default val of sides is 6

# print(cube.sides)

#roll the die 'cube' 10 times
for i in range(0, 10):
	cube.roll_die()