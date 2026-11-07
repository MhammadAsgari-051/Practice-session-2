import turtle

t = turtle.Turtle()
t.speed(0)
t.color("green")
t.hideturtle()

def triangle(points, depth):

    if depth == 0:
        t.penup()
        t.goto(points[0])
        t.pendown()
        t.goto(points[1])
        t.goto(points[2])
        t.goto(points[0])

    else:
        A, B, C = points

        AB = ((A[0]+B[0])/2, (A[1]+B[1])/2)
        BC = ((B[0]+C[0])/2, (B[1]+C[1])/2)
        AC = ((A[0]+C[0])/2, (A[1]+C[1])/2)

        triangle([A, AB, AC], depth-1)
        triangle([AB, B, BC], depth-1)
        triangle([AC, BC, C], depth-1)

A = (-250, -200)
B = (250, -200)
C = (0, 230)

triangle([A, B, C], 5)

turtle.done()