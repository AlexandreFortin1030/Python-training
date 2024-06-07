import csv


print("Enter a starting year:")
start = int(input("  "))
print("And now an end year:")
end = int(input("  "))

file = open ("Books.csv", "r")
reader = csv.reader(file)
count = 0

for row in reader:
    num = int(row[2])
    if num >= start and num <= end:
        print(row)
        count = count + 1

if count == 0:
    print("Sorry, no match to your search")