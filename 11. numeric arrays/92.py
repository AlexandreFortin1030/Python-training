from array import *
import random


x = array('i',[])
y = array('i',[])

for i in range(0,3):
    num = int(input("Enter a number:  "))
    x.append(num)
print("Numbers saved")

for i in range(0,5):
    num = random.randint(0, 30000)
    y.append(num)

length = len(x) - 1

for i in range(0, length):
    y.append(x[i])
print("Arrays merged")

y = sorted(y)

length = len(y)
for i in range(0, length):
    print(y[i])




# Create two arrays (one
# containing three numbers that
# the user enters and one
# containing a set of five random
# numbers). Join these two arrays
# together into one large array.
# Sort this large array and display
# it so that each number appears
# on a separate line.