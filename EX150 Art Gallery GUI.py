import sqlite3
from tkinter import *

def addartist():
    newname = artistname.get()
    newaddress = artistadd.get()
    newtown = artisttown.get()
    newcounty = artistcounty.get()  
    newpostcode = artistpostcode.get()
    cursor.execute("""INSERT INTO Artists (name, address, town, county, postcode)
VALUES (?,?,?,?,?)""",(newname,newaddress,newtown,newcounty,newpostcode))
    db.commit()
    artistname.delete(0, END)
    artistadd.delete(0, END)
    artisttown.delete(0, END)
    artistcounty.delete(0, END)
    artistpostcode.delete(0, END)
    artistname.focus()

def clearartist():
    artistname.delete(0, END)
    artistadd.delete(0, END)
    artisttown.delete(0, END)
    artistcounty.delete(0, END)
    artistpostcode.delete(0, END)
    artistname.focus()

def addart():
    newartname = artname.get()
    newtitle = arttitle.get()
    newmedium = medium.get()
    newprice = artprice.get()
    cursor.execute("""INSERT INTO Art (artistid,title,medium,price)
VALUES (?,?,?,?)""", (newartname,newtitle,newmedium,newprice))
    db.commit()
    artname.delete(0, END)
    arttitle.delete(0, END)
    medium.set("")
    artprice.delete(0, END)
    artname.focus()
    
def clearwindow():
    outputwindow.delete(0, END)

def viewartists():
    cursor.execute("SELECT * FROM Artists")
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2])+ ", " + str(x[3])+ ", " + str(x[4])  + ", " + x[5] + "\n"
        outputwindow.insert(END,newrecord)

def viewart():
    cursor.execute("SELECT * FROM Art")
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2])+ ", " + str(x[3])+ ", $" + str(x[4])  + "\n"
        outputwindow.insert(END,newrecord)

def searchartistoutput():
    selectedartist = searchartist.get()
    cursor.execute("SELECT name FROM Artists WHERE artistid=?",[selectedartist])
    for x in cursor.fetchall():
        outputwindow.insert(END,x)
        cursor.execute("SELECT * FROM Art WHERE artistid=?",[selectedartist])
        for x in cursor.fetchall():
            newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2])+ ", " + str(x[3])+ ", $" + str(x[4])  + "\n"
            outputwindow.insert(END,newrecord)
    searchartist.delete(0, END)
    searchartist.focus()

def searchmediumoutput():
    selectedmedium = medium2.get()
    cursor.execute("""SELECT Art.pieceid, Artists.name, Art.title, Art.price "
FROM Artists,Art WHERE Artists.artistid=Art.artistid AND Art.medium = ?""",[selectedmedium])
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2])+ ", " + str(x[3])+ ", $" + str(x[4])  + "\n"
        outputwindow.insert(END,newrecord)
    medium2.set("")

def searchbyprice():
    minprice = selectmin.get()
    maxprice = selectmax.get()
    cursor.execute("""SELECT Art.pieceid, Artists.name, Art.title, Art.price "
FROM Artists,Art WHERE Artists.artistid=Art.artistid AND Art.price>=? AND Art.price<=?""",[minprice,maxprice])
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2])+ ", " + str(x[3])+ ", $" + str(x[4])  + "\n"
        outputwindow.insert(END,newrecord)
    selectmin.delete(0, END)
    selectmax.delete(0, END)
    selectmin.focus()

def sold():
    file = open("SoldArt.txt","a")
    selectedpiece = soldpiece.get()
    cursor.execute("SELECT * FROM Art WHERE pieceid=?",[selectedpiece])
    for x in cursor.fetchall():
        newrecord = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2])+ ", " + str(x[3])+ ", " + str(x[4])  + "\n"
        file.write(newrecord)
    file.close()
    cursor.execute("DELETE FROM Art WHERE pieceid =?",[selectedpiece])
    db.commit()

def clearart():
    pass

with sqlite3.connect("Art Gallery.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Artists(
    artistid integer PRIMARY KEY,
    name text,
    address text,
    town text,
    county text,
    postcode text);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Art(
    pieceID integer PRIMARY KEY,
    artistID integer,
    title text,
    medium text,
    price integer);""")

window = Tk()
window.geometry("1220x600")
window.title("Art Gallery")

title1 = Label(text= "Enter new details:")
title1.place(x = 10, y= 10, height= 25, width= 100)
artistnamelbl = Label(text="Name:")
artistnamelbl.place(x = 30, y= 40, height= 25, width= 80)
artistname = Entry(text="")
artistname.place(x = 110, y= 40, height= 25, width= 200)
artistname.focus()
artistaddlbl = Label(text="Address:")
artistaddlbl.place(x = 310, y= 40, height= 25, width= 80)
artistadd = Entry(text = "")
artistadd.place(x = 390, y= 40, height= 25, width= 200)
artisttownlbl = Label(text="Town:")
artisttownlbl.place(x = 590, y= 40, height= 25, width= 100)
artisttown = Entry(text = "")
artisttown.place(x = 670, y= 40, height= 25, width= 100)
artistcountylbl = Label(text="County:")
artistcountylbl.place(x = 770, y= 40, height= 25, width= 80)
artistcounty = Entry(text= "")
artistcounty.place(x = 850, y= 40, height= 25, width= 100)
artistpostcodelbl = Label(text="PostCode:")
artistpostcodelbl.place(x = 950, y= 40, height= 25, width= 80)
artistpostcode = Entry(text="")
artistpostcode.place(x = 1030, y= 40, height= 25, width= 100)
addbtn = Button(text="Add Artist", command= addartist)
addbtn.place(x = 100, y= 80, width= 130, height = 25)
clearbtn = Button(text= "Clear Artist", command = clearartist)
clearbtn.place(x = 250, y = 80, width = 130, height= 25)

artnamelbl = Label(text= "Artist ID:")
artnamelbl.place(x = 30, y= 120, height= 25, width= 80)
artname = Entry()
artname.place(x = 110, y= 120, height= 25, width= 50)
arttitlelbl = Label(text="Title:")
arttitlelbl.place(x = 200, y= 120, height= 25, width= 80)
arttitle = Entry()
arttitle.place(x = 280, y= 120, height= 25, width= 280)
artmediumlbl = Label(text= "Medium:")
artmediumlbl.place(x = 590, y= 120, height= 25, width= 80)
medium = StringVar(window)
artmedium = OptionMenu(window, medium, "Oil","Watercolour","Ink","Acrylic")
artmedium.place(x = 670, y= 120, height= 25, width= 100)
artpricelbl = Label(text = "Price:")
artpricelbl.place(x = 770, y= 120, height= 25, width= 80)
artprice = Entry()
artprice.place(x = 850, y= 120, height= 25, width= 100)
addartbtn = Button(text= "Add Piece", command= addart)
addartbtn.place(x = 110, y = 150, width= 130, height= 25)
clearartbtn = Button(text = "Clear Piece", command= clearart)
clearbtn.place(x=250, y=150, width=130, height=25)

outputwindow = Listbox()
outputwindow.place(x = 10, y= 200, width=1000, height=350)

clearoutputwindow = Button(text= "Clear Output", command= clearwindow)
clearoutputwindow.place(x= 1020, y= 200, width= 155, height= 25)
viewallartists = Button(text= "View All Artists", command= viewartists)
viewallartists.place(x= 1020, y= 230, width=155, height= 25)
viewallart = Button(text = "View All Art", command= viewart)
viewallart.place(x = 1020, y= 260, width=155, height= 25)
searchartist = Entry()
searchartist.place(x = 1020, y= 300, width=50, height= 25)
searchartistbtn = Button(text= "Search by Artist", command= searchartistoutput)
searchartistbtn.place(x = 1075, y= 300, width=100, height= 25)
medium2 = StringVar(window)
searchmedium = OptionMenu(window, medium2, "Oil","Watercolour","Ink","Acrylic")
searchmedium.place(x = 1020, y= 330, width=100, height= 25)
searchmediumbtn = Button(text= "Search", command= searchmediumoutput)
searchmediumbtn.place(x = 1125, y= 330, width=50, height= 25)
minlbl = Label(text = "Min:")
minlbl.place(x = 1020, y= 360, width=75, height= 25)
maxlbl = Label(text = "Max:")
maxlbl.place(x = 1100, y= 360, width=75, height= 25)
selectmin = Entry()
selectmin.place(x = 1020, y= 380, width=75, height= 25)
selectmax = Entry()
selectmax.place(x = 1100, y= 380, width=75, height= 25)
searchpricebtn = Button(text="Search by Price", command= searchbyprice)
searchpricebtn.place(x = 1020, y= 410, width= 155, height=25)
soldpiece = Entry()
soldpiece.place(x = 1020, y= 450, width= 50, height=25)
soldbtn = Button(text= "Sold", command=sold)
soldbtn.place(x = 1075, y= 450, width= 100, height= 25)

window.mainloop()
db.close()
