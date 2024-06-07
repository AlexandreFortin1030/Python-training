for i in range(9, -1, -1):
    print("there are ", i+1, " green bottles hanging on the wall,")
    print(i+1, "green bottles hanging on the wall,")
    print(" and if one green bottle should accidently fall...")
    print("###")
    print(i)
    res = int(input("How many green bottles will there be on the wall:  "))

    if res == i:
        print("There will be ", i, "green bottles hanging on the wall")
    else:
        print("No, try again")
        i = i +1

print("There are no more green bottles hanging on the wall")
