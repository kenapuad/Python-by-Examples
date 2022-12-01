from tkinter import *

window = Tk()
window.title("Names")
window.geometry("300x300")

def hello():
    name = name_entry.get()
    msg = str(f"Hello {name}")
    outputbox["text"] = msg

logo = PhotoImage(file = "logo.gif")
logoimage = Label(image = logo)
logoimage.place(x = 50, y = 20, height = 150, width = 200)

namelabel = Label(text = "Enter your name: ")
namelabel.place(x = 20, y = 180, height = 20, width = 100)

name_entry = Entry(text = "")
name_entry.place(x = 120, y = 180, height = 20, width = 140)

pressme = Button(text = "Press Me", bg= "blue", command= hello)
pressme.place(x = 20, y = 210, height = 20, width = 100)

outputbox = Message(text = "", justify="right")
outputbox.place(x = 120, y = 210, height = 20, width = 200)

window.mainloop()
