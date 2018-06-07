import turtle
from random import randint


# 生成器生成斐波那契数列
def fib(max):
    n, a, b = 0, 1, 1
    while n < max:
        yield b
        a, b = b, a + b
        n +=1


def draw(pen, n, color='red', scale=5, origin_x=0, origin_y=0):
    # n: 斐波那契数列序数
    pen.up()
    pen.goto(origin_x, origin_y)
    pen.color(color)
    pen.down()
    for radius in fib(n):
        pen.circle(radius * scale, 90)


def get_scale(n):
     if n <= 4:
        return
     if n <= 8:
        return 5
     if n <= 16:
        return 0.5
     else:
        return 0.1


def single_spiral(pen, n, color, origin_x=0, origin_y=0):
    if n % 4 != 0:
        return False
    draw(pen, n, color=color, scale=get_scale(n), origin_x=0, origin_y=0)
    return True


def double_spiral(pen, n, color, origin_x=0, origin_y=0):
    if n % 4 != 2:
        return False
    scale = get_scale(n)
    for i in range(2):
        draw(pen, n, color=color, scale=scale, origin_x=0, origin_y=0)
    return True


def q_spiral(pen, n, color, origin_x=0, origin_y=0):
    # 绘制4螺旋
    if (n % 4) % 2 == 0:
        return False
    scale = get_scale(n)
    for i in range(4):
        draw(pen, n, color=color, scale=scale, origin_x=0, origin_y=0)
    return True


if __name__ == '__main__':
    turtle.reset()
    turtle.title('斐波那契螺旋')
    turtle.screensize(2000, 2000)
    turtle.speed(0)
    # single_spiral(turtle, 8, 'red')
    # double_spiral(turtle, 6, 'blue')
    # q_spiral(turtle, 5, 'black')

    colors = ['yellow', 'blue', 'green', 'red', 'purple']
    for i in range(360):
        if single_spiral(turtle, 12, colors[i % 5]):
            turtle.left(i)
        else:
            break

    turtle.hideturtle()
    turtle.mainloop()