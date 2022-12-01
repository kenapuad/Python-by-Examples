name = input("What's your name?: ")
times = int(input("Repeat: "))

if times < 10:
    for i in range(times):
        print(name)
else:
    for i in range(3):
        print("Too high")