countries = ("Philippines","Japan","Taiwan","Hong Kong","Canada")
print(countries)
x = input("Enter one of the countries shown: ")
print(x,"is at index number",countries.index(x.capitalize()))
y = int(input("Enter a number 0 to 4: "))
print("Country in position",y,"is",countries[y])