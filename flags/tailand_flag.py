import turtle

def turn(t, step):
    t.up()
    t.setheading(90)
    t.forward(step)
    t.down()

def rectangle(t, length, width, fill = True, colors = ('black', 'red')):
    t.setheading(0)
    if fill:
        t.color(colors[0], colors[1])
        t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)
    if fill:
        t.end_fill()
    
def netherland_flag(t, size, start_x=0, start_y = 0):
    t.up()
    t.speed('fastest')
    t.screensize(1200, 800)
    t.title('泰国国旗')
    t.bgcolor('black')
    t.goto(start_x, start_y)
    t.down()
    length = size
    width_6_1 = size * 2 / 3 / 6
    rectangle(t, length, width_6_1, colors = ('red' ,'red'))
    turn(t, width_6_1)
    rectangle(t, length, width_6_1, colors = ('white' ,'white'))
    turn(t, width_6_1)
    rectangle(t, length, 2 * width_6_1, colors = ('darkblue' ,'darkblue'))
    turn(t, 2 * width_6_1)
    rectangle(t, length, width_6_1, colors = ('white', 'white'))
    turn(t, width_6_1)
    rectangle(t, length, width_6_1, colors = ('red' ,'red'))
    turn(t, width_6_1)
    t.pensize(5)
    t.pencolor('brown')
    t.setheading(-90)
    t.forward(2 * size / 3 * 2)
    t.setheading(0)
    t.pencolor('white')
    t.up()
    t.forward(50)
    t.write('泰国国旗', font=('微软雅黑', 20, 'bold'))
    t.pensize(1)
    t.hideturtle()

if __name__ == '__main__':
    netherland_flag(turtle, 240, start_x = -240)
    netherland_flag(turtle, 180, start_x = 30)
    netherland_flag(turtle, 120, start_x = 240)

    turtle.mainloop()
    