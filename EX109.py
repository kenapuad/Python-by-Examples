print("1) Create a new file")
print("2) Display the file")
print("3) Add a new item to the file")

tryagain = True
while tryagain == True:
    selection = int(input("Enter a selection 1, 2 or 3:\n"))
    if selection == 1:
        subject = input("Enter a subject: ")
        file = open("F:\\python\\Python by Examples\\Subject.txt","w")
        file.write(subject + "\n")
        file.close()
        tryagain = False
    elif selection == 2:
        file = open("F:\\python\\Python by Examples\\Subject.txt","r")
        print(file.read())
        file.close()
        tryagain = False
    elif selection == 3:
        subject = input("Enter a subject: ")
        file = open("F:\\python\\Python by Examples\\Subject.txt","a")
        file.write(subject + "\n")
        file.close()
        file = open("F:\\python\\Python by Examples\\Subject.txt","r")
        print(file.read())
        file.close()
        tryagain = False

print("Thank you!")