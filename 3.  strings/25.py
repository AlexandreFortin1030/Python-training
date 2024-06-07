firstname = input("Enter your firstname:")
if len(firstname)<5:
    surname = input("Enter your surname")
    join = firstname+surname
    print(join.upper())
elif len(firstname)>=5:
    print(firstname.lower())