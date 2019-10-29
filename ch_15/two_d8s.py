import pygal
from die import Die

# Create the dice.
d_1 = Die(8)
d_2 = Die(8)

# Roll the dice.
results = [d_1.roll() + d_2.roll() for j in range(5000)]

# Analyze the results.
max_val = d_1.num_sides + d_2.num_sides
frequencies = [results.count(val) for val in range(2, max_val + 1)]

# Plot the results
hist = pygal.Bar()
hist.title = "Results of rolling 2 D8s 1,000 times."
hist.x_labels = [str(j) for j in range(2, max_val + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add("D8 + D8", frequencies)
hist.render_to_file("two_d8s.svg")

