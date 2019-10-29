bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

#python lists are 0-indexed
print(bicycles[0].title())

#special python syntax to access the last element of a string:
#ask for the item at index -1
#(mnemonic: going down 1 before index 0, the count 'wraps back around')

print(bicycles[-1])

#using individual values from a list
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

names = ["Craigford","Jennothy","Mandrew"]
print("Hello, " + names[0])
print("Salutations, " + names[1])
print("Buenos dias, " + names[2])
