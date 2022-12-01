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

def main():
    again = True
    while again == True:
        print("1) Add to file\n2) View all records\n3) Quit Program\n\n")
        selection = int(input("Enter the number of your selection: "))
        if selection == 1:
            add_to_file()
        elif selection == 2:
            view_records()
        elif selection == 3:
            again = False
        else:
            print("Please choose a valid option")

main()