direction = input("Which direction do you want? up/down:  ")
direction = direction.lower()
if direction == "up":
    topnum = int(input("Enter a top number:  "))
    topnum = topnum+1
    for i in range(1,topnum):
        print(i)
elif direction == "down":
    botnum = int(input("Enter a number bellow 20:  "))
    botnum = botnum -1
    for i in range(20, botnum, -1):
        print(i)

