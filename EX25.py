fname = input("What's your first name?\n")
if len(fname) < 5:
    lname = input("What's your last name?\n")
    wname = fname+lname
    print(wname.upper())
else:
    print(fname.lower())
