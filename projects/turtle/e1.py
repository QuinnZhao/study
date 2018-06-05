from turtle import *
import time

# 画一个边长为100的正方形
up()
goto(-100, 100)
down()

for i in range(4):
    forward (100)
    left(90)
    
time.sleep(5)
# clear()

# 画一个圆
up()
goto(0, 50)
down()
circle(100)    
    
mainloop()