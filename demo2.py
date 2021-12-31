from manimlib import *

class AnimatingMethods(Scene):
    def construct(self):
        grid = Tex(r"\pi").get_grid(10, 10, height=4)
        self.add(grid)

        # 你可以通过.animate语法来动画化物件变换方法
        self.play(grid.animate.shift(LEFT))

        # 或者你可以使用旧的语法，把方法和参数同时传给Scene.play
        self.play(grid.shift, LEFT)

        # 这两种方法都会在mobject的初始状态和应用该方法后的状态间进行插值
        # 在本例中，调用grid.shift(LEFT)会将grid向左移动一个单位

        # 这种用法可以用在任何方法上，包括设置颜色
        self.play(grid.animate.set_color(YELLOW))
        self.wait()
        self.play(grid.animate.set_submobject_colors_by_gradient(BLUE, GREEN))
        self.wait()
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.wait()

        # 方法Mobject.apply_complex_function允许应用任意的复函数
        # 将把Mobject的所有点的坐标看作复数

        self.play(grid.animate.apply_complex_function(np.exp), run_time=5)
        self.wait()

        # 更一般地说，你可以应用Mobject.apply方法，它接受从R^3到R^3的一个函数
        self.play(
            grid.animate.apply_function(
                lambda p: [
                    p[0] + 0.5 * math.sin(p[1]),
                    p[1] + 0.5 * math.sin(p[0]),
                    p[2]
                ]
            ),
            run_time=5,
        )
        self.wait()