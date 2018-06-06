import turtle


def square_1(t, x, y, length):
    # 常规方法画正方形
    t.up()
    t.goto(x, y)
    t.down()
    for i in range (4):
        t.fd(length)
        t.left(90)


def square_2(t, x, y, length):
    # 采用画圆内切正方形的方式画正方形
    from math import sqrt
    t.up()
    t.goto(x,y)
    t.setheading(-45)
    t.down()
    t.circle(length/sqrt(2), steps=4)


def circle_(t, center_x, center_y, radius, heading=0):
    t.up()
    t.goto(center_x, center_y - radius)
    t.setheading(heading)
    t.down()
    t.circle(radius)


if __name__ == '__main__':
    turtle.speed('slowest')
    turtle.bgcolor('gray')
    turtle.pencolor('red')
    turtle.setheading(45)
    square_1(turtle, 0, 0, 100)
    turtle.pencolor('white')
    square_2(turtle, 0, 0, 100)
    turtle.pencolor('pink')
    circle_(turtle,0, 0, 50)
    # turtle.setheading(0)
    # turtle.hideturtle()
    turtle.mainloop()