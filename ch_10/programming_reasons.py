filename = 'reasons.txt'

prompt = "\nWhy do you enjoy programming?"
prompt += "\nPress 'q' to quit any time. "

with open(filename, 'a') as file_object:
	reason = ""
	while reason != 'q':
		reason = input(prompt)
		if reason != 'q':
			file_object.write(reason + "\n")