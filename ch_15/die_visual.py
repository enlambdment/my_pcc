import pygal
from die import Die

# Create D6 die.
d6 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
	result = d6.roll()
	results.append(result)

# Analyze the results.
frequencies = []
for val in range(1, d6.num_sides + 1):
	freq = results.count(val)
	frequencies.append(freq)

# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling 1 D6 1000 times."
hist.x_labels = [str(n) for n in range(1, d6.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result" 

# Add the data series to the histogram.
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')