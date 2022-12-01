from array import *
import random

random_ints = array("i",[])

for x in range(5):
    nums = random.randint(1,100)
    random_ints.append(nums)

for i in random_ints:
    print(i)