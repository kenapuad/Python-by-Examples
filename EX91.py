from array import *

nums = array("i",[11,23,21,6,24,11])

print(nums)

num = int(input("Give a number from the array: "))

x = nums.count(num)

print(num,f"appeared {x} time/s in the array")