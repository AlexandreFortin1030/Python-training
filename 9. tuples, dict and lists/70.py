country_tuple = ("usa", "france", "belgium", "iceland", "ireland")
for i in country_tuple:
    print(i)

choice = int(input("Enter a number between 1 and 5 included:  "))
choice = choice-1
print(country_tuple[choice])
