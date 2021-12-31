from manimlib import *

class CoordinateSystemExample(Scene):
    def construct(self):
        axes = Axes(
            # x轴的范围从-1到10，步长为1
            x_range=(-1, 10),
            # y轴的范围从-2到2，步长为0.5y-axis ranges from -2 to 10 with a step size of 0.5
            y_range=(-2, 2, 0.5),
            # 坐标系将会伸缩来匹配指定的height和width
            height=6,
            width=10,
            # Axes由两个NumberLine组成，你可以通过axis_config来指定它们的样式
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            # 或者，你也可以像这样分别指定各个坐标轴的样式
            y_axis_config={
                "include_tip": False,
            }
        )
        # add_coordinate_labels方法的关键字参数可以传入DecimalNumber来指定它的样式
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        self.add(axes)

        # Axes从CoordinateSystem类派生而来，意思是可以调用Axes.coords_to_point
        # （缩写为Axes.c2p）将一组坐标与一个点相关联，如下所示：
        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))
        self.play(FadeIn(dot, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(3, 2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
        self.wait()

        # 同样，你可以调用Axes.point_to_coords（缩写Axes.p2c）
        # print(axes.p2c(dot.get_center()))

        # 我们可以从轴上画线，以便更好地标记给定点的坐标在这里
        # always_redraw命令意味着在每一个新帧上重新绘制线来保证线始终跟随着点移动
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))

        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )
        self.play(dot.animate.move_to(axes.c2p(3, -2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(1, 1)))
        self.wait()

        # 如果我们把这个点固定在一个特定的坐标上，当我们移动轴时，它也会跟随坐标系移动
        f_always(dot.move_to, lambda: axes.c2p(1, 1))
        self.play(
            axes.animate.scale(0.75).to_corner(UL),
            run_time=2,
        )
        self.wait()
        self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))

        # manim还有一些其它的坐标系统：ThreeDAxes，NumberPlane，ComplexPlane