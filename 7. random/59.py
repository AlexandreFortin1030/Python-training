
import random


colors = ["blue", "green", "black", "purple", "pink"]

print("blue", "green", "black", "purple", "pink")
pick = random.choice(colors)
choice = input("Choose one color among theses:  ")
while choice != pick:
    if pick == "blue":
        print("Do you feel blue these days?")
        choice = input("Try another colour:  ")


    elif pick == "green":
        print("maybe you lack nature")
        choice = input("Try another colour:  ")

    elif pick == "black":
        print("Do you know batman's colour?")
        choice = input("Try another colour:  ")

    elif pick == "purple":
        print("I like eggplants, do you?")
        choice = input("Try another colour:  ")

    elif pick == "pink":
        print("Be more girly...")
        choice = input("Try another colour:  ")


print("Well done!")        


