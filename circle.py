import turtle as t
import random

tim=t.Turtle()
t.colormode(255)

tim.speed("fastest")
tim.pensize(5)
def random_colors():
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    return(r,b,g)

for i in range (360):
    tim.pencolor(random_colors())
    tim.setheading(i)
    tim.circle(100)
    
screen = t.Screen()
screen.exitonclick()
