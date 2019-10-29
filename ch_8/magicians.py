magicians = ['bozo', 'harriet houdini', 'disappear-o']

def make_great(magicians):
	greats = []
	for m in magicians:
		m = m + " the Great"
		greats.append(m)
	return greats
#?
def show_magicians(magicians):
	for m in magicians:
		print(m.title() + "\n")

great_magicians = make_great(magicians)

show_magicians(magicians)
show_magicians(great_magicians)