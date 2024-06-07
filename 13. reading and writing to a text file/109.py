print("Enter 1, 2 or 3")
num = input(" ") #string here, no int...
if num == "1": #so string here also.. ;)
    print("Enter a school subject of your choice")
    subject = input(" ") + "\n"
    file = open("Subject.txt", "w")
    file.write(subject)
    file.close()

elif num == "2":
    file = open("Subject.txt", "r")
    print(file.read())

elif num == "3":
    print("Enter a new suject to be added")
    new = input(" ")
    file = open("Subject.txt", "a")
    file.write(new + "\n")
    file.close()


else:
    print("Error, you must enter 1, 2 or 3...")








# Display the following menu to the user:
# Ask the user to enter 1, 2 or 3. If they select
# anything other than 1, 2 or 3 it should display a
# suitable error message.
# If they select 1, ask the user to enter a school
# subject and save it to a new file called
# “Subject.txt”. It should overwrite any existing file
# with a new file.
# If they select 2, display the contents of the
# “Subject.txt” file.
# If they select 3, ask the user to enter a new
# subject and save it to the file and then display
# the entire contents of the file.
# Run the program several times to test the
# options