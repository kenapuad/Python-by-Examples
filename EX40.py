import time

a = int(input("Input a number below 50:\n"))

for i in range(50,a-1,-1):
    print(i)
    time.sleep(0.5)
