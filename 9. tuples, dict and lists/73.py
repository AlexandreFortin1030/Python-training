favfood = {}
print("Enter your 5 favorite food")
for i in range(1, 6):
    print("number", i, "/5")
    favfood[i]= input("")
print(favfood)
choice = int(input("Which one would you like to remove? Enter the number:  "))
del favfood[choice]
print(favfood)