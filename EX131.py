from tkinter import *
import csv

window = Tk()
window.title("Name and Age")
window.geometry("250x150")

def create():
    file = open("F:\\python\\Python by Examples\\Info.csv","w+")
    file.close()

def save():
    file = open("F:\\python\\Python by Examples\\Info.csv","a+")
    name = name_entry.get()
    age = age_entry.get()
    entry1 = name + ", " + age
    name_entry.delete(0,END)
    age_entry.delete(0, END)
    name_entry.focus()
    file.write(entry1 + "\n")
    file.close()

create_csv = Button(text = "Create File", command=create)
create_csv.place(x = 10, y = 10, height = 20, width = 75)

name_label = Label(text = "Name: ")
name_label.place(x = 10, y = 40, height = 20, width = 75)

name_entry = Entry(text = "")
name_entry.place(x = 70, y = 40, height = 20, width = 100)

age_label = Label(text = "Age: ")
age_label.place(x = 10, y = 60, height = 20, width = 75)

age_entry = Entry(text = "")
age_entry.place(x = 70, y = 60, height = 20, width = 100)

saveTo_csv = Button(text = "Save to File", command=save)
saveTo_csv.place(x = 50, y = 90, height = 20, width = 75)

window.mainloop()
