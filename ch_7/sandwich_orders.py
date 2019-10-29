sandwich_orders = ['reuben', 'pastrami', 'croque monsieur', 'pastrami', 'BLT', 'italian sub', 'pastrami']
finished_sandwiches = []

print("Sorry! All out of pastrami for today.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	sandwich = sandwich_orders.pop(0)
	print("\nI made your " + sandwich.title() + " sandwich.")
	finished_sandwiches.append(sandwich)

print("--- Sandwich orders served today ---")
for sandwich in finished_sandwiches:
	print(sandwich)