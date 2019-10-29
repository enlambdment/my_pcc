def make_shirt(size='large', text='i love python'):
	"""Accepts a shirt size & shirt text, summarizing how to make the shirt."""
	print("I'll print a " + size + " shirt that says, '" + text.title() + "'.")

make_shirt('large')
make_shirt(size='medium')
make_shirt(text="torso shroudin'")