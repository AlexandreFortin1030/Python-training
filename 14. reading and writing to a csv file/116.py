file = open ("Books.csv", "r")
list = []

for row in file:          # Get each row and clean it from the /n part.
    length = len(row)
    end = length -1
    row = row[0:end]
    list.append(row)

file.close()

for row in list:          # present every row with an index before it
    index = list.index(row)
    print(str(index) + ":" + row)

row = int(input("Which row do you want to remove from the list?  "))

del list[row]
for row in list:          
    index = list.index(row)
    print(str(index) + ":" + row)

row = int(input("Which row do you want to change?  "))

print(list[row])
print("Enter a title followed by a coma, an author followed by a coma and then a realese date")
print("When done, press enter")
list[row] = input("  ")

print("Change's been saved")
for row in list:          
    index = list.index(row)
    print(str(index) + ":" + row)

file = open("Books.csv", "w")
for row in list:
    newrecord = row + "\n"
    file.write(newrecord)
file.close()
