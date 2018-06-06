# 画紫色的五角星

import turtle

def star(t, x, y, length, color, pensize):
    t.color(color)
    t.pensize(pensize)
    t.up()
    turtle.goto(x,y)
    t.down()
    for i in range(6):
        t.forward(length)
        t.right(144)

def main():
    turtle.speed(0)
    turtle.title('Star')
    star(turtle, 0, 0, 200, 'blue', 5)
    turtle.up()
    turtle.goto(-150,-120)
    turtle.color("red")
    turtle.write("Done")

if __name__ == '__main__':
    main()

turtle.mainloop()