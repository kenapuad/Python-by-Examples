import random

x = random.randint(1,5)

y = int(input("Guess a number from 1 to 5: "))

if y == x:
    print("Well done")
elif y > x:
    print("Too high")
    y = int(input("Guess again: "))
    if y == x:
        print("Correct")
    else:
        print("You lose!")
else:
    print("Too low")
    y = int(input("Guess again: "))
    if y == x:
        print("Correct")
    else:
        print("You lose!")