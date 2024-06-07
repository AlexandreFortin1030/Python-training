import csv
print("How many records would you like to add?")
amount = int(input("Enter a number:  "))


for i in range(0, amount):
    if i == 0:
        continue
    else:
        file = open ("Books.csv", "a")
        title = input("Enter title here: ")
        author = input("an author: ")
        date = input("and a realease date:  ")
        newrecord = title + "," + author + "," + date + "\n"
        file.write(str(newrecord))
        file.close()

print("Enter an author's name to get all the books")

file = open ("Books.csv", "r")
search = input("  ")
count = 0

for row in file:
    if search in str(row):
        print(row)
        count = count + 1
if count == 0:
    print("No books found for this author")
    file.close()



# Using the Books.csv file, ask the user how many records
# they want to add to the list and then allow them to add
# that many. After all the data has been added, ask for an
# author and display all the books in the list by that author.
# If there are no books by that author in the list, display a
# suitable message.