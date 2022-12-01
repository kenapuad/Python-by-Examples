from array import *

nums = array("i",[])


for i in range(5):
    num = int(input("Give a number: "))
    nums.append(num)
print("Here are your numbers: ")
nums = sorted(nums)

for j in nums:
    print(j)

x = int(input("Give a number to remove: "))
if x in nums:
    nums.remove(x)
    nums2 = array("i",[])
    nums2.append(x)
    print("Original Array: ")
    print(nums)
    print("New Array: ")
    nums2 = sorted(nums2)
    print(nums2)
else:
    print("Not in your list")





