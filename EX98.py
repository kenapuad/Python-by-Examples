array1 = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

rowshow = int(input("What row would you like to show? "))

print(array1[rowshow])

addto1 = int(input("Give a number to add to the row: "))

array1[rowshow].append(addto1)

print(array1[rowshow])
