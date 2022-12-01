import csv
import random

name = input("Enter player name: ")
x = random.randint(1, 100)
y = random.randint(1, 100)
z = int(input(f"{x}  +  {y} = "))
score = 0
if z == x + y:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")
a = random.randint(1, 100)
b = random.randint(1, 100)
c = int(input(f"{a}  -  {b} = "))
if c == a - b:
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

file = open("F:\\python\\Python by Examples\\Scores.csv","a+")
file.write(name+"\n")
file.write(f"{x}  +  {y} = {z}\n")
file.write(f"{a}  -  {b} = {c}\n")
file.write(f"Score: {score}\n")
file.close()