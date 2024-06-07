print("####################")
print("### 1/  Square   ###")
print("### 2/ Triangle  ###")
print("####################")
print("--> Enter a number:")
num = int(input())
if num == 1:
    side = float(input("Enter the length of a side: "))
    res = side*side
    print("the area is equal to", res)
elif num == 2:
    base = float(input("Enter the base of your triangle: "))
    height = float(input("Now enter the height: "))
    area = base*height/2
    print("Your triangle's area is: ", round(area,2))
else:
    print("selection error, exiting program...")