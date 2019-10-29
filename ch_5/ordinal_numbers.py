#5-11
digits = list(range(1,10))
#print(digits)

for d in digits:
	if d == 1:
		print(str(d) + "st")
	elif d == 2:
		print(str(d) + "nd")
	elif d == 3:
		print(str(d) + "rd")
	else:
		print(str(d) + "th")