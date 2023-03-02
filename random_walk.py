import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
def random_colors():
    r=random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    return(r,b,g)

for _ in range(200):
    tim.pencolor(random_colors())
    tim.forward(30)
    tim.setheading(random.choice(directions))
