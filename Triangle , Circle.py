import turtle

t = turtle.Turtle()
t.speed(5)
t.color("green")
t.pensize(3)

A = (-180, -120)
B = (180, -120)
C = (0, 190)

t.penup()
t.goto(A)
t.pendown()
t.goto(B)
t.goto(C)
t.goto(A)

def draw_circle(x, y):
    t.penup()
    t.goto(x, y - 60)
    t.pendown()
    t.circle(60)
 
draw_circle(-180, -120)
draw_circle(180, -120)
draw_circle(0, 190)

t.hideturtle()
turtle.done()