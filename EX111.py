import csv

file = open("F:\\python\\Python by Examples\\Books.csv","w")
newRecord = "To Kill A Mockingbird, Harper Lee, 1960\n"
file.write(str(newRecord))
newRecord = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(newRecord))
newRecord = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(newRecord))
newRecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(newRecord))
newRecord = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(newRecord))
file.close()