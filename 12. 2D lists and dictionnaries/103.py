
profiles = {} # had to be a dictionnary, cuz lists don't take str values as indexes, only int..

for i in range(1, 2):
    print(i,"/4 Enter name, age and shoe size")
    name = input("Name:  ")
    name = name.lower()
    age = int(input("Age:  "))
    shoe = int(input("Shoe size:  "))
    profiles[name] = {"age": age, "shoe size": shoe}  # note the way the info is refered to and therefore stored!


print("ok c'est partit...")

for profile in profiles:
    print(name)
    print(age)







# Adapt program 102
# to display the
# names and ages of
# all the people in
# the list but do not
# show their shoe
# size.