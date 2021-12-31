rom manimlib import *

class InteractiveDevelopment(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()

        # 这会打开一个iPython终端，你可以在其中继续写你想要执行的代码
        # 在这个例子中，square/circle/self都会成为终端中的实例
        self.embed()

        # 尝试拷贝粘贴下面这些行到交互终端中
        self.play(ReplacementTransform(square, circle))
        self.wait()
        self.play(circle.animate.stretch(4, 0))
        self.play(Rotate(circle, 90 * DEGREES))
        self.play(circle.animate.shift(2 * RIGHT).scale(0.25))

        text = Text("""
            In general, using the interactive shell
            is very helpful when developing new scenes
        """)
        self.play(Write(text))

        # 在交互终端中，你可以使用play, add, remove, clear, wait, save_state
        # 和restore来代替self.play, self.add, self.remove……

        # 这时如果要使用鼠标键盘来与窗口互动，需要输入执行touch()
        # 然后你就可以滚动窗口，或者在按住z时滚动来缩放
        # 按住d时移动鼠标来更改相机视角，按r重置相机位置
        # 按q退出和窗口的交互来继续输入其他代码

        # 特别的，你可以自定一个场景来和鼠标和键盘互动
        always(circle.move_to, self.mouse_point)
