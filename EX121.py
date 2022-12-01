def add():
    name = input("Add name: ")
    namelist.append(name)
    return namelist

def change():
    x = 0
    for i in namelist:
        print(x,i)
        x = x + 1
    amend = int(input("What index to change: "))
    namelist[amend] = input("What name to replace: ")
    return namelist

def delete():
    x = 0
    for i in namelist:
        print(x,i)
        x = x + 1
    remove = int(input("What index to remove: "))
    del namelist[remove]
    return namelist

def view():
    print("Names: ")
    x = 0
    if len(namelist) < 1:
        print("No names yet")
    else:
        for i in namelist:
            print(x,i)
            x = x + 1
    print("~~~~~~~")
    return namelist

def main():
    exit = False
    while exit == False:
        print("Welcome to Main: ")
        print("1) Add")
        print("2) Change")
        print("3) Delete")
        print("4) View")
        print("5) Exit")
        choice = int(input("Enter option: "))
        if choice == 1:
            namelist = add()
        elif choice == 2:
            namelist = change()
        elif choice == 3:
            namelist = delete()
        elif choice == 4:
            namelist == view()
        elif choice == 5:
            exit = True
        else:
            print("Choose a valid option!")
        
namelist = []
main()

