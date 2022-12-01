a = int(input("1) Square\n2) Triangle\n\nEnter a number:\n"))
    
if a == 1:
    b = int(input("Length of the sides: "))
    print("Area is",b**2)
elif a == 2:
    c = int(input("Enter base: "))  
    d = int(input("Enter height: "))
    print("Area is",0.5*c*d)
else:
    print("Incorrect")