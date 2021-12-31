from manimlib import *

class demo(Scene):
    def construct(self):
        c1 = Circle()                             # 创建第一个圆形对象
        c1.set_stroke(color=RED, width=4)         # 设置c1的边属性
        c1.set_fill(color=YELLOW, opacity=0.5)    # 设置c1的填充属性

        c2 = Circle()                             # 创建第二个圆形对象
        c2.set_stroke(color=PURPLE)               # 设置c2的边属性
        c2.set_fill(color=BLUE, opacity=0.5)      # 设置c2的填充属性

        c1.next_to(c2, 10 * LEFT)                      # c1在c2的左边

        self.play(Write(c1))                      # 为c1创建Write动画，并播放
        self.play(Write(c2))                      # 为c2创建Write动画，并播放
        self.wait(1)
        c1.next_to(c2, 5 * DOWN)
        self.play(Write(c1))
        self.play(Write(c2))
