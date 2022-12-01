invites = int(input("How many guests do you have?\n"))

if invites < 10:
    for i in range(invites):
        name = input("Guest name?: ")
        print(name, "has been invited!")
else:
    print("Too many invites!")