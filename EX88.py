from array import *

new_nums = array("i",[])

for x in range(5):
    nums = int(input("Give an integer: "))
    new_nums.append(nums)

new_nums = sorted(new_nums)

new_nums.reverse()

print(new_nums)