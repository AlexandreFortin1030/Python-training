import random

num = random.randint(1, 5)

choice = int(input("Pick a number between 1 and 5:  "))
if choice == num:
    print("Well done!")

else:
    if choice < num:
        print("too low")
        choice = int(input("pick another number:  "))
        if choice == num:
            print("Correct :)")
        else:
            print("Too bad, you lost")

    elif choice > num:
        print("Too high")
        choice = int(input("pick another number:  "))
        if choice == num:
            print("Correct :)")
        else:
            print("You lost... try again :)")        