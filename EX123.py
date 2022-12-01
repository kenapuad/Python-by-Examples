import csv

def add_to_file():
    file = open("F:\\python\\Python by Examples\\Salaries.csv","a+")
    name = input("Name: ")
    salary = input("Salary: ")
    abc = name + ", " + salary + "\n"
    file.write(abc)
    file.close()

def view_records():
    file = open("F:\\python\\Python by Examples\\Salaries.csv","r+")
    for row in file:
        print(row)

def delete_rec():
    file = open("F:\\python\\Python by Examples\\Salaries.csv","r")
    x = 0
    tmp = []
    for row in file:
        tmp.append(row)
    file.close()
    for row in tmp:
        print(x,row)
        x = x + 1
    row_del = int(input("Enter row to delete: "))
    del tmp[row_del]
    file = open("F:\\python\\Python by Examples\\Salaries.csv", "w")
    for row in tmp:
        file.write(row)
    file.close()

def main():
    again = True
    while again == True:
        print("1) Add to file\n2) View all records\n3) Delete a Record\n4) Quit Program\n\n")
        selection = input("Enter the number of your selection: ")
        if selection == "1":
            add_to_file()
        elif selection == "2":
            view_records()
        elif selection == "3":
            delete_rec()
        elif selection == "4":
            again = False
        else:
            print("Please choose a valid option")

main()