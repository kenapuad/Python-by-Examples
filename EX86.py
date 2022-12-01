newpass = input("Input a new password: ")
repass = input("Enter it again: ")
if newpass == repass:
    print("Thank you!")
elif newpass.lower() == repass.lower():
    print("Cases incorrect")
else:
    print("Password not match")
