nums = []

for i in range(3):
    num = int(input("Give a number: "))
    nums.append(num)


rem = input("Do you want to keep the last number?(y/n) ")

if rem == "n":
    del nums[len(nums)-1]

print(nums)