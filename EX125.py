from tkinter import *
import random


window = Tk()
window.title("Virtual Dice")
window.geometry("200x200")

def roll():
    result1 = random.randint(1,6)
    result["text"] = result1

rolldice = Button(text = "Roll Dice", command = roll)
rolldice.place(x = 75, y = 50, width = 75, height = 25)

result = Message(text = "")
result.place(x = 75, y = 110, width = 75, height = 25)

window.mainloop()