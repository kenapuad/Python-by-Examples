numbers = [123,223,624,221]
for i in range(len(numbers)):
    print(numbers[i])

choice = int(input("Enter a 3 digit number: "))

if choice in numbers:
    print(choice,"is in index", numbers.index(choice))
else:
    print(choice, "is not in the list")



