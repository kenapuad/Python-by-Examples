import turtle
import random

turtle.pensize(4)

"""for j in range(random.randint(1,10)):
    turtle.right(random.randint(1,36))
    for i in range(random.randint(1,8)):
        turtle.forward(random.randint(20,100))    
        turtle.right(random.randint(1,45))"""

lines = random.randint(5,20)

for x in range(0,lines):
    length = random.randint(25,100)
    rotate = random.randint(1,365)
    turtle.forward(length)
    turtle.right(rotate)
    
turtle.exitonclick()
