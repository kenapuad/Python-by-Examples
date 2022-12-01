word = input("Type a word in uppercase:\n")

upper = False

while upper == False:
    word = input("Try again:\n")
    if word.isupper():
        upper = True

print("FINAL WORD:",word)