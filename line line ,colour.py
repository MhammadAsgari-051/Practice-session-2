import turtle
from random import random

t = turtle.Turtle()

for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)

    t.pencolor(random(), random(), random())

    t.right(angle)
    t.fd(steps)

turtle.done()