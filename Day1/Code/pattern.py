import turtle 

pen = turtle.Pen()


pen.color('red','yellow')
pen.speed(0)
pen.begin_fill()

for var in range(200) : 
     
    pen.circle(var)
    pen.left(90)

pen.end_fill()

turtle.exitonclick()
