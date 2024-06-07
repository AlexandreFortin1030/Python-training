colors = ["grey", "green", "black", "purple", "brown", "red", "white", "pink", "orange", "yellow"]
start = int(input("Enter a starting number between 0 and 4:  "))
end = int(input("Enter a finish number between 5 and 9:  "))
end = end + 1
print(colors[start:end])