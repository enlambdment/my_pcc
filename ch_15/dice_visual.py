import pygal
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
	freq = results.count(value)
	frequencies.append(freq)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling 2 D6's 1000 times."
hist.x_labels = [str(n) for n in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("2 D6's", frequencies)
hist.render_to_file('dice_visual.svg')

