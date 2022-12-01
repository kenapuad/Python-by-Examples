data = {}

for i in range(4):
        name = input("Enter a name: ")
        age = int(input("Enter age: "))
        size = int(input("Enter shoe size: "))
        data[name] = {"Age": age, "Shoe Size": size}

ask = input("Who's info do you want to display: ")
print(data[ask])