list = [243, 522, 120, 123]
for i in list:
    print(i)

num = int(input("Enter a three digit number:  "))

if num in list:
    print(list.index(num))

else: 
    print("Not in the list")
