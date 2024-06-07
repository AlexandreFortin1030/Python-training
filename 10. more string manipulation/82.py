poem = "jme roule encore un doobie puis j'oublie tout-bi doobie doobie..."
print(poem)
length = len(poem)
length = length-1
print("Length of the poem is", length)
print("Between 0 and ", length, ", pick the start index, to set where the quote will start")
start = int(input("--->  "))
print("Now, pick the end index, to choose where the quote ends")
end = int(input("--->  "))

print(poem[start:end])

