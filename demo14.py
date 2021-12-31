from manimlib import *

class demo(Scene):
    def construct(self): # 其内容将决定如何在屏幕中创建mobjects以及需要执行哪些操作
        c1 = Circle( radius=0.1 ) # 创建一个Circle的实例c1,半径为0.1
        c1.set_stroke(color=RED, width=DEFAULT_STROKE_WIDTH) # 描边颜色为RED
        c1.set_fill(color=YELLOW, opacity=0.5) # 填充颜色为YELLOW，透明度为0.5

        c2 = Circle( radius=0.1)
        c2.set_stroke(color=PURPLE)
        c2.set_fill(color=BLUE, opacity=0.5)

        self.play(Write(c1))

        # cs = [c2.copy() for _ in range(4)]
        position = [TOP, RIGHT_SIDE, BOTTOM, LEFT_SIDE]
        # for c, p in zip(cs, position):
        for p in position:
            # c.next_to(c1, p)
            c = c2.copy()
            c.next_to(c1, p)
            self.play(Write(c))
