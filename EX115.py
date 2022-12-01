import csv

file = open("F:\\python\\Python by Examples\\Books.csv","r")
tmp = []
for row in file:
    tmp.append(row)
x = 1
for row in tmp:
    print(x, tmp[x-1])
    x = x + 1