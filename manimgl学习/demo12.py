from manimlib import *

class test_cn(Scene):
    def construct(self):
        text01 = TexText("黑夜给了我一双黑色的眼睛，")
        text02 = TexText("我却用它寻找光明。")
        text03 = TexText("顾城 《一代人》")
        text_group = VGroup(text01, text02)
        text02.next_to(text01, DOWN)

        text04 = TexText("春晓")
        text05 = TexText("唐·孟浩然")

        self.play(Write(text01))
        self.wait(1)
        self.play(TransformFromCopy(text01, text02))
        self.wait(1)
        self.play(Transform(text_group,text03))
        self.wait(2)

        self.play(Write(text04))
        self.wait(1)
