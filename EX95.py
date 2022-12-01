from array import *

nums = array("f",[10.25,11.21,11.23,16.24,88.89])

for j in nums:
    print(round(j,2))

div = int(input("Give a whole number between 2 and 5: "))

again = True

while again == True:
    if div >= 2 and div <= 5:
        again = False
        for i in nums:
            print("Quotient for list is",round(i/div,2))
    else:
        print("Try again!")
        div = int(input("Give a whole number between 2 and 5: "))






