import random

pool = ["heads", "tails"]
value = random.choice(pool)
choice = input("heads or tails? :   ")
choice = choice.lower()
if choice == value:
    print("Well done, you won !")
elif choice != value:
    if choice == "heads" or choice == "tails":
        print("Bad luck, try again")
    else: 
        print("Input error") 