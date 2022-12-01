compnum = 50
count = 0
guess = 0

while guess != compnum:
    guess = int(input("Guess: "))
    count = count + 1
    if guess < compnum:
        print("Too low")
    elif guess > compnum:
        print("Too high")

print(count, "tries")