from turtle import *


def dreieck(lengh, levels):
    if levels == 0:
        return 
    else:
        for i in range(3):
            forward(lengh)
            right(120)
            dreieck(lengh/2, levels-1)


screensize(1000,1000)
penup()
goto(-500,450)
pendown()
hideturtle()
speed(1000000000)
dreieck(1000,6)