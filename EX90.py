from array import *
#import random

nums = array("i",[])

#count = 0

while len(nums) < 5:
    num = int(input("Give a number: "))
    if num >= 10 and num <= 20:
        nums.append(num)
        # count = count + 1
    else:
        print("Outside range")

print("Thank you here are the numbers: ")

for i in nums:
    print(i)