list = []
for i in range(1,6):
    print(i, "/5 Enter a number:  ")
    num = int(input(" "))
    list.append(num)
    
list.reverse()
print(list)