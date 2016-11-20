from turtle import right, left, forward, penup, pendown, exitonclick
#posun kurzoru do prava
penup()
left(180)
forward(250)
right(180)
pendown()

#zde se kreslí hvězdičky
for j in range(10):
    for i in range(12):
        forward(50)
        left(180*(1-(2/12)))
    penup()
    forward(70)
    pendown()
exitonclick()
