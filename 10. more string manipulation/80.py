firstName = input("Enter your first name:  ")
print(len(firstName))

lastName = input("Enter you lastname:  ")
print(len(lastName))

print("Length of your full name (space included) is:")
join = firstName + " " + lastName

print(len(join))