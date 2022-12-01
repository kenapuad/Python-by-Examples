import random

def low_high():
    a = int(input("Input low number: "))
    b = int(input("Input high number: "))
    comp_num = random.randint(a, b)
    return comp_num

def guess_number():
    print("I am thinking of a number")
    guess = int(input("Can you guess that number? "))
    return guess


def if_correct(comp_num,guess):
    tryagain = True
    while tryagain == True:
        if comp_num == guess:
            print("You win")
            tryagain = False
        elif guess > comp_num:
            guess = int(input("Too high, try again: "))
        else:
            guess = int(input("Too low, try again: "))

def main():
    comp_num = low_high()
    guess = guess_number()
    if_correct(comp_num,guess)

main()

