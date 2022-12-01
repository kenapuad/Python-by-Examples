import random

def add():
    a = random.randint(5, 20)
    b = random.randint(5, 20)
    correct_ans = a + b
    user_ans = int(input(f"What is the sum of {a} and {b}: "))
    return correct_ans, user_ans

def subtract():
    a = random.randint(25, 50)
    b = random.randint(1, 25)
    correct_ans = a - b
    user_ans = int(input(f"What is the difference of {a} and {b}: "))
    return correct_ans, user_ans

def answer(correct_ans,user_ans):
    if correct_ans == user_ans:
        print("Correct!")
    else:
        print("Correct answer is:",correct_ans)

def main():
    print("1) Addition\n2)Subtraction")
    choice = int(input("Enter 1 or 2: "))
    tryagain = True
    while tryagain == True:
        if choice == 1:
            correct_ans, user_ans = add()
            answer(correct_ans,user_ans)
            tryagain = False
        elif choice == 2:
            correct_ans, user_ans = subtract()
            answer(correct_ans,user_ans)
            tryagain = False
        else:
            choice = int(input("Try Again: "))

main()