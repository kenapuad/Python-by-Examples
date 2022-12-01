import random

x = random.randint(1,10)
y = False

while y == False:
    a = int(input("Enter a number: "))
    if a == x:
        y = True

print(y)

