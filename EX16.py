rain = input("Is it raining outside?: ")

if rain.lower() == "yes":
    wind = input("Is it windy?: ")
    if wind.lower() == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take and umbrella.")
else:
    print("Enjoy your day!")