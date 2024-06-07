profiles = {} # had to be a dictionnary, cuz lists don't take str values as indexes, only int..

for i in range(1, 3):
    print(i,"/4 Enter name, age and shoe size")
    name = input("Name:  ")
    name = name.lower()
    age = int(input("Age:  "))
    shoe = int(input("Shoe size:  "))
    profiles[name] = {"age": age, "shoe size": shoe}  # note the way the info is refered to and therefore stored!

print(profiles)

print("Choose a person you want to remove from the list")
person = input("Enter the name here:   ")

del profiles[person]

print(profiles)








# After gathering the four names, ages and shoe sizes, ask the
# user to enter the name of the person they want to remove from
# the list. Delete this row from the data and display the other rows
# on separate lines.