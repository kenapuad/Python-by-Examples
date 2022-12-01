import csv

start = int(input("Add a beginning year: "))
end = int(input("Add an ending year: "))
file = open("F:\\python\\Python by Examples\\Books.csv","r")
file2 = list(csv.reader(file))
tmp = []
for row in file2:
    tmp.append(row)

x = 0

for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <= end:
        print(tmp[x])
    x = x + 1



