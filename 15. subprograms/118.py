
def choice():
    num = int(input("Enter a number here:  "))
    num = num + 1
    return num
def count(num):
    for i in range(1,num):
        if 1 < num:
            print(i)
        else:
            print("Number is too low")

def main():
    num = choice()
    count(num)

main()