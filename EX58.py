import random

score = 0
for i in range(0,5):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    num3 = num1 + num2
    num4 = int(input(f"{num1} + {num2} is "))
    if num4 == num3:
        score = score + 1
print("You scored", score, "out of 5")