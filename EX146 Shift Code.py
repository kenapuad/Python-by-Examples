import string
loweralpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upperalpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
digits = [0,1,2,3,4,5,6,7,8,9]


def option1():
    message = input("Enter a message to encode: ")
    step = int(input("Enter an integer to code (1-10): "))
    encodedmsg = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                x = loweralpha.index(char)
                y = x + step
                if y > 25:
                    z = y - 26
                    encodedmsg = encodedmsg + loweralpha[z]
                else:
                    encodedmsg = encodedmsg + loweralpha[y]
            elif char.isupper():
                x = upperalpha.index(char)
                y = x + step
                if y > 25:
                    z = y - 26
                    encodedmsg = encodedmsg + upperalpha[z]
                else:
                    encodedmsg = encodedmsg + upperalpha[y]
        elif char.isdigit():
            x = digits.index(int(char))
            y = x + step
            if y > 9:
                z = y - 10
                encodedmsg = encodedmsg + str(digits[z])
            else:
                encodedmsg = encodedmsg + str(digits[y])
        elif char.isspace():
            encodedmsg = encodedmsg + " "
        elif char in string.punctuation:
            encodedmsg = encodedmsg + char
    print("Your encoded message is: ",encodedmsg)

def option2():
    message = input("Enter a message to decode: ")
    step = int(input("Enter an integer to code1-10: "))
    decodemsg = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                x = loweralpha.index(char)
                y = x - step
                if y < 0:
                    z = y + 26
                    decodemsg = decodemsg + loweralpha[z]
                else:
                    decodemsg = decodemsg + loweralpha[y]
            elif char.isupper():
                x = upperalpha.index(char)
                y = x - step
                if y < 0:
                    z = y + 26
                    decodemsg = decodemsg + upperalpha[z]
                else:
                    decodemsg = decodemsg + upperalpha[y]
        elif char.isdigit():
            x = digits.index(int(char))
            y = x - step
            if y < 0:
                z = y + 10
                decodemsg = decodemsg + str(digits[z])
            else:
                decodemsg = decodemsg + str(digits[y])
        elif char.isspace():
            decodemsg = decodemsg + " "
        elif char in string.punctuation:
            decodemsg = decodemsg + char
    print("Your encoded message is: ",decodemsg)

def main():
    tryagain = True
    while tryagain == True:
        print("1) Make a code\n2) Decode a message\n3) Quit\n")
        selection = input("Enter your selection: ")
        if selection == "1":
            option1()
        elif selection == "2":
            option2()
        elif selection == "3":
            tryagain = False
        else:
            print("Invalid Selection!")

main()
