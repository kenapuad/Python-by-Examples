sales = {"John": {"N":3056,"S":8463,"E":8441,"W":2694},
         "Tom":  {"N":4832,"S":6786,"E":4737,"W":3612},
         "Anne": {"N":5239,"S":4802,"E":5820,"W":1859},
         "Fiona":{"N":3904,"S":3645,"E":8821,"W":2451},
        }

print(sales)

name = input("Give a name: ")
region = input("Give a region: ")

print(f"{name}'s sales in {region} is ", sales[name][region])

name1 = input("Give a name you want to change: ")
region2 = input("Give a region you you want to alter: ")
salesfig = int(input("What sales: "))

sales[name1][region2] = salesfig

print(sales[name1])

