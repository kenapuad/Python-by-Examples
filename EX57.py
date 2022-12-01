import random

x = random.randint(1,10)
y = False

while y == False:
    a = int(input("Enter a number: "))
    if a > x:
        print("Too high")
    elif a < x:
        print("Too low")
    elif a == x:
        y = True

print("Choice is", x)

