file = open("F:\\python\\Python by Examples\\Names.txt","r")
print(file.read())
file.close()

file = open("F:\\python\\Python by Examples\\Names.txt","r")
name = input("Type the name to remove: ")
name = name + "\n"

for row in file:
    if row != name:
        file = open("F:\\python\\Python by Examples\\Names2.txt","a")
        file.write(row)
        file.close()
    
file.close()