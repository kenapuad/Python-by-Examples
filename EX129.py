from tkinter import *

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

enterlabel = Label(text = "Enter a number: ", bg = "green")
enterlabel.place(x = 10, y = 10, height = 20, width = 100)

enterbox = Entry(text = "")
enterbox.place(x = 120, y = 10, height = 20, width = 75)

addbutton = Button(text = "Add", command=add)
addbutton.place(x = 10, y = 40, height = 20, width = 40)

clearbutton = Button(text = "Clear", command=clear)
clearbutton.place(x = 60, y = 40, height = 20, width = 40)

list_box = Listbox()
list_box.place(x = 10, y = 70, height = 20, width = 75)

window.mainloop()
