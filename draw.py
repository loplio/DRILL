import turtle
count = 0
count_2 = 0
while(count < 6):
    turtle.penup() 
    turtle.goto(0,count * 30)
    turtle.pendown()
    turtle.forward(150)
    count = count + 1
turtle.left(90)
while(count_2 < 6):
    turtle.penup() 
    turtle.goto(count_2 * 30,0)
    turtle.pendown()
    turtle.forward(150)
    count_2 = count_2 + 1
