from array import *

count = 0
coll = array('i',[])


while count < 5:
    num = int(input("Enter a number:  "))
    if num <= 20 and num >= 10:
        coll.append(num)
        count = count +1
    else:
        print("Out of range...")

print("Thank you")
for i in coll:
    print(i)