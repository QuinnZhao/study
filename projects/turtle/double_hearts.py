import turtle


def go_to(t,x, y):
    t.up()
    t.goto(x, y)
    t.down()


def big_Circle(t, size, left):  # 函数用于绘制心的大圆
    t.speed(0)
    for i in range(150):
        t.forward(size)
        if left:
            t.right(0.3)
        else:
            t.left(0.2)


def small_Circle(t, size, left):  # 函数用于绘制心的小圆
    for i in range(210):
        t.forward(size)
        if left:
            t.right(0.786)
        else:
            t.left(0.786)


def line(t, size):
    t.speed(1)
    t.forward(51*size)


def heart(t,  x, y, size):
    t.speed(0)
    go_to(t, x, y)
    t.left(150)
    t.begin_fill()
    line(t, size)
    big_Circle(t, size, 1)
    small_Circle(t, size,1)
    go_to(t, x, y)
    t.setheading(27.5)
    big_Circle(t, size, 0)
    small_Circle(t, size, 0)
    t.end_fill()


def arrow(t):
    t.pensize(10)
    t.setheading(0)
    go_to(t, -400, 0)
    t.left(15)
    t.forward(150)
    go_to(t, 339, 178)


def arrow_head(t):
    t.pensize(1)
    t.speed(5)
    t.color('red', 'red')
    t.forward(20)
    t.right(150)
    t.forward(35)
    t.right(120)


def main():
    turtle.pensize(2)
    turtle.color('red', 'pink')
    heart(turtle, 200, 0, 1)  # 画出第一颗心，前面两个参数控制心的位置，函数最后一个参数可控制心的大小
    turtle.setheading(0)  # 使画笔的方向朝向x轴正方向
    heart(turtle, -80, -100, 1.5)  # 画出第二颗心
    arrow(turtle)  # 画出穿过两颗心的直线
    arrow_head(turtle)  # 画出箭的箭头
    go_to(turtle, 400, -300)
    turtle.write("author：Quinn Zhao", move=True, align="left", font=("宋体", 30, "normal"))
    turtle.mainloop()

if __name__ == '__main__':
    main()

