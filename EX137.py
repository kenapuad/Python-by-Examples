from tkinter import *

window = Tk()
window.title("Name and Gender")
window.geometry("300x240")

def submit():
    name = name_entry.get()
    gen = gender.get()
    entry = str(name + ", " + gen)
    namelist.insert(END, entry)
    file = open("Name_Gender.txt","a+")
    file.write(entry + "\n")
    file.close()
    name_entry.delete(0, END)
    gender.set("Select")
    name_entry.focus()

def view():
    file = open("Name_Gender.txt", "r")
    print(file.read())

name_label = Label(text= "Name: ", justify= "left", bg= "light green")
name_label.place(x= 20, y= 20, height= 20, width= 75)

name_entry = Entry()
name_entry.place(x= 110, y= 20, height= 20, width= 120)

gender_label = Label(text= "Gender: ", justify= "left", bg= "light green")
gender_label.place(x= 20, y= 50, height= 20, width= 75)

gender = StringVar(window)
gender.set("Select")
gender_entry = OptionMenu(window,gender,"Male","Female")
gender_entry.place(x= 110, y= 50, height= 25, width= 120)

add_to_list = Button(text= "Submit", command= submit)
add_to_list.place(x= 20, y= 80, height = 20, width= 75)

namelist = Listbox()
namelist.place(x= 20, y= 110, height = 20, width= 120)

view_list = Button(text = "View", command= view)
view_list.place(x= 20, y= 140, height = 20, width= 120)

window.mainloop()
