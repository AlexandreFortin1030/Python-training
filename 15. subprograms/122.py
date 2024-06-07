import csv

### Subprograms

def menu():
    print("###### --- Menu --- ######")
    print("1) Add to file")
    print("2) View all records")
    print("3) Quit program")
    print(" ")
    print("Enter the number of your selection")
    choice = input("--->  ")
    return choice

def option1():
    file = open("Salaries.csv", "a")
    name = input("Enter a name:  ")
    salary = input("Enter a salary:  ")
    newrecord = name + "," + salary + "\n"
    file.write(newrecord)
    print("#########################")
    print("New record added to file")
    file.close()

def option2():
    file = open("Salaries.csv", "r")
    display = file.read()
    print(display)
    file.close()
    print("#########################")


def option3():
    print("##########################")
    print("Thank you, see you soon...")
    print("##########################")

def main():
    choice = menu()
    if choice == "1":
        option1()
        main()
    elif choice == "2":
        option2()
        main()
    elif choice == "3":
        option3()
    else:
        print("Type error, option are only 1, 2 or 3")
        main()

### Main function

main()