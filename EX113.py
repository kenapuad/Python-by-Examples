import csv

entry = int(input("How many books to add: "))

file = open("F:\\python\\Python by Examples\\Books.csv","a")

for x in range(entry):
    new_book = input("Enter new book title: ")
    new_author = input("Enter new book author: ")
    new_pub = input("Enter new book publish year: ")
    file.write(new_book + ", " + new_author + ", " + new_pub + "\n")
file.close()    

file = open("F:\\python\\Python by Examples\\Books.csv","r")
author = input("Name the author you want to display: ")
reader = csv.reader(file)
count = 0
for row in file:
    if author in str(row):
        print(row)
        count = count + 1
if count == 0:
        print("No book for that author")
file.close()