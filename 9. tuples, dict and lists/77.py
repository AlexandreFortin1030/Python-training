list = []

print("Enter three names of friends you want to invite:  ")
pers1 = input("1/3 Enter the name here:  ")
pers2 = input("2/3 Enter the name here:  ")
pers3 = input("3/3 Enter the name here:  ")

list.append(pers1)
list.append(pers2)
list.append(pers3)

print("Do you want to invite someone else?")
choice = input("y/n:  ")
choice.lower()
while choice == "y" or choice == "yes":
    pers = input("Enter the name here:  ")
    list.append(pers)
    choice = input("Do you want to add someone else? (y/n):  ")

print(list)

name = input("Enter one of the names from the list:  ")
name = name.lower()
print(list.index(name))

print("Do you still want to invite ", name, " to the party?")
choice = input("y/n:  ")
choice.lower()

if choice == "yes" or choice == "y":
    pass
elif choice == "no" or choice == "n":
    list.remove(name)
    print(list)