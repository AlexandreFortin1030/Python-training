name = input("Enter your name: ")
num = int(input("Enter a number: "))
if num < 10:
    num = num -1
    for i in range(1,num):
        print(name)
else:
    for i in range(1,4):
        print("Too high :(")