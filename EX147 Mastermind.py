import random

colorlist = ["RED","BLUE","YELLOW"]

colors = []
for i in range(3):
    colors.append(colorlist[random.randint(0,len(colorlist)-1)])

print(colors)

tryagain = True
attempt = 0

while tryagain == True:
    score = 0
    order = 0    
    tmpcolors = colors
    guess = []
    #print(tmpcolors)
    for i in range(3):
        guess.append(input(f"Guess color number {i+1}: ").upper())
    print(guess)
    for x in range(0,len(tmpcolors)):
        if guess[x] == tmpcolors[x]:
            score = score + 1
    tmpcolors2 = []  
    guess2 = []
    for y in range(0,len(tmpcolors)):
        if guess[y] != tmpcolors[y]:
            tmpcolors2.append(tmpcolors[y])
            guess2.append(guess[y])
    #print(tmpcolors2)
    #print(guess2)
    if len(tmpcolors2) > 0:
        for a in tmpcolors2:
            for b in guess2:
                #print(a,b)
                if a == b:
                    order = order + 1
    correct_choice = 0
    for x in range(3):
        if guess[x] in colorlist:
            correct_choice = correct_choice + 1
    if correct_choice == 3:
        attempt = attempt + 1
    else:
        print("One of your choice is not in list")  
    print("Correct guesses", score)
    print("Correct color incorrect order", order)
    if score == 3:
        tryagain = False
        #tmpcolors = colors


print("You attempted",attempt)


    
    


