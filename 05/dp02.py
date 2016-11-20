from turtle import left, right, forward, exitonclick, penup, pendown
from math import sqrt
def nakresli_domecek(strana):

#levá strana
    left(90)
    forward(strana)
#příčka
    right(135)
    forward(sqrt(strana**2+strana**2))
#pravá strana
    left(45+90)
    forward(strana)
#strop
    left(90)
    forward(strana)
#střecha
    right(90+45)
    forward((sqrt(strana**2+strana**2)/2))
    right(90)
    forward((sqrt(strana**2+strana**2)/2))
#příčka
    right(90)
    forward(sqrt(strana**2+strana**2))
#podlaha
    left(135)
    forward(strana)

a=float(input("jak velký bude domeček:"))
left(180)
penup()
forward(250)
right(180)
pendown()
#nakreslíme domeček

for i in range(5):
    nakresli_domecek(a*i+10)
    forward(20)


exitonclick()
