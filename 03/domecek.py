#zde se kreslí domeček

from turtle import forward, left, right, penup, pendown, exitonclick
from math import sqrt
strana=float(input('Jak je dlouhá strana?:'))
for i in range(4):
    forward(strana)
    left(90)
for i in range(2):
    left(45 +i*90)
    forward(sqrt(2)*strana)
    left(135)
    penup()
    forward(strana)
    pendown()
for i in range(2):
    left(45 +i*45)
    forward((sqrt(2)*strana)/2)

exitonclick()
