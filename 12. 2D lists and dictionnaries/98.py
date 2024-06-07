list = [[2,7,5],[1,9,3],[5,1,3],[7,5,9]]
L = len(list)
print("There are", L,"rows in the list, from 0 to 3.")
row = int(input("Which one would you like to display?"))

print(list[row])

num = int(input("Enter a new number to be added to that row:  "))

list[row].append(num)
print(list[row])
print(num, "added to the list :)")




# Using the 2D list from program 096, ask the user
# which row they would like displayed and display
# just that row. Ask them to enter a new value and
# add it to the end of the row and display the row
# again.