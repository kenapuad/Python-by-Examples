def getNumber():
    num = int(input("Enter a number: "))
    return num
def count(num):
    for i in range(1,num+1):
        print(i)
def main():
    num = getNumber()
    count(num)

main()