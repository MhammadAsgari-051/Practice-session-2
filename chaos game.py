import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)
A = (-200, -150)
B = (200, -150)
C = (0, 196)

vertices = [A, B, C]
t = turtle.Turtle()
t.speed(0)
t.color("white")
t.penup()
t.goto(A)
t.pendown()
t.goto(B)
t.goto(C)
t.goto(A)
t.hideturtle()
x = 0
y = 0
p = turtle.Turtle()
p.hideturtle()
p.penup()
p.speed(0)
for i in range(5000):
    vertex = random.choice(vertices)
    x_new = (x + vertex[0]) / 2
    y_new = (y + vertex[1]) / 2
    x = x_new
    y = y_new
    p.goto(x, y)
    p.dot(2, "lime")

screen.update()
turtle.done()