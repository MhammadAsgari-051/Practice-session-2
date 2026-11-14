import turtle

def draw_triangle(x0, y0, x1, y1, x2, y2):

    t = turtle.Turtle()
    t.speed(2)

    t.penup()
    t.goto(x0, y0)
    t.pendown()

    t.goto(x1, y1)
    t.goto(x2, y2)
    t.goto(x0, y0)

    turtle.done()


draw_triangle(-100, -50, 100, -50, 0, 100)