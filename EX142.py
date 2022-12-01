import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)

birthplace = input("Select a place of birth: ")
birthplace = birthplace.capitalize()
cursor.execute("""SELECT Books.Title, Books.DatePublished, Books.Author
FROM Books,Authors WHERE Authors.Name=Books.Author AND Authors.PlaceOfBirth=?""",[birthplace])
for x in cursor.fetchall():
    print(x)

db.close()





