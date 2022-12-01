import csv

file = list(csv.reader(open("un_pw.csv")))
tmp = []
for col in file:
    tmp.append(col[0])
    
print(tmp)