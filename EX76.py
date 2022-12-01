invites = []

for i in range(3):
    invites.append(input("Invite a guest: "))

more = input("Do you want to invite more? ")

while more == "yes":    
    invites.append(input("Invite a guest: "))
    more = input("Do you want to invite more? ")

print(f"You've invited a total of {len(invites)}")




