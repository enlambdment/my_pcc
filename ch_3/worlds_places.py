#3-8

world_places = ["Seattle", "Iceland", "Keystone", "Portland", "Netherlands"]
print(world_places)

print(sorted(world_places))

print(world_places) #order of the list is unchanged

print(sorted(world_places, reverse=True))

print(world_places)

world_places.reverse()
print(world_places) #the order is changed now

world_places.reverse()
print(world_places) #the order is changed back 

world_places.sort()
print(world_places) #order is now changed into sort order

world_places.sort(reverse=True)
print(world_places)

