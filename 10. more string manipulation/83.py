name = input("Type in your name in uppercase:  ")

while name.isupper() == False:
    print("Name was not written in uppercases, try again")
    name = input("Type in your name in uppercase:  ")

print("Well done baby")
