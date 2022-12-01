import turtle
#3 square

turtle.penup()
turtle.backward(200)
turtle.pendown()
turtle.color("black","red")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(150)
turtle.pendown()

turtle.color("black","green")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.penup()
turtle.forward(150)
turtle.pendown()

turtle.color("black","blue")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

    
    
turtle.exitonclick()
