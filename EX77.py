invites = []

for i in range(3):
    invites.append(input("Invite a guest: "))

more = input("Do you want to invite more? ")

while more == "yes":    
    invites.append(input("Invite a guest: "))
    more = input("Do you want to invite more? ")

print(invites)

guest = input("Give one guest: ")

print(guest, "is number", invites.index(guest),"of your list")

rem = input("Do you want to keep " + guest + "? ")

if rem == "no":
    invites.remove(guest)

print(invites)


