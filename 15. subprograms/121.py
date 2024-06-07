list = []
print("#####--- Welcome in the list manager ---#####")
# Subprograms

def menu():
    print("-------- Menu --------")

    print("1. Add a name to the list")
    print("2. Change a name from the list")
    print("3. Delete a name from the list")
    print("4. View all names in the list")
    print("5. Quit program")
    choice = input(" Enter a number:  ")
    return choice
    

def option1():
    print("Add a name to the list")
    name = input("  ")
    list.append(name)
    welcome = False
    return welcome
    

def option2():
    print("Change a name from the list")
    for row in list:
        index = list.index(row)
        print(str(index) + ": " + row)
    print("Enter the index of the name you want to change")
    oldname = int(input("  "))
    print("Changing name: ", list[oldname])
    newname = input("Enter new name here:  ")
    list[oldname] = newname
    print("New name has been saved !")
    print(list)
    


def option3():
    print("Delete a name from the list")
    for row in list:
        index = list.index(row)
        print(str(index) + ": " + row)
    print("Enter the index of the name you want to delete")
    oldname = int(input("  "))
    deleted = list[oldname]
    del list[oldname]
    print(deleted," has been deleted from the list")
    print(list)
    


def option4():
    print("View all names in the list")
    for row in list:
        print(row)


# Main function

def main():
    choice = menu()
    if choice == 1 or choice == "1":
        option1()
        main()
    elif choice == 2 or choice == "2":
        option2()
        main()
    elif choice == 3 or choice == "3":
        option3()
        main()
    elif choice == 4 or choice == "4":
        option4()
        main()
    elif choice == 5 or choice == "5":
        print("At your service, see you soon :)")
    else:
        print("Type error, options are only 1, 2, 3, 4 or 5. Try again")
        main()

# Init program

main()


    

