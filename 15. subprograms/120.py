import random


def menu():
    print("1) ", "Addition")
    print("2) ", "Substraction")
    print("Enter 1 or 2:")
    choice = int(input("  "))
    return choice

def random1():
    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    print(num1, "+", num2, "=...?")
    answer = int(input("  "))
    res = num1 + num2
    return answer, res


def random2():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    print(num1, "-", num2, "=...?")
    answer = int(input("  "))
    res = num1 - num2
    return answer, res

def check(answer, res):
    if answer == res:
        print("Correct !")
    else:
        print("Incorrect :(")
        print("The answer is ", answer)



def main():
    choice = menu()
    if choice == 1:
        answer, res = random1()
        check(answer, res)
    elif choice == 2:
        answer, res = random2()
        check(answer, res)
    else:
        print("Type error: menu has only option 1 and 2")


main()
