import matplotlib.pyplot as plt

# '''
# To plot a single point, use the scatter() function.
# Pass the single (x, y) values of the point of interest
# to scatter(), and it should plot those values:
# '''

# plt.scatter(2, 4, s=200)	# s argument sets the size of the dots
# 							# used to draw the graph.

# '''
# To plot a series of points, we can pass scatter() separate
# lists of x- and y-values, like this:
# '''
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.scatter(x_values, y_values, s=100)

'''
Writing out lists by hand can be inefficient, esp. when we have many
points. Rather than passing our points in a list, let's use a *loop* in 
Python to do the calculations for us. Here's how this would look with 1000
pts:
'''
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
'''
1. range goes *from* the 1st param, inclusive, *to* the 2nd param,
   *exclusive*;
2. then, list takes the range & turns it into a list.
'''

# To change the color of the points, pass c to scatter() with
# c the name of a color to use. 
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)

# You can also define custom color using RGB color model e.g.
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)

'''
A colormap is a series of colors in a gradient that moves from a starting
to ending color. Used in visualizations to emphasize a pattern in the data 
e.g. low values - lighter color, high - darker.
pyplot module includes some built-in colormaps. Need to specify how pyplot
should assign a color to each pt in the data set, to use a colormap. e.g. 
Here's how to assign each pt a color based on its y-value:
'''
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
	edgecolor='none', s=40)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

# plt.show()
'''
If you want your program to automatically sace the plot to a file,
you can replace the call to plt.show() with a call to plt.savefig():
'''
plt.savefig('squares_plot.png', bbox_inches='tight')
# 1st arg: filename for the plot image, which will be saved in same
# directory as scatter_squares.py the python file.
# 2nd arg: trims extra whitespaces from the plot. Omit this arg if 
# you want the extra whitespace.


