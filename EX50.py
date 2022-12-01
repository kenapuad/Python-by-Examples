a = int(input("Enter a number between 10 and 20: "))

while a < 10 or a > 20:
    if a < 10:
        print("Too low!")        
    else:
        print("Too high!")        
    a = int(input("Try again: "))
    
print("Great job!")