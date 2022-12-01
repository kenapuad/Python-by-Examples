from tkinter import *
import csv

window = Tk()
window.title("If Number")
window.geometry("250x150")

def add():
    x = enterbox.get()
    if x.isdigit():
        list_box.insert(END, x)
    enterbox.delete(0, END)

def clear():
    list_box.delete(0, END)
    enterbox.delete(0, END)

def save():
    tmp_list = list_box.get(0,END)
    file = open("F:\\python\\Python by Examples\\List.csv", "a+")
    for x in tmp_list:
        file.write(x+"\n")
    file.close()


enterlabel = Label(text = "Enter a number: ", bg = "green")
enterlabel.place(x = 10, y = 10, height = 20, width = 100)

enterbox = Entry(text = "")
enterbox.place(x = 120, y = 10, height = 20, width = 75)

addbutton = Button(text = "Add", command=add)
addbutton.place(x = 10, y = 40, height = 20, width = 40)

clearbutton = Button(text = "Clear", command=clear)
clearbutton.place(x = 60, y = 40, height = 20, width = 40)

savebutton = Button(text = "Save", command=save)
savebutton.place(x = 110, y = 40, height = 20, width = 40)

list_box = Listbox()
list_box.place(x = 10, y = 70, height = 20, width = 75)

window.mainloop()
