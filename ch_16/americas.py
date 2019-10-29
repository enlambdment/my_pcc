from pygal.maps.world import World

wm = World()	# make an instance of the World class
wm.title = 'North, Central, and South America'	# set the map's 'title' attrib.

# each call to 'add' sets up a new color for the set of countries
# that it is invoked on, and adds that color to a key on the left of the graph.
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 
	'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')