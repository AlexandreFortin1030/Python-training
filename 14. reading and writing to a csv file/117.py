import random
import csv
import datetime

game = ""
name = input("Enter your name:  ")
game = game + name
score = 0

for i in range (0,3):
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 10)
    num3 = random.randint(0, 3)
    operand = ["+","-","*","/"]


    question = str(num1) + operand[num3] + str(num2) + "=...?"
    game = game + "," + question
    print(question)
    answer = int(input(""))
    game = game + "," + str(answer)

    if num3 == 0 and answer == num1+num2:
        score += 1
        print("Well done!")
    elif num3 == 1 and answer == num1-num2:
        score += 1
        print("Well done!")

    elif num3 == 2 and answer == num1*num2:
        score += 1
        print("Well done!")

    elif num3 == 3 and answer == num1/num2:
        score += 1
        print("Well done!")

    else:
        print("Not quite...!")

print("ok,", name, " Your score is: ", score)
game = game + "," + str(score)
date = datetime.datetime.now()
game = game + "," + str(date) + "\n"

file = open("Quiz.csv", "a")
file.write(game)
file.close()

# write every question, answer, name and score in a csv file.