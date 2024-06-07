

list = [[2,6,9],[1,3,5],[7,5,9],[1,2,8]]

row = int(input("Which row do you want to display:  "))

print(list[row])

col = int(input("Now wich column from that row do you want to display:  "))

print(list[row][col])

print("Do you want to change this value?")
choice = input("y/n:   ")
choice.lower()
if choice == "yes" or choice == "y":
    value = int(input("Enter new value:  "))
    list[row][col] = value
    print(list[row])
elif choice == "n" or choice == "no":
    print("Ok. bye")
else:
    print("Answer with y or n please. Try again")







# Change your previous program
# to ask the user which row they
# want displayed. Display that
# row. Ask which column in that
# row they want displayed and
# display the value that is held
# there. Ask the user if they want
# to change the value. If they do,
# ask for a new value and change
# the data. Finally, display the
# whole row again.