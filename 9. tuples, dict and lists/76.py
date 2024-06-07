print("Enter three names of people you want to invite to your party")
pers1 = input("First person:  ")
pers2 = input("Second person:  ")
pers3 = input("Third person:  ")

list = []
list.append(pers1)
list.append(pers2)
list.append(pers3)

print("Done!")
print("Do you want to enter another?")
choice = input(" y/n:  ")
choice.lower()
while choice == "y" or choice == "yes":
    pers = input("Enter the name here:  ")
    list.append(pers)
    print(pers, "has been invited :)")
    choice = input(" Invite another person? y/n:  ")
    choice.lower()


number = len(list)
print("You have invited ", number, "people to your party")