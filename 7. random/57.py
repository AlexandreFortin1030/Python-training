import random

num = random.randint(0, 10)
choice = 11

while choice != num:
    choice = int(input("Enter a number netween 0 and 10:  "))
    if choice < num:
        print("Too low :)")
    elif choice > num:
        print("Too high ^^")

print("Well done !")