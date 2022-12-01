import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

year = int(input("Enter a year: "))

cursor.execute("""SELECT Title, DatePublished FROM Books WHERE DatePublished>? ORDER by DatePublished""",[year])
for x in cursor.fetchall():
    print(x)

db.close()





