import csv

file = open("F:\\python\\Python by Examples\\Books.csv","r")
tmp = []
for row in file:
    tmp.append(row)
x = 0
for row in tmp:
    print(x, tmp[x])
    x = x + 1

delete_row = int(input("Which row should be deleted? "))
del tmp[delete_row]
y = 0
for row in tmp:
    print(y, tmp[y])
    y = y + 1
amend_row = int(input("Which row you want to amend? "))
z = 0
for row in tmp:
    print(tmp[amend_row][z])
    z = z + 1

