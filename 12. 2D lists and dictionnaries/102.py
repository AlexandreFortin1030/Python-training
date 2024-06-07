
profiles = {} # had to be a dictionnary, cuz lists don't take str values as indexes, only int..

for i in range(1, 5):
    print(i,"/4 Enter name, age and shoe size")
    name = input("Name:  ")
    name = name.lower()
    age = int(input("Age:  "))
    shoe = int(input("Shoe size:  "))
    profiles[name] = {"age": age, "shoe size": shoe}  # note the way the info is refered to and therefore stored!

print(profiles)

print("Enter the name of one of the profiles")
name = input("Name:  ")
name = name.lower()

print(profiles[name])




# Ask the user to enter the name, age and shoe size for four
# people. Ask for the name of one of the people in the list and
# display their age and shoe size.