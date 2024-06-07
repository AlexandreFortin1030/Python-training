import csv

file = open ("Books.csv", "r")
reader = csv.reader(file)
x = 0
for row in reader:
    display = "row" + str(x) + ": "
    print(display)
    print(row)
    x = x + 1
file.close()




