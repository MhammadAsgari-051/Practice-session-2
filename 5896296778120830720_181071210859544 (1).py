import turtle as t
import random
t.speed(0)
t.hideturtle()
t.tracer(0)
t.pu()
rules = [(2,(0,0,.50),(0,.27,0)),
         (15,(-.14,.26,.57),(.25,.22,-.04)),
         (13,(.17,-.21,.41),(.22,.18,.09)),
         (70,(.78,.03,.11),(-.03,.74,.27))]
n = 30000
s = 600
x,y = 0,0
probability = [r[0] for r in rules]
for _, (a,b,c),(d,e,f) in random.choices(rules, probability, k=n):
    x,y = a*x + b*y + c, d*x + e*y + f
    t.goto((x - 0.5)*s , (y - 0.5)*s)
    t.dot(2, 'green')
t.update()
t.done()