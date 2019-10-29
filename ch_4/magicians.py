#python's 'for' loop

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title())

#doing more work within a 'for' loop

x = 0
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	x = x + 1
	print("How about " + magicians[x % len(magicians)].title() + "'s trick?")

#usually after a 'for' loop concludes, you somehow want to summarize a block of output
# or move on to something else.

#any lines of code after the 'for' loop that are not indented are executed once without repetition.

for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")

print ("Thank you everyone. That was a great magic show!")
