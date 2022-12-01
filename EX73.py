fave_food = dict()

for i in range(4):
    x = input("Favorite foods: ")
    fave_food[i+1] = x

print(fave_food)

remove = int(input("What food to remove? "))
del fave_food[remove]

print(sorted(fave_food.values()))



