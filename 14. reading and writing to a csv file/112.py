import csv

file = open("Books.csv", "a")
print("Enter a title:")
title = input("")
print("an author:")
author = input("")
print("and a realease date:")
date = input("")

newrecord = title + "," + author + "," + date + "\n"
file.write(str(newrecord))

file.close()





# Using the Books.csv file
# from program 111, ask
# the user to enter another
# record and add it to the
# end of the file. Display
# each row of the .csv file
# on a separate line.
