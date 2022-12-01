import csv
import string

def passwordcheck():
    global password
    password = input("Enter new password: ")
    pw_strength = 0
    if len(password) >= 8:
        pw_strength = pw_strength + 1
    upper = 0
    for char in password:
        if char.isupper():
            upper = upper + 1
    if upper > 0:
        pw_strength = pw_strength + 1
    lower = 0
    for char in password:
        if char.islower():
            lower = lower + 1
    if lower > 0:
        pw_strength = pw_strength + 1
    digit = 0
    for char in password:
        if char.isdigit():
            digit = digit + 1
    if digit > 0:
        pw_strength = pw_strength + 1
    punct = 0
    for char in password:
        if char in string.punctuation:
            punct = punct + 1
    if punct > 0:
        pw_strength = pw_strength + 1
    if pw_strength < 3:
        print("Password is too weak, please enter a new one: ")
        passwordcheck()
    elif pw_strength > 2 and pw_strength < 5:
        option = input("This password could be improved, try again? (y/n)")
        if option == "y":
            passwordcheck()
        elif option == "n":
            pass
    else:
        pass
    
def createnew():
    file = list(csv.reader(open("un_pw.csv")))
    tmp = []
    try:
        for col in file:
            tmp.append(col[0])
    except:
        print("Empty List")
    username = input("Enter new User ID: ")
    while username in tmp:
        print(username,"already used")
        username = input("Enter new User ID: ")
    passwordcheck()
    file = open("un_pw.csv", "a+")
    new_entry = username + "," + password + "\n"
    file.write(str(new_entry))
    file.close()

def changepass():
    file = list(csv.reader(open("un_pw.csv")))
    tmp = []
    try:
        for col in file:
            tmp.append(col[0])
    except:
        print("Empty List")
    username = input("Enter User ID for password change: ")
    while username not in tmp:
        print("User ID not in file!")
        username = input("Enter User ID for password change (or X to main menu): ")
        if username.upper() == "X":
            main()
    passwordcheck()
    x = tmp.index(username)
    file = list(csv.reader(open("un_pw.csv")))
    tmp1 = []
    for row in file:
        tmp1.append(row)
    tmp1[x][1] = password
    file = open("un_pw.csv","w+")
    x = 0
    for row in tmp1:
        new_data = tmp1[x][0] + "," + tmp1[x][1] + "\n"
        file.write(new_data)
        x = x + 1
    file.close()

def displayall():
    file = list(csv.reader(open("un_pw.csv")))
    tmp = []
    try:
        for col in file:
            tmp.append(col[0])
    except:
        print("Empty file!")
    print("\nUser IDs:")
    for i in tmp:
        print(i)
    print("~~~~~")

def main():
    while True:
        print("1) Create a new User ID\n2) Change a password\n3) Display all User IDs\n4) Quit\n")
        selection = input("Enter Selection: ")
        if selection == "1":
            createnew()
        elif selection == "2":
            changepass()
        elif selection == "3":
            displayall()
        elif selection == "4":
            return False
        else:
            print("Please select a valid option: ")

main()