file = open("Names.txt", "r")
print(file.read())

name = input("Enter a name to add:  ")

file = open("Names.txt", "a")
file.write(name)
file.close()

file = open("Names.txt", "r")
print(file.read())













# Open the Names.txt file. Ask the user to input a
# new name. Add this to the end of the file and
# display the entire file.