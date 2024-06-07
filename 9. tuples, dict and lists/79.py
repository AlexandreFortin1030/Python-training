nums = []
for i in range(0, 3):
    num = int(input("Enter a number:  "))
    nums.append(num)

print(nums)
print("are you sure you want to keep ", nums[2], " saved?")
choice = input("y/n:  ")
choce = choice.lower()
if choice == "n" or choice == "no":
    num = nums[2]
    nums.remove(num)
else:
    pass

print(nums)