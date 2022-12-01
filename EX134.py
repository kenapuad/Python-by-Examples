from tkinter import *
import random

window = Tk()
window.title("Add Game")
window.geometry("300x240")

def new():
    photobox = Label(window, image = defaultp)
    photobox.place(x = 135, y = 200, height = 30, width= 30)

def generate():
    x = random.randint(10, 50)
    num1_msg["text"] = x
    y = random.randint(10, 50)
    num2_msg["text"] = y
    new()
    ans.delete(0, END)


def submit():
    a = int(num1_msg["text"])
    b = int(num2_msg["text"])
    c = int(ans.get())
    if c == (a + b):
        photobox = Label(window, image = correct)
        photobox.place(x = 135, y = 200, height = 30, width= 30)    
    else:
        photobox = Label(window, image = wrong)
        photobox.place(x = 135, y = 200, height = 30, width= 30)   

num1 = Label(text = "First Number: ")
num1.place(x = 20, y = 20, height = 20, width = 100)

num1_msg = Message(text = "")
num1_msg.place(x = 140, y = 20, height = 20, width = 100)

num2 = Label(text = "Second Number: ")
num2.place(x = 20, y = 50, height = 20, width = 100)

num2_msg = Message(text = "")
num2_msg.place(x = 140, y = 50, height = 20, width = 100)

ans_msg = Label(text = "Your sum: ")
ans_msg.place(x = 20, y = 80, height = 20, width = 100)

ans = Entry()
ans.place(x = 140, y = 80, height = 20, width = 100)

check = Button(text = "Submit", command= submit)
check.place(x = 100, y = 120, height = 20, width = 100)

gen = Button(text = "New Game", command= generate)
gen.place(x = 100, y = 160, height = 20, width= 100)

correct = PhotoImage(file = "correct.gif")
wrong = PhotoImage(file = "wrong.gif")
defaultp = PhotoImage(file = "R.gif")

new()

window.mainloop()
