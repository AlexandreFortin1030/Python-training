word = input("Enter a word:  ")
length = len(word)
num = length-1
for i in range(num, -1, -1):
    print(word[i])