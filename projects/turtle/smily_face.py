import turtle

turtle.title('笑脸')
turtle.bgcolor('gray')
turtle.speed(0)


turtle.up()
turtle.goto(0, -100)
turtle.down()

# 画脸，填充黄色
turtle.begin_fill()
turtle.fillcolor('yellow')
turtle.circle(100)
turtle.end_fill()

# 画嘴巴
turtle.up()
turtle.goto(-67, -40)
turtle.setheading(-60)
turtle.pensize(5)
turtle.down()
turtle.circle(80, 120)

# 画两个眼睛
turtle.fillcolor('white')
for i in range(-35, 105, 70):
    turtle.up()
    turtle.goto(i, 35)
    turtle.setheading(0)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(12)
    turtle.end_fill()

turtle.fillcolor('black')
for i in range(-34, 106, 70):
    turtle.up()
    turtle.goto(i, 42)
    turtle.setheading(0)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(4)
    turtle.end_fill()

turtle.hideturtle()
turtle.mainloop()