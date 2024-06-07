people = int(input("How namy people do you want to invite to the party:  "))

if people < 10:
    print("OK!" )
    people = people + 1
    for i in range(1, people):
        num = people - 1
        print(i, "/", num)
        name = input("Enter the name: ")
        print(name, "Has been invited :)")
elif people >= 10:
    print("Too many people..!")