total = 0
for i in range(1,6):
    print(i, "/5")
    num = int(input("--->Enter a number: "))
    choice = input("Do you want this number to be included? y/n:  ")
    if choice == "y":
        total = total + num
    else:
        continue
    
print("#############")
print("#############")
print("total is:", total)
print("#############")
