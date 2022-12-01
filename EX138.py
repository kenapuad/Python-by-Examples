from tkinter import *

window = Tk()
window.title("It's MEEEEEE")
window.geometry("1000x900")


def new():
    photo = PhotoImage(file = "def.gif")
    photobox = Label(window, image = photo)
    photobox.image = photo
    photobox.place(x = 50, y = 150, height = 695, width= 900)

photo1 = PhotoImage(file = "1.gif")
photo2 = PhotoImage(file = "2.gif")
photo3 = PhotoImage(file = "3.gif")

def photoget():
    selection = select.get()    
    if selection == "1":
        
        photobox = Label(window, image = photo1)
        photobox.place(x = 50, y = 150, height = 695, width= 900)
    elif selection == "2":
        photobox = Label(window, image = photo2)
        photobox.place(x = 50, y = 150, height = 695, width= 900)
    elif selection == "3":
        photobox = Label(window, image = photo3)
        photobox.place(x = 50, y = 150, height = 695, width= 900)
    else:
        photo = PhotoImage(file = "def.gif")
        photobox.image = photo

select = StringVar(window)
select.set("Select")
photolist = OptionMenu(window, select, "1","2","3")
photolist.place(x = 50, y = 50)

selectbutton = Button(text= "GO", command= photoget)
selectbutton.place(x = 150, y = 50, height= 29, width=50)

new()

window.mainloop()
