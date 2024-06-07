num = int(input("Enter a number between 10 and 20:  "))


while num <= 10 or num >= 20:

    if num < 10:
        print("Too low!")
        print("try again...")
        num = int(input("Enter  number between 10 and 20:  "))

    
    elif num > 20:
        print("Too high!")
        print("Try again")
        num = int(input("Enter a number between 10 and 20:  "))

    elif num <= 20 and num >= 10:
        print("Thank you")


print("Thank you")
