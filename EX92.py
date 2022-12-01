from array import *
import random

nums = array("i",[])
new_array = array("i",[])

for i in range(3):
    num = int(input("Give a number: "))
    nums.append(num)

for j in range(5):
    num = random.randint(1, 100)
    new_array.append(num)

nums.extend(new_array)
nums = sorted(nums)

for x in nums:
    print(x)
