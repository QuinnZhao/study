def seed(t, x, y, size):
    t.up()
    t.goto(x,y)
    t.down()
    t.dot(size)


# 瓜皮、瓜瓤
def melon_rind(t, center_x, center_y, size, angle, color):
    t.up()
    t.goto(center_x, center_y)
    t.down()
    t.setheading(270 - angle/2)
    t.begin_fill()
    t.fillcolor(color)
    t.forward(size)
    t.setheading(-1 * angle/2)
    t.circle(size,angle)
    t.goto(center_x,center_y)
    t.end_fill()


def main():
    import turtle
    t = turtle.Pen()
    t.pensize(10)
    t.reset()
    t.speed(0)

    melon_rind(t, 0, 200, 400, 90, 'green')   # 画绿色瓜皮
    melon_rind(t, 0, 200, 380, 90, 'red')     # 画红色瓜瓤

    # 画瓜子
    seed(t, 0,100,30)
    seed(t, 50,0,30)
    seed(t, -50,0,30)
    seed(t, 0,-100,30)
    seed(t, 100,-100,30)
    seed(t, -100,-100,30)
    t.hideturtle()

    turtle.mainloop()


if __name__ == '__main__':
    main()