from turtle import right, left, forward, exitonclick, penup, pendown

for i in range(4):
    for j in range(5+i):
        forward((200/(5+i)))
        left(180-(180*(1-2/(5+i))))
    penup()
    forward(80)
    pendown()


exitonclick()
