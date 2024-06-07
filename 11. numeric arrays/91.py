from array import *


x = array('i',[2,2,3,4,4])
print(x)
num = int(input("Enter one number from this list:  "))
count = 0
length = len(x)

for i in range(0, length) :
    if x[i] == num:
        count = count + 1

print("Your number appears", count, " times")
