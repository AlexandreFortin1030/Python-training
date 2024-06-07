compnum = 50
reset = "yes"

while reset == "yes" or reset == "y":
    tries = 0
    num = int(input("Enter a number:  "))
    while num != compnum:
        if num < compnum:
            print(" Too low, try again :)")
            num = int(input("Enter a number:  "))
            tries = tries + 1

        elif num > compnum:
            print("Too high! Bu try again")
            num = int(input("Enter a number:  "))
            tries = tries + 1

    print("Well done, you fount it!! Secret number was 50 :)")
    print("You used", tries, "tries to find it...")

    reset = input("Do you want to do better? (y/n)  ")
    reset = reset.lower()

print("Thank you, bye !")