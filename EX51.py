import time
num = 10

while num > 0:
    print(f"There are {num} green bottles hanging on the wall")
    print(f"{num} green bottles hanging on the wall")
    print("and if 1 green bottle should accidentally fall")
    a = int(input("How many green bottles will be hanging on the wall "))
    num = num - 1
    if a == num:
        print(f"There will be {num} green bottles hanging on the wall")
    else:
        while a != num:
            a = int(input("Try again "))
print("There are no more green bottles")  
