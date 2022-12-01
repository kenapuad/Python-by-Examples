num1 = int(input("Give a number: "))
#num2 = int(input("Give another number: "))
total = num1 
ans = "y"
while ans == "y":
    num3 = int(input("Give the number to add: "))
    total = total + num3
    ans = input("Do you want to add again?")   
    

print("Your total is", total)
