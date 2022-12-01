total = 0

for i in range(0,5):
    a = int(input("5 Numbers:"))
    b = input("Include? y/n")
    if b == "y":
        total = total + a
    
print(total)
