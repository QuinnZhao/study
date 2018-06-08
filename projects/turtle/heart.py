def heart_1(t, x, y):
    from math import sin, pi, cos
    A = 100
    t.up()
    t.goto(A + x , y)
    t.down()
    t.begin_fill()
    t.color('red','pink')
    for i in range(1,360):
        rad_i =  i * pi / 180
        r = A * (1 - sin(rad_i))
        x_i = r * cos(rad_i) + x
        y_i = r * sin(rad_i) + y
        t.goto(x_i,y_i)
    t.end_fill()
    
def heart_2(t, x, y, size=100):
    from math import sin, pi, cos
    if not size:
        A  = 100
    else:
        A = size
    t.up()
    t.goto(x , y)
    t.down()
    t.begin_fill()
    t.color('red','pink')
    for i in range(1,360):
        rad_i =  i * pi / 180
        r = A * (1 - cos(rad_i))
        x_i = r * cos(rad_i) + x
        y_i = r * sin(rad_i) + y
        t.goto(x_i,y_i)
    t.end_fill()
    
def heart_3(t, x, y, size=100):
    from math import sin, pi, cos
    if not size:
        A = 100
    else:
        A = size
    t.up()
    t.goto(2*A + x , y)
    t.down()
    t.begin_fill()
    t.color('red','pink')
    for i in range(1,360):
        rad_i =  i * pi / 180
        r = A * (1 + cos(rad_i))
        x_i = r * cos(rad_i) + x
        y_i = r * sin(rad_i) + y
        t.goto(x_i,y_i)
    t.end_fill()
    
def heart_4(t, x, y, size=100):
    from math import sin, pi, cos
    if not size:
        A = 100
    else:
        A = size
    t.up()
    t.goto(A + x , y)
    t.down()
    t.begin_fill()
    t.color('red','pink')
    for i in range(1,360):
        rad_i =  i * pi / 180
        r = A * (1 + sin(rad_i))
        x_i = r * cos(rad_i) + x
        y_i = r * sin(rad_i) + y
        t.goto(x_i,y_i)
    t.end_fill()
    
def heart_5(t, x, y, size=50):
    from math import sin, pi, cos, sqrt
    if not size:
        A = 50
    else:
        A = size
    t.up()
    t.goto(2 * A + x , y)
    t.down()
    t.begin_fill()
    t.color('red','pink')
    for i in range(1,360):
        rad_i =  i * pi / 180
        r = A * (sin(rad_i)* sqrt(abs(cos(rad_i)))/(sin(rad_i) + 7/5) - 2 * sin(rad_i) + 2)
        x_i = r * cos(rad_i) + x
        y_i = r * sin(rad_i) + y
        t.goto(x_i,y_i)
    t.end_fill()
    
def heart_6(t, x, y, size=100):
    from math import sin, pi, cos, acos
    if not size:
        A = 100
    else:
        A = size
    t.up()
    t.goto(pi/2 * A + x , y)
    t.down()
    t.begin_fill()
    t.color('red','pink')
    for i in range(1,360):
        rad_i =  i * pi / 180
        r = A * acos(sin(rad_i))
        x_i = r * cos(rad_i) + x
        y_i = r * sin(rad_i) + y
        t.goto(x_i,y_i)
    t.end_fill()

if __name__ == '__main__':
    import turtle, time
    turtle.title('heart')
    turtle.speed(1)
    heart_1(turtle, 0, 0)
    time.sleep(2)
    turtle.clear()
    heart_2(turtle, 0, 0)
    time.sleep(2)
    turtle.clear()
    heart_3(turtle, 0, 0)
    time.sleep(2)
    turtle.clear()
    heart_4(turtle, 0, 0)
    time.sleep(2)
    turtle.clear()
    heart_5(turtle, 0, 0)
    time.sleep(3)
    turtle.clear()
    heart_6(turtle, 0, 0)
    turtle.mainloop()
        