import turtle
interval = 50
def drunken_left():
    turtle.setheading(180)
    turtle.forward(interval)
    turtle.stamp()
def drunken_right():
    turtle.setheading(0)
    turtle.forward(interval)
    turtle.stamp()
def drunken_up():
    turtle.setheading(90)
    turtle.forward(interval)
    turtle.stamp()
def drunken_down():
    turtle.setheading(270)
    turtle.forward(interval)
    turtle.stamp()
def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.stamp();
turtle.onkey(drunken_left,'Left')
turtle.onkey(drunken_right,'Right')
turtle.onkey(drunken_up,'Up')
turtle.onkey(drunken_down,'Down')
turtle.onkey(restart,'Escape')
turtle.listen()
