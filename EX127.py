from tkinter import *

window = Tk()
window.title("Names List")
window.geometry("300x200")



def addname():
    name = namebox.get()
    list_box.insert(END, name)
    namebox.delete(0, END)
    namebox.focus()

def deletename():
    list_box.delete(0, END)
    namebox.delete(0, END)
    namebox.focus()

entername = Label(text = "Enter name:")
entername.place(x = 5, y = 10, width = 100, height = 20)

namebox = Entry(text = "")
namebox.place(x = 100, y = 10, width = 100, height = 20)

button1 = Button(text = "Add", command = addname)
button1.place(x = 210, y = 10, width = 40, height = 20)

button2 = Button(text = "Clr", command = deletename)
button2.place(x = 210, y = 30, width = 40, height = 20)

list_box = Listbox()
list_box.place(x = 5, y = 30, width = 100, height = 20)

window.mainloop()
