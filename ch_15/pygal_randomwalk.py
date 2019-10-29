import pygal 

from random_walk import RandomWalk

# Generate the series of x- and y-values.

while True:
	rw = RandomWalk()
	rw.fill_walk()

	# make list of points.
	rw_points = [(rw.x_values[j], rw.y_values[j]) for j in range(rw.num_points)]

	# create scatter plot: for this we will set 'stroke=False'
	rw_scatter = pygal.XY(stroke=False)
	rw_scatter.title = 'Random Walk'

	# add the data series to the scatter plot.
	rw_scatter.add('Random Walk', rw_points)

	rw_scatter.render_to_file('pygal_randomwalk.svg')

	keep_running = input("Make another random walk? (y/n): ")
	if keep_running == 'n':
		break



