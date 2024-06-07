sales = {"john":{"N":3056, "S":8463, "E":8441, "W":2694},
        "tom":{"N":4832, "S":6786, "E":4737, "W":3612},
        "anne":{"N":5239, "S":4802, "E":5820, "W":1859},
        "fiona":{"N":3904, "S":3645, "E":8821, "W":2451}}

print("Choose a name and a district you'd like to know about: john, tom, anne, fionna.  ")
name = input("Enter a name in here:  ")
print("Choose a district: N, S, E, W.")
district = input("Enter your choice here:  ")
district = district.upper()

print(sales[name][district])

print("Now choose a name and district you'd like to change:  ")
print("A name first")
name = input("Enter your choice in here:  ")
print("And now a district")
district = input("Enter it here:  ")


print(sales[name][district])

print("Do you want to change the figure?")
choice = input("y/n  ")
choice.lower()

if choice == "y" or choice == "yes":
    value = int(input("Enter new value here:  "))
    sales[name][district] = value
    print("New value saved")
    print(sales[name][district])
    print(sales[name])

elif choice == "n" or choice == "no":
    print("Ok, see you!")
else:
    print("Input error, try again")





# Using program 100, ask the user for a name and a region. Display the relevant data. Ask
# the user for the name and region of data they want to change and allow them to make
# the alteration to the sales figure. Display the sales for all regions for the name they
# choose.