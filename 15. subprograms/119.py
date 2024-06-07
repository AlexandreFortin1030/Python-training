import random

def randomNumber():
    low = int(input("Enter a number here:  "))
    high = int(input("Enter a greater number here:  "))
    comp_num = random.randint(low, high)
    return comp_num

def userNumber():
    print("I am thinking of a number...")
    print("Try and guess it:")
    number = int(input("  "))
    return number

def check(comp_num, number):
    while comp_num != number:
        if number < comp_num:
            print("Too low...")
            print("Try again:")
            number = int(input("  "))
        elif number > comp_num:
            print("Too high...")
            print("Try again:")
            number = int(input("  "))

    print("Correct, you won !!")

def main():
    comp_num = randomNumber()
    number = userNumber()
    check(comp_num, number)


main()
