count = 0
more = "y"

while more == "y":
    invite = input("What's the name you want to invite: ")
    print(invite, "has been invited!")
    count = count + 1
    more = input("Do you want to invite more? ")

print("You have invited a total guests of ",count)