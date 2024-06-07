num1 = int(input("Enter a number:  "))
num2 = int(input("Enter a second one:  "))
res = num1 + num2
choice = input("Do you want to add another number? (y/n):  ")
choice = choice.lower()

if choice == "y" or choice == "yes":

    while choice == "y" or choice == "yes":
        num = int(input("Enter number here:  "))
        res = res + num
        choice = input("Do you still want to add another number (y/n):  ")
        choice = choice.lower()

    print("the total is: ", res)

else:
    print("the total is: ", res)