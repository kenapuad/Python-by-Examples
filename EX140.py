import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor=db.cursor()

def view_phonebook():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

def add_to_phonebook():
    newID = int(input("Enter ID#: "))
    newFname = input("Enter First Name: ")
    newSname = input("Enter Surname: ")
    newphone = input("Enter Phone Number: ")    
    cursor.execute("""INSERT INTO Names(ID,FirstName,Surname,PhoneNumber)
        VALUES(?,?,?,?)""",(newID,newFname,newSname,newphone))
    db.commit()

def surname_search():
    sname = input("Enter Surname: ")
    cursor.execute("SELECT * FROM Names WHERE Surname = ?",[sname])
    for x in cursor.fetchall():
        print(x)

def del_to_phonebook():
    del_id = input("Enter ID to delete: ")
    cursor.execute("DELETE FROM Names WHERE ID = ?",[del_id])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()

def main():
    while True:
        print("Main Menu\n\n1) View phone book\n2) Add to phone book\n3) Search for surname\n4) Delete person from phone book\n5) Quit\n")
        selection = int(input("Enter your selection:\n"))    
        if selection == 1:
            view_phonebook()
        elif selection == 2:
            add_to_phonebook()
        elif selection == 3:
            surname_search()
        elif selection == 4:
            del_to_phonebook()
        elif selection == 5:
            return False
        else:
            selection = int(input("Incorrect selection!"))

main()
db.close()