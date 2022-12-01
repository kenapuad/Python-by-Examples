from tkinter import *

window = Tk()
window.geometry("450x300")
window.title("Times Table")

def view():
    num = entrynum.get()    
    for i in range(1,13):
        answer = int(num) * i
        list_num.insert(END,(i,"x",num,"=",answer))
    entrynum.delete(0, END)
    entrynum.focus()

def clear():
    entrynum.delete(0, END)
    list_num.delete(0, END)
    entrynum.focus()
    

labelnum = Label(text= "Enter a number:")
labelnum.place(x = 10, y = 20, height = 20, width = 120)

entrynum = Entry()
entrynum.place(x = 120, y = 20, height = 20, width = 130)

buttonnum = Button(text= "View Times Table", command= view)
buttonnum.place(x = 260, y = 20, height = 20, width = 100)

buttonclear = Button(text= "Clear", command= clear)
buttonclear.place(x = 260, y = 45, height = 20, width = 100)

list_num = Listbox()
list_num.place(x = 120, y = 45, height = 200, width = 130)

window.mainloop()