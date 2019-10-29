from collections import OrderedDict

programming_words = OrderedDict()

programming_words['list'] = 'an ordered sequence of values that you can individually access & edit'
programming_words['tuple'] = 'an ordered sequence of values that cannot individually be edited'
programming_words['for loop'] = 'an instruction to carry out certain actions for each item in a sequence'
programming_words['dictionary'] = 'an unordered collection of key-value pairs that you can individually access & edit'

for k, v in programming_words.items():
	print(
		"\n" + k.title() + ":\n" +
		"\t" + v)