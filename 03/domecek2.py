#zde se kresli domecek jednim tahem

from turtle import forward, left, right, penup, pendown, exitonclick
from math import sqrt
strana=float(input('Jak je dlouha strana?:'))
left(90)
#leva stena
forward(strana)
#sikmo doprava dolu
right(135)
forward(sqrt(2)*strana)
#zakladna
right(135)
forward(strana)
#sikmo do prava nahoru
right(135)
forward(sqrt(2)*strana)
#horni cast
left(135)
forward(strana)
#leva strana strechy
right(135)
forward((sqrt(2)*strana)/2)
#prava strana strechy
right(90)
forward((sqrt(2)*strana)/2)
#prava stena
right(45)
forward(strana)

exitonclick()
