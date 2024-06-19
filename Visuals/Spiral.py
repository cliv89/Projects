import turtle as t
import colorsys

t.bgcolor('black')
t.tracer(100)
t.pensize(1)
x = 0.5

for i in range (500):
    c = colorsys.hsv_to_rgb(x, 1, 1)
    x += 0.008
    t.fillcolor(c)
    t.begin_fill()
    t.fd(i)
    t.lt(100)
    t.circle(30)
    
    for j in range(2):
        t.fd(i * j)
        t.rt(109)
    t.end_fill()
