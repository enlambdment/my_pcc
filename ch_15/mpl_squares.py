import matplotlib.pyplot as plt 

'''
When you give plot() a sequence of numbers, it assumes
the first data point corresponds to an x-coordinate
value of 0, but our first point corresponds to an x-value
of 1. We can *override* the default behavior by giving plot()
both the input and output values used to calculate the squares:
'''

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()