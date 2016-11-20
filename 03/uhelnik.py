from turtle import forward, left, right, exitonclick
#pocet uhlu
n = int(input('Zadej počet uhlů:'))
#velikost strany
v=float(input("Jak velkou bude mít stranu:"))

for i in range(n):
    forward(v)
    left(180-(180*(1-2/n)))

exitonclick()
