array1 = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

rowshow = int(input("What row would you like to show? "))

print(array1[rowshow])

colshow = int(input("What column? "))

print(array1[rowshow][colshow])

change = input("Would you like to change this value? y/n: ")

if change == "y":
    newvalue = int(input("What value would you replace? "))
    array1[rowshow][colshow] = newvalue

print(array1[rowshow])
