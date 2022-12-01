from tkinter import *
import random

window = Tk()
window.title("Screen Color")
window.geometry("300x240")

def click():
    window.configure(background = selectColor.get())

selectColor = StringVar(window)
selectColor.set("Select Color")
colorsList = OptionMenu(window,selectColor,"Red","Blue","Green","Yellow","Orange","Violet")
colorsList.place(x = 90, y = 30)

change = Button(text = "Click Me!", command= click)
change.place(x = 120, y = 90, height= 30, width=60)


window.mainloop()
