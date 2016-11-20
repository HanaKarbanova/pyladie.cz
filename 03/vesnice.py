#zde se kreslí vesnice

from turtle import forward, left, right, penup, pendown, exitonclick
from math import sqrt
strana=float(input('Jak je dlouhá strana?:'))
velikost = int(input('Kolik chceš baráčků:'))
penup()
left(180)
forward(300)
pendown()
right(180)
#setpoint(300)

for i in range(velikost):
    left(90)
    forward(strana)
    right(135)
    forward(sqrt(2)*strana)
    right(135)
    forward(strana)
    right(135)
    forward(sqrt(2)*strana)
    left(135)
    forward(strana)
    right(135)
    forward((sqrt(2)*strana)/2)
    right(90)
    forward((sqrt(2)*strana)/2)
    right(45)
    forward(strana)
    left(90)
    forward(20)

print("Vesnice postavena;o)")
exitonclick()
