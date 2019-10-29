def count_planet(filename):
	"""
	Counts the number of times the word 'planet' appears in a file's text,
	and calculates approximate percentage of the words that are 'planet'."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist."
		print(msg)
	else:
		num_planets = contents.lower().count('planet')
		frac_planets = num_planets / len(contents.split())
		pcent_planets = round(frac_planets * 100, 2)
		print("The word 'planet' occurs " + str(num_planets) + " times in the file "
			+ filename + ", constituting approx. " + str(pcent_planets) + 
			"% of the text.")

astronomy_txts = [
	'history_of_astronomy.txt', 
	'astronomy_for_amateurs.txt',
	'astronomy_of_milton.txt']
for txt in astronomy_txts:
	count_planet(txt)