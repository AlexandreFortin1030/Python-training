name = input("Enter your name:  ")
count = 0
for letter in name:
    if letter == "a" or letter == "e" or letter == "i" or letter == "0" or letter == "u" or letter == "y":
        count = count + 1
    else:
        pass

print("There are", count, "vowels in your name")
