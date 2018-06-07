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


# 画瓜子，随机分布
def seed(t, mc_x, mc_y, m_size, m_angle):
    from math import sin, pi, cos
    from random import randint
    for r in range (150, m_size - 80, 100):
        half_length = int(r * sin(m_angle / 2 * pi / 180))
        y = int(r * cos(m_angle / 2 * pi / 180)) * -1 + mc_y
        for i in range(-1 * half_length + 3, half_length - 3, 50):
            t.up()
            t.goto(i + mc_x, y + randint(-10, 10))
            t.setheading(0)
            t.down()
            t.dot(10, 'black')


def main():
    import turtle
    t = turtle.Pen()
    t.pensize(10)
    t.reset()
    t.speed(0)
    center_x, center_y = 0, 200
    malon_size = 500
    rind_thick = 20
    angle = 60
    melon_rind(t, center_x, center_y, malon_size, angle, 'green')   # 画绿色瓜皮
    melon_rind(t, center_x, center_y, malon_size - rind_thick, angle, 'red')     # 画红色瓜瓤

    seed(t, center_x, center_y, malon_size, angle)
    t.hideturtle()

    turtle.mainloop()


if __name__ == '__main__':
    main()