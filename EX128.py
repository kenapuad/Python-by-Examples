from tkinter import *

window = Tk()
window.title("Names List")
window.geometry("400x200")



def klToMi():
    kl = enterkl.get()
    ml = float(kl) * 0.6214
    ml = str(ml)
    text1 = kl+" kl is "+ml+" in miles"
    output["text"] = text1


def miToKl():
    mi = entermi.get()
    kl = float(mi) * 1.6093
    kl = str(kl)
    text1 = mi + " ml is " + kl + " in kl"
    output["text"] = text1

labelkl = Label(text = "Enter kilometers:", justify= "left")
labelkl.place(x = 5, y = 20, width = 100, height = 20)

enterkl = Entry(text = "")
enterkl.place(x = 110, y = 20, width = 100, height = 20)

button1 = Button(text = "Convert to mi", command= klToMi)
button1.place(x = 250, y = 20, width = 100, height = 20)
button2 = Button(text = "Convert to kl", command= miToKl)
button2.place(x = 250, y = 45, width = 100, height = 20)

labelmi = Label(text = "Enter miles:",justify= "left")
labelmi.place(x = 5, y = 45, width = 100, height = 20)

entermi = Entry(text = "")
entermi.place(x = 110, y = 45, width = 100, height = 20)

output = Message(text = "", justify= "center")
output.place(x = 5, y = 90, width = 390, height = 40)
output["bg"] = "red"

window.mainloop()
