count = 0
name = input("Enter the name of someone to invite:  ")
print(name, " has been invited to the party :)")
count = count +1
invite = input("Do you want to invite someone else? (y/n):  ")
invite = invite.lower()

if invite == "yes" or invite == "y":

    while invite == "yes" or invite == "y":

        name = input("Enter the name of the person:  ")
        print(name, " has been invited too :)")
        count = count + 1
        invite = input("Do you want to invite someone else? (y/n):  ")
        invite = invite.lower()

    print("You have", count, "guests coming to the party!")

else:
    
    print("You have", count, "guest(s) coming to the party!")

