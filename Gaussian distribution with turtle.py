import turtle
import math

screen = turtle.Screen()
screen.setup(900, 600)
screen.bgcolor("white")
screen.title("Gaussian Distribution")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# رسم محور افقی
t.penup()
t.goto(-350, 0)
t.pendown()
t.goto(350, 0)

# رسم منحنی گوسی
t.penup()

for x in range(-300, 301):
    y = 200 * math.exp(-(x / 100) ** 2 / 2)

    if x == -300:
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

turtle.done()