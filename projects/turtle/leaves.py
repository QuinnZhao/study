def triple_leaves(t, x, y, size=100):
    from math import sin, pi, cos
    if not size:
        A = 100
    else:
        A = size
    t.up()
    t.goto(A + x, y)
    t.down()
    t.begin_fill()
    t.fillcolor('green')
    for i in range(1,360):
        rad_i =  i * pi / 180
        r = A * cos(3 * rad_i)
        x_i = r * cos(rad_i) + x
        y_i = r * sin(rad_i) + y
        t.goto(x_i,y_i)
    t.end_fill()
    
def q_leaves(t, x, y, size=100):
    from math import sin, pi, cos
    if not size:
        A = 100
    else:
        A = size
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.fillcolor('green')
    for i in range(1,360):
        rad_i =  i * pi / 180
        r = A * sin(2 * rad_i)
        x_i = r * cos(rad_i) + x
        y_i = r * sin(rad_i) + y
        t.goto(x_i,y_i)
    t.end_fill()
    
def magic_leaves(t, x, y, size=100):
    from math import sin, pi, cos
    if not size:
        A = 100
    else:
        A = size
    t.up()
    t.goto(2 * A + x, y)
    t.down()
    t.begin_fill()
    t.fillcolor('green')
    for i in range(1,360):
        rad_i =  i * pi / 180
        r = A * 2 * (1 - 3 * sin(rad_i)) * cos(6 * rad_i)
        x_i = r * cos(rad_i) + x
        y_i = r * sin(rad_i) + y
        t.goto(x_i,y_i)
    t.end_fill()
    
if __name__ == '__main__':
    import turtle, time
    turtle.title('leaves')
    turtle.speed(1)
    triple_leaves(turtle, 0, 0)
    time.sleep(3)
    turtle.clear()
    q_leaves(turtle, 0, 0)
    time.sleep(3)
    turtle.clear()
    magic_leaves(turtle, 0, 0, size=30)
    turtle.mainloop()