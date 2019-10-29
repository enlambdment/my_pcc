# python script to roll different numbers of D6's.

import pygal
from die import Die

inp_n = input("Number of dice? ")
try:
	n = int(inp_n)
except ValueError:
	print("Non-numeric input was given.")

# Create the dice.
dice = [Die() for j in range(n)]

rn_inp = input("Number of rolls? ")
try:
	roll_num = int(rn_inp)
except ValueError:
	print("Non-numeric input was given.")

# Roll the dice.
results = [ sum([d.roll() for d in dice]) for j in range(roll_num)]

# Analyze the results.
min_val = len(dice)
max_val = sum([d.num_sides for d in dice])
val_range = range(min_val, max_val + 1)
frequencies = [results.count(val) for val in val_range]

# Plot the results.
hist = pygal.Bar()
hist.title = "Results of rolling " + inp_n + " D6's " + rn_inp + " times."
hist.x_values = [str(j) for j in val_range]
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add(inp_n + " D6's", frequencies)
hist.render_to_file("n_d6s.svg")