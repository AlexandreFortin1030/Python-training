from array import *
import random



x = array('i',[])

for i in range(0, 5):
    num = random.randint(0,100)
    x.append(num)

print(x)

number = int(input("Enter a number from the list:  "))

while number not in x:
    print("Oopsy, this number's not in the list...")
    number = int(input("Enter a number from the list:  "))

index = x.index(number)
print(index)








# Display an array of five
# numbers. Ask the user to
# select one of the numbers.
# Once they have selected a
# number, display the
# position of that item in the
# array. If they enter
# something that is not in
# the array, ask them to try
# again until they select a
# relevant item.