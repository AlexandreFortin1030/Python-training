country_tuple = ("france", "icelande", "usa", "belgium", "algeria")
for i in country_tuple:
    print(i)

choice = input("Enter the name of one of the previous countries:  ")
choice = choice.lower()
print("Index of your contry is:")
print(country_tuple.index(choice)+1, "out of 5")