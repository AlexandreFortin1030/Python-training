import csv

### Subprograms

def menu():
    print("###### --- Menu --- ######")
    print("1) Add to file")
    print("2) View all records")
    print("3) Delete a record")
    print("4) Quit program")
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
    list = []
    file = open("Salaries.csv", "r")
    reader = csv.reader(file)
    for row in file:
        list.append(row)
    file.close()

    for row in list:
        index = list.index(row)
        print(index, "- ", row)
    print("Enter the number of the record you want to delete")
    record = input("--->  ")
    record = int(record)
    del list[record]

    file = open("Salaries.csv", "w")
    for row in list:
        file.write(row)
    
    print("Record deleted !")
    print("#########################")


def option4():
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
        main()
    elif choice == "4":
        option4()
    else:
        print("Type error, option are only 1, 2 or 3")
        main()

### Main function

main()