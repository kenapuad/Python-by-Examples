import random

hort = ["heads","tails"]

x = random.choice(hort)
y = input("Heads or Tails: ")

if y.lower() == x:
    print("You win!")
else:
    print("Bad luck!")

print("Computer chose ",x)