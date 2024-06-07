subjects = ["math", "litterature", "sport", "algebra", "history"]
for i in subjects:
    print(i)

choice = input("Enter the one you liked the least at school:  ")
choice.lower()

subjects.remove(choice)

for i in subjects:
    print(i)