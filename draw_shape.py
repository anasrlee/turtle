import turtle as t
import random

timmy=t.Turtle()
x=360
i=1

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range (3,15):
    x=360/i
    timmy.color(random_color())
    for _ in range(i):
        timmy.forward(40)
        timmy.left(x)

def draw_shape(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        timmy.forward(40)
        timmy.right(angle)

for shape_side_n in range(3, 15):
    timmy.color(random_color())
    draw_shape(shape_side_n)
