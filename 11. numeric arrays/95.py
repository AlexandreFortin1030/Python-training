from array import *
import random


nums = array('d',[])


for i in range(0, 5):
    num = random.random()
    num = round(num, 2) + random.randint(10, 99)
    nums.append(num)

print(nums)
num = int(input("Enter a number between 2 and 5:  "))
length = len(nums)

if num < 2 or num > 5:
    print("Number not in range")
    num = int(input("Enter a number between 2 and 5:  "))
else:
    for i in range(0,length):
        nums[i] = nums[i]/num     
        nums[i] = round(nums[i], 2)
        print(nums[i])

print(nums)


# Create an array of five numbers
# between 10 and 100 which each have
# two decimal places. Ask the user to
# enter a whole number between 2 and 5.
# If they enter something outside of that
# range, display a suitable error message
# and ask them to try again until they
# enter a valid amount. Divide each of the
# numbers in the array by the number the
# user entered and display the answers
# shown to two decimal places.