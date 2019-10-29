import pygal
from die import Die

# Create a D6 and a D10.
d6 = Die()
d10 = Die(10)

# Make some rolls, and store the results in a list.
# results = []
# for j in range(50000):
# 	result = d6.roll() + d10.roll()
# 	results.append(result)
results = [d6.roll() + d10.roll() for j in range(50000)]

# Analyze the results.
# freqs = []
# for val in range(2, d6.num_sides + d10.num_sides + 1):
# 	freq = results.count(val)
# 	freqs.append(freq)
max_val = d6.num_sides + d10.num_sides
freqs = [results.count(val) for val in range(2, max_val + 1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling 1 D6 and 1 D10"
hist.x_labels = [str(j) for j in range(2, d6.num_sides + d10.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', freqs)
hist.render_to_file('different_dice.svg')