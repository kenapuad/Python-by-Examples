from tkinter import *

window = Tk()
window.title("Addition")
window.geometry("200x200")

def add():
    num = textbox1.get()
    num = int(num) 
    answer = result["text"]  
    answer = int(answer)
    total = num + answer
    result["text"] = total

def reset():
    textbox1.delete(0, END)
    result["text"] = 0

total = 0
num = 0

textbox1 = Entry(text = "")
textbox1.place(x = 75, y = 20, width = 75, height = 25)

add = Button(text = "Add", command = add)
add.place(x = 75, y = 50, width = 75, height = 25)

delete1 = Button(text = "Reset", command = reset)
delete1.place(x = 75, y = 110, width = 75, height = 25)

result = Message(text = 0)
result.place(x = 75, y = 80, width = 75, height = 25)

window.mainloop()
