import matplotlib.pyplot as plt

from die import Die

# Create 1 D6.
die = Die()

# Roll 1 D6s 5000 times to generate results.
results = [die.roll() for j in range(5000)]

# Analyze results.
min_val = 1
max_val = die.num_sides
val_range = range(min_val, max_val + 1)
frequencies = [results.count(val) for val in val_range]

# Plot results using matplotlib.pyplot.
x_values = list(val_range)
y_values = frequencies

plt.scatter(x_values, y_values, s = 100)

# Set chart title and label axes.
plt.title("Results of rolling 1 D6 5000 times", fontsize=24)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of result", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()