word = input("Enter a word here:")
length = len(word)
if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" or word[0] == "y":
    res = word+"way"
    print(res.lower())
else:
    res = word[1:length]
    letter = word[0]
    print(res+letter+"ay")

