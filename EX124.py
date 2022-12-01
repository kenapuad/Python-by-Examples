from tkinter import *

window = Tk()
window.title("Window Title")
window.geometry("450x450")

def go():
    name = entry_box.get()
    message = str("Hello " + name)
    output_box["text"] = message

label1 = Label(text = "Name: ")
label1.grid(row = 0, column = 0)
entry_box = Entry (text = "")
entry_box.grid(row = 1, column = 0)
button1 = Button(text = "OK", command = go)
button1.grid(row = 2, column = 0)
output_box = Message(text = "")
output_box.grid(row = 3, column = 0, columnspan = 3)

window.mainloop()
