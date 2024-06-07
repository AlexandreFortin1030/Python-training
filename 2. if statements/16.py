rain = input("Is it raining outside?")
rain = str.lower(rain)
if rain == "yes":
    wind = input("And is it windy too?")
    wind = str.lower(wind)
    if wind == "yes":
        print("Then it's too windy for an umbrella..!")
    else:
        print("Take an umbrella!")
else:
    print("Enjoy your day!")