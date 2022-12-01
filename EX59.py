import random

color = ["RED","GREEN","BLUE","YELLOW","VIOLET"]
print(color)
color1 = random.choice(color)
tryagain = True

while tryagain == True:
    color2 = input("Pick a color: ")
    color2 = color2.upper()
    if color2 == color1:
        print("Well done!")
        tryagain = False
    else:
        if color1 == "RED":
            print("You're getting reddish")
        elif color1 == "GREEN":
            print("You look like the HULK")
        elif color1 == "BLUE":
            print("Feeling blue today?")
        elif color1 == "YELLOW":
            print("It's going bananas")
        elif color1 == "VIOLET":
            print("haha eggplant")