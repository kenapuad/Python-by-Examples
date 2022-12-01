countries = ("Philippines","Japan","Taiwan","Hong Kong","Canada")
print(countries)
x = input("Enter one of the countries shown: ")
print("Your choice is no.",countries.index(x.capitalize())+1,"in the list")