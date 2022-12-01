tv_shows = ["Ang Probinsyano","Bolera","Lolong","Arcane","Breaking Bad"]
for i in tv_shows:
    print(i)
show = input("What show do you like?\n")
order = int(input("What order do you like to put it?\n"))
tv_shows.insert(order-1,show)
for j in tv_shows:
    print(j)

