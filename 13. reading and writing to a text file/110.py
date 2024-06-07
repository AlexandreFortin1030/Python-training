file = open("Names.txt", "r")
print(file.read())
file.close()
print("Choose a name in the previous list")
name = input("Enter the name here :  ")
name = name + "\n"

file = open("Names.txt", "r")

for row in file:
    if row == name:
        pass
    else:
        newfile = open("Names2.txt", "a")
        newfile.write(row)
        newfile.close()

        






















# Using the Names.txt file you
# created earlier, display the list of
# names in Python. Ask the user to
# type in one of the names and then
# save all the names except the one
# they entered into a new file called
# Names2.txt.