sports = ["diving", "climbing"]
fav = input("Enter your favorite sport:  ")
fav = fav.lower()
sports.append(fav)
sports.sort()
for i in sports:
    print(i)