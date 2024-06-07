from array import *

x = array('i',[])
for i in range(0, 5):
    print(i, "/5")
    num = int(input("Enter a number:  "))
    x.append(num)

x = sorted(x)
print(x)
num = int(input("Select one of the previous numbers:  "))
y = array('i',[])


if num in x:
    y.append(num)
    x.remove(num)
    print(x)
    print(y)
else:
    print(num, " is not in the array...")





# Ask the user to enter five
# numbers. Sort them into order
# and present them to the user.
# Ask them to select one of the
# numbers. Remove it from the
# original array and save it in a
# new array.