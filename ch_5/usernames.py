usernames = ['tangelo', 'yung_hemisphere', 'jcube', 'admin', 'c-jawn']
#usernames = []

#5-8
if (not usernames):
	print("We need to find some users!")
else:
	for name in usernames:
		if name == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello " + name + ", thank you for logging in again.")

new_users = ['aybaybay', 'JCuBe', 'birbmode']

#5-10
for user in new_users:	
	if user.lower() in usernames:
		print("Username taken! Please choose another username, " + user.lower())
	else:
		usernames.append(user.lower())
		print("Welcome aboard, " + usernames[-1])
print(usernames)


