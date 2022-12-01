import time
direction = input("Count from up or down?: ")

if direction.lower() == "up":
    top = int(input("Give top number: "))
    for i in range(1,top+1):
        print(i)
        time.sleep(0.5)
elif direction.lower() == "down":
    down = int(input("Give down number below 20: "))
    for i in range(20,down-1,-1):
        print(i)
        time.sleep(0.5)
else:
    print("I don't understand")
