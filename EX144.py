import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""SELECT Name FROM Authors""")
for x in cursor.fetchall():
    print(x)

author = input("Select an author: ")

cursor.execute("""SELECT Books.ID, Books.Title, Books.Author, Books.DatePublished
FROM Books,Authors WHERE Authors.Name=Books.Author AND Authors.Name=?""",[author])
file = open("Authors.txt","w")
tmp = []
x = 0
for i in cursor.fetchall():
    tmp.append(i)
for row in tmp:
    record = str(tmp[x][0]) + " - "+ tmp[x][1]+ " - "+ tmp[x][2]+ " - " + str(tmp[x][3])+"\n"
    file.write(record)
    x = x + 1
file.close()

db.close()





