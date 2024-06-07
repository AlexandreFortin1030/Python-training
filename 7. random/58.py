import random


print("---> Question 1/3:")
score = 0
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
print(num1, "-", num2, "=")
choice = int(input())
if choice == num1 - num2:
    score += 1
else:
    pass

print("---> Question 2/3:")
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
print(num1, "x", num2, "=")
choice = int(input())
if choice == num1 * num2:
    score += 1
else:
    pass

print("---> Question 3/3:")
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
print(num1, "+", num2, "=")
choice = int(input())
if choice == num1 + num2:
    score += 1
else:
    pass

print("Your score is", score, "/3")

