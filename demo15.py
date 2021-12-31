from manimlib import *

class show_creation_example(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text('Text').scale(2)
        )
        mobjects.scale(1.5)

        mobjects.arrange(RIGHT, buff=2)

        # ShowCreation显示创建过程
        self.play(
            *[ShowCreation(mob) for mob in mobjects]
        )

        self.wait()

class uncreate_example(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text('Text').scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects) # 将圆和文字添加到屏幕上

        self.wait(0.3) # 延迟0.3秒

        # Uncreate 显示销毁过程（ ShowCreation 的倒放）
        self.play(
            *[Uncreate(mob) for mob in mobjects]
        )

class draw_border_then_fill_example(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text('Text').scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        # DrawBorderThenFill 画出边缘，然后填充颜色
        self.play(
            *[DrawBorderThenFill(mob) for mob in mobjects]
        )
        self.wait()

class write_example(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text('Text').scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        # Write 写（对子物件逐个使用 DrawBorderThenFill ）
        self.play(
            *[Write(mob) for mob in mobjects]
        )
        self.wait()

# ShowIncreasingSubsets 字符一个一个显示
class show_increasing_subsets_example(Scene):
    def construct(self):
        text = Text("ShowIncreasingSubsets")
        text.set_width(11)
        self.wait()
        self.play(ShowIncreasingSubsets(text, run_time=4))
        self.wait()

class show_increasing_subsets_example_1(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text('Text').scale(2)
        )
        # mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.wait()
        self.play(ShowIncreasingSubsets(mobjects, run_time=4))
        self.wait()

# 不能正确工作
class show_submobjects_one_by_one_example(Scene):
    def construct(self):
        text = Text("ShowSubmobjectsOneByOne")
        text.set_width(11)
        self.wait()
        self.play(ShowSubmobjectsOneByOne(text, run_time=14))
        self.wait()

# 同上，无法正确工作
class show_submobjects_one_by_one_example_1(Scene):
    def construct(self):
            mobjects = VGroup(
                    Circle(),
                    Circle(fill_opacity=1),
                    Text('Text').scale(2)
            )
            # mobjects.scale(1.5)
            mobjects.arrange(RIGHT, buff=2)

            self.wait()
            self.play(ShowSubmobjectsOneByOne(mobjects, run_time=4))
            self.wait()

class fade_out_example(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text('Text').scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.add(mobjects)
        self.wait(0.3)
        self.play(
            *[FadeOut(mob) for mob in mobjects]
        )

        self.wait()

class fade_in_example(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text('Text').scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)

        self.play(
            *[FadeIn(mob) for mob in mobjects]
        )

        self.wait()

class fade_in_from_example(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text('Text').scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)
        directions = [UP, LEFT, DOWN, RIGHT]

        for direction in directions:
            self.play(
                *[FadeIn(mob, shift=direction) for mob in mobjects]
            )

        self.wait()

class fade_out_and_shift_example(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text('Text').scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT, buff=2)
        directions = [UP, LEFT, DOWN, RIGHT]

        self.add(mobjects)
        self.wait(0.3)

        for direction in directions:
            self.play(
                *[FadeOut(mob, shift=direction) for mob in mobjects]
            )

        self.wait()

class fade_in_from_large_example(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TexText("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT,buff=2)

        scale_factors=[0.3,0.8,1,1.3,1.8]

        for scale_factor in scale_factors:
            t_scale_factor = TexText(f"\\tt scale\\_factor = {scale_factor}")
            t_scale_factor.to_edge(UP)

            self.add(t_scale_factor)

            self.play(
                *[FadeIn(mob,scale=scale_factor) for mob in mobjects]
            )

            self.remove(t_scale_factor)

        self.wait(0.3)

class fade_in_from_point_example(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            TexText("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT,buff=2)

        self.wait()
        self.play(
            *[FadeInFromPoint(mob, UP*3) for mob in mobjects]
        )
        self.wait()

class fade_out_to_point_example(Scene):
    def construct(self):
        mobjects = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            TexText("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT,buff=2)

        self.add(mobjects)
        self.wait(0.3)
        self.play(
            *[FadeOutToPoint(mob, UP*3) for mob in mobjects]
        )
        self.wait()

class fade_transform_example(Scene):
    def construct(self):
        mobjects1 = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text('Text').scale(2)
        )
        mobjects2 = VGroup(
            Circle(fill_opacity=1),
            Circle(),
            Text('Text').scale(1)
        )

        mobjects1.scale(1.5)
        mobjects2.scale(1.5)
        mobjects1.arrange(RIGHT, buff=2)
        mobjects2.arrange(RIGHT, buff=2)

        self.wait()
        self.play(
            *[FadeTransform(mob1, mob2) for mob1 in mobjects1 for mob2 in mobjects2]
        )
        self.wait()

class fade_transform_pieces_example(Scene):
    def construct(self):
        mobjects1 = VGroup(
            Circle(),
            Circle(fill_opacity=1),
            Text('Text').scale(2)
        )
        mobjects2 = VGroup(
            Circle(fill_opacity=1),
            Circle(),
            Text('Text').scale(1)
        )

        mobjects1.scale(1.5)
        mobjects2.scale(1.5)
        mobjects1.arrange(RIGHT, buff=2)
        mobjects2.arrange(RIGHT, buff=2)

        self.wait()
        self.play(
            *[FadeTransformPieces(mob1, mob2) for mob1 in mobjects1 for mob2 in mobjects2]
        )
        self.wait()

class grow_from_point_example(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text("Text").scale(2)
            )
        mobjects.arrange(RIGHT,buff=2)

        directions=[UP,LEFT,DOWN,RIGHT]

        for direction in directions:
            self.play(
                *[GrowFromPoint(mob,mob.get_center()+direction*3) for mob in mobjects]
            )

        self.wait()

class grow_from_center_example(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT,buff=2)

        self.play(
            *[GrowFromCenter(mob) for mob in mobjects]
        )

        self.wait()

class grow_from_edge_example(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                Text("Text").scale(2)
            )
        mobjects.arrange(RIGHT,buff=2)

        directions=[UP,LEFT,DOWN,RIGHT]

        for direction in directions:
            self.play(
                *[GrowFromEdge(mob,direction) for mob in mobjects]
            )

        self.wait()

class grow_arrow_example(Scene):
    def construct(self):
        mobjects = VGroup(
                Arrow(LEFT,RIGHT),
                Vector(RIGHT*2)
            )
        mobjects.scale(3)
        mobjects.arrange(DOWN,buff=2)

        self.play(
            *[GrowArrow(mob)for mob in mobjects]
        )

        self.wait()

class spin_in_from_nothing_example(Scene):
    def construct(self):
        mobjects = VGroup(
                Square(),
                RegularPolygon(fill_opacity=1),
                TexText("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange(RIGHT,buff=2)

        self.play(
            *[SpinInFromNothing(mob) for mob in mobjects]
        )

        self.wait()

class focus_on_example(Scene):
    def construct(self):
        mobjects = VGroup(
            Dot(),
            Tex("x")
        )
        mobjects.arrange(RIGHT,buff=2)

        mobject_or_coord = [
            *mobjects,                    # Mobjects: Dot and "x"
            mobjects.get_right()+RIGHT*2  # Coord
        ]

        colors=[GREY,RED,BLUE]

        self.add(mobjects)

        for obj,color in zip(mobject_or_coord,colors):
            self.play(FocusOn(obj,color=color))

        self.wait(0.3)

class indicate_example(Scene):
    def construct(self):
        #                     0    1   2
        formula = Tex("f(","x",")")
        dot = Dot()

        VGroup(formula,dot).scale(3).arrange(DOWN,buff=3)

        self.add(formula,dot)

        for mob in [formula[1],dot]:
            self.play(Indicate(mob))

        self.wait(0.3)
