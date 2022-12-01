import sqlite3
from tkinter import *

with sqlite3.connect("TestScores.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Scores(
    Name text PRIMARY KEY,
    Grade float);""")

window = Tk()
window.title("Test Scores")
window.geometry("380x150")

def add():
    newname = entryname.get()
    newgrade = entrygrade.get()
    cursor.execute("""INSERT INTO Scores(Name,Grade)
        VALUES(?,?)""",(newname,newgrade))
    db.commit()
    entryname.delete(0, END)
    entrygrade.delete(0, END)
    entryname.focus()

def clear():
    entryname.delete(0, END)
    entrygrade.delete(0, END)
    entryname.focus()

labelname = Label(text= "Enter student's name: ")
labelname.place(x= 20, y= 20, height= 20, width= 150)

labelgrade = Label(text= "Enter student's grade: ")
labelgrade.place(x= 20, y= 50, height= 20, width= 150)

entryname = Entry(text = "")
entryname.place(x= 160, y= 20, height= 20, width= 150)

entrygrade = Entry(text= "")
entrygrade.place(x= 160, y= 50, height= 20, width= 150)

addbutton = Button(text= "Add", command= add)
addbutton.place(x= 160, y= 80, height= 20, width= 50)
clearbutton = Button(text = "Clear", command= clear)
clearbutton.place(x= 220, y= 80, height= 20, width= 50)

window.mainloop()
db.close()





