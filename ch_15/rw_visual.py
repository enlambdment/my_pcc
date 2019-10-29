import matplotlib.pyplot as plt 

from random_walk import RandomWalk 

while True:
	rw = RandomWalk(50000)
	rw.fill_walk()

	point_numbers = list(range(rw.num_points))

	# Fill in the whole series of dots on the screen.
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		edgecolor='none', s=1)

	# Mark the starting dot green.
	plt.scatter(0, 0, c='green', edgecolors='none', s=100)

	# Mark the ending dot red.
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

	# Remove the axes.
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another random walk? (y/n): ")
	if keep_running == 'n':
		break

