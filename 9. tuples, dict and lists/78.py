list = ["GoT", "Dexter", "Back Harbor", "True Detective"]
for i in list:
    print(i)
newShow = input("Enter the name of a new show to be inserted:  ")
newShow = newShow.title()
index = int(input("Starting from zero, where do you want your program to be inserted in the list:  "))
list.insert(index, newShow)

for i in list:
    print(i)

