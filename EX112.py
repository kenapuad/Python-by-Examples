import csv

file = open("F:\\python\\Python by Examples\\Books.csv","a")
new_book = input("Enter another book: ")
file.write(new_book + "\n")
file.close()
file = open("F:\\python\\Python by Examples\\Books.csv","r")
print(file.read())
file.close()