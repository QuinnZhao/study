from manimlib import *
from os import system

class Curved_arrows(Scene):
    def construct(self):
        arrow = CurvedArrow(
            start_point=UP * 2,
            end_point=DOWN * 2,
            angle=TAU / 4.             # 90度
            # angle = PI / 4
        )
        arrow.set_color(color=RED)

        d_arrow = CurvedDoubleArrow(
            start_point=UP * 2,
            end_point=DOWN * 2,
            angle=TAU / 4.             # 90度
            # angle = PI / 4
        )
        d_arrow.set_color(color=GREEN)
        d_arrow.next_to(arrow, RIGHT)   # 双头箭头在单箭头的右边

        self.add(arrow, d_arrow)

class New_curved_arrow(Scene):
    def construct(self):
        arc = Arc(
            start_angle=PI / 2.,
            angle=PI / 4., # 45度
            radius=3,
            arc_center=ORIGIN
        )
        self.play(Write(arc))
        arc2 = arc.copy()
        arc2.angle = 1.5 * PI            # 270度
        arc2.init_points()
        arc2.add_tip(at_start=False)     # 在圆弧的尾部添加箭头，构成一个新Arrow
        self.play(ReplacementTransform(arc, target_mobject=arc2)) 

class Circle_and_ellipse(Scene):
    def construct(self):
        ellipse = Ellipse(
            width=4,            # 长轴为4, 也就是a = 2
            height=2            # 短轴为2，也就是b = 1    
        )
        ellipse.set_fill(color=GREEN_B, opacity=0.9)
        ellipse2 = ellipse.copy()
        ellipse2.set_width(2)
        ellipse2.set_height(4) # 因为短轴对于长轴，自动取长轴的值，故ellipse2事实上一个圆
        ellipse2.init_points() # 修改参数后必须调用的方法

        
        circle = Circle(
            radius=2,
            color=BLUE
        )
        circle.radius = 2

        self.add(circle) # 半径为2的圆
        self.add(ellipse) # 长轴为4，短轴为2的椭圆
        self.add(ellipse2) # 半径1的圆

class Dots(Scene):
    def construct(self):
        colors = [BLUE, YELLOW, RED]
        for i in range(-2, 3):
            for j in range(-2, 3):
                d = Dot(
                    point=np.array([i, j, 0]),
                    color=colors[(i + j) % len(colors)]
                )
                self.add(d)

class Sectors(Scene):
    def construct(self):
        annularsector = AnnularSector(
            start_angle=0,
            angle=TAU / 4.,
            inner_radius=1,
            outer_radius=3,
            color=GREEN
        )
        sector = Sector(
            start_angle=0,
            angle=TAU / 4.,
            outer_radius=3,
            color=BLUE
        )
        
        annularsector.next_to(sector, DOWN)
        self.add(annularsector, sector)

class Annulu(Scene):
    def construct(self):
        annulus = Annulus(
            inner_radius=2,
            outer_radius=3,
            color=BLUE,
            fill_opacity=0.8
        )
        self.add(annulus)

class Lines(Scene):
    def construct(self):
        l1 = Line(
            start=LEFT * 3,
            end=RIGHT * 3,
            buff=0,
            path_arc=0,
            color=GREEN
        )
        l2 = DashedLine(
            start=LEFT * 3,
            end=RIGHT * 3,
            dash_length=0.05,
            dash_spacing=0.1,
            positive_space_ratio=0.5,
            color=BLUE
        )
        l2.next_to(l1, DOWN * 2)
        self.add(l1, l2)

class Circle_and_its_tangentline(Scene):
    def construct(self):
        circle = Circle(
            radius=3,
            color=BLUE,
            fill_opacity=0.5
        )
        line = TangentLine(
            vmob=circle,
            alpha=0.5,
            length=4
        )
        self.play(Write(circle))
        self.wait()
        self.play(Write(line))

class Elbows(Scene):
    def construct(self):
        e1 = Elbow(
            width=1,
            angle=0,
            color=GREEN
        )
        self.add(e1)

class Color_retangle(Scene):
    def construct(self):
        colors = [BLUE, RED, GREEN, GREY_A]
        for i in range(4):
            self.add(Elbow(
                width=3.,
                angle=i * PI / 2.,
                color=colors[i]
            ))

class Arrows(Scene):
    def construct(self):
        a1 = Arrow(
            start=LEFT,
            end=RIGHT,
            stroke_color=BLUE,
            # fill_color=BLUE,
            fill_opacity=0.5,
            thickness=3,
            tip_width_ratio=5,
            tip_angle=PI / 2.
        )

        a2 = Arrow(
            start=LEFT * 2,
            end=RIGHT * 2,
            # fill_color=GREEN, # 不起作用
            stroke_color=GREEN,
            fill_opacity=0.8,
            thickness=3,
            tip_width_ratio=8,
            tip_angle=PI / 6.
        )

        self.add(a1)
        self.wait()
        self.play(ReplacementTransform(a1, a2))
        self.wait()

class Vectors(Scene):

    def construct(self):
        colors = [BLUE, RED, GREEN]
        vectors = [
            np.array([1, 0]),
            np.array([1, 1]),
            np.array([1, 3]),
            np.array([-2, 1]),
            np.array([-1, -1])
        ]
        
        temp_vec, temp_text = None, None
        for index, v in enumerate(vectors):
            empty_scene = (len(self.get_mobjects()) == 1)
            if empty_scene:     # 检查Scene画布上有没有放实体，没有就放，你也可以通过temp_vec是否为None来等价判断，这个地方只是单纯想让你知道有get_mobjects这个方法
                temp_vec = Vector(
                    direction=v,
                    fill_color=colors[index % len(colors)]
                )
                temp_text = Tex(f"({v[0]}, {v[1]})")
                temp_text.move_to(np.hstack((v, 0)) * 1.2)      # move_to的参数必须是三维向量
                self.add(temp_vec, temp_text)
            else:
                cur_vec = Vector(
                    direction=v,
                    fill_color=colors[index % len(colors)]
                )
                cur_text = Tex(f"({v[0]}, {v[1]})")
                cur_text.move_to(np.hstack((v, 0)) * 1.2)
                self.play(
                    ReplacementTransform(temp_vec, cur_vec),
                    ReplacementTransform(temp_text, cur_text)
                )
                temp_vec = cur_vec
                temp_text = cur_text

# 一头大，一头小，因为起点使用默认的箭头宽度，终点使用Arrow默认宽度
class Double_arrow(Scene):
    def construct(self):
        self.add(
            DoubleArrow(
                start=np.array([-1, 2, 0]),
                end=np.array([1, 1, 0]),
                # color=BLUE, # 不起作用
                # fill_color=BLUE # 不起作用
                stroke_color = BLUE
            )
        )

class Cubic_bezier(Scene):
    def construct(self):
        curve = CubicBezier(
            a0=np.array([-2, 1, 0]),
            h0=np.array([-1, 0, 0]),
            h1=np.array([1, 0, 0]),
            a1=np.array([2, 1, 0])
        )
        self.add(curve)

class Cubic_bezier_2(Scene):
    def construct(self):
        points = [
            np.array([-2, 1, 0]),
            np.array([-1, 0, 0]),
            np.array([1, 0, 0]),
            np.array([2, 1, 0])
        ]
        names = ["a0", "h0", "h1", "a1"]
        
        # 创建坐标轴
        axes = Axes(
            x_range=(-2, 2),
            y_range=(0, 1.2)
        )
        axes.add_coordinate_labels()
        self.play(Write(axes))
        # 将三阶贝塞尔曲线的三条外边画出来，并加上*names的标注
        for i, _ in enumerate(points):
            if i < len(points) - 1:
                text = self.write_word(names[i], axes.c2p(points[i][0], points[i][1]))
                self.play(
                    ShowCreation(axes.get_graph(
                        function=self.get_line_func(points[i], points[i + 1]),
                        x_range=(points[i][0], points[i + 1][0]),
                        color=BLUE)),
                    Write(text)
                )

        text = self.write_word(names[-1], axes.c2p(points[-1][0], points[-1][1]))
        self.play(Write(text))

        group = VGroup(*self.get_mobjects()[1:])

        # 改变坐标轴的位置
        self.play(group.animate.scale(0.6).to_corner(UL), run_time=2)

        # 设定变化参数t，初值为0
        t = ValueTracker(0)
        # 显示数字
        formula = Tex(r"B_n(t)=\sum_{k=0}^n\binom{n}{k}t^k(1-t)^{n-k}P_k", font_size=56)
        text, number = label = VGroup(
            Tex("t = ", font_size=64),
            DecimalNumber(0, num_decimal_places=2, include_sign=False)
        )
        label.arrange(RIGHT)
        formula.move_to(np.array([0, -2, 0]))
        label.move_to(np.array([3, 2, 0]))
        f_always(number.set_value, t.get_value)
        self.play(FadeIn(text), FadeIn(number), Write(formula))

        # 跟踪的点
        point = Dot(axes.c2p(points[0][0], points[0][1]), color=RED)
        # 跟踪的线
        l1 = Line(
            start=axes.c2p(points[0][0], points[0][1]),
            end=axes.c2p(points[1][0], points[1][1]),
            color=RED_B
        )

        l2 = Line(
            start=axes.c2p(points[1][0], points[1][1]),
            end=axes.c2p(points[2][0], points[2][1]),
            color=RED_B
        )

        l3 = Line(
            start=axes.c2p(points[0][0], points[0][1]),
            end=axes.c2p(points[1][0], points[1][1]),
            color=GREEN
        )

        # 创建TracedPath对象，它代表点的中心出现过的地方的集合
        tracer = TracedPath(point.get_center)
        tracer.set_stroke(YELLOW, width=3, opacity=1)
        self.play(ShowCreation(tracer))
        
        self.play(Write(point), Write(l1), Write(l2), Write(l3))
        
        # 增加updater，画出Dot的轨迹
        point.add_updater(self.bezier_curve(axes, t, *points))
        l1.add_updater(self.updater1(axes, t, points[0], points[1], points[2]))
        l2.add_updater(self.updater1(axes, t, points[1], points[2], points[3]))
        l3.add_updater(self.updater2(axes, t, *points))

        self.play(t.animate.set_value(1), run_time=5)
        

    def write_word(self, words, position=ORIGIN):
        t = Tex(words, color=GREEN_B)
        t.move_to(position)
        return t

    def get_line_func(self, point1, point2):    # 两点确定的直线方程
        if point1[0] == point2[0]:
            return lambda x : point1[0]
        else:
            k = (point2[1] - point1[1]) / (point2[0] - point1[0])
            b = point1[1] - k * point1[0]
            return lambda x : k * x + b
    
    def bezier_curve(self, axes : Axes, t : ValueTracker, a0, h0, h1, a1):
        bf = lambda x : a0 * pow(1 - x, 3) + 3 * h0 * x * (1 - x) * (1 - x) + 3 * h1 * x * x * (1 - x) + a1 * pow(x, 3)
        def func(point : Dot):      # 传入updater的闭包函数
            p = bf(t.get_value())
            point.move_to(axes.c2p(p[0], p[1]))
        return func
    
    def updater1(self, axes : Axes, t : ValueTracker, p1, p2, p3):
        def func(line : Line):
            x = t.get_value()
            s1 = (1 - x) * p1 + x * p2 
            s2 = (1 - x) * p2 + x * p3 
            line.set_points_by_ends(
                start=axes.c2p(s1[0], s1[1]),
                end=axes.c2p(s2[0], s2[1])
            )
            return line
        return func 
    
    def updater2(self, axes : Axes, t : ValueTracker, a0, h0, h1, a1):
        def func(line : Line):
            x = t.get_value()
            s1 = (1 - x) * (1 - x) * a0 + 2 * x * (1 - x) * h0 + x * x * h1
            s2 = (1 - x) * (1 - x) * h0 + 2 * x * (1 - x) * h1 + x * x * a1
            line.set_points_by_ends(
                start=axes.c2p(s1[0], s1[1]),
                end=axes.c2p(s2[0], s2[1])
            )
            return line
        return func

class Polygon1(Scene):
    def construct(self):
        p = Polygon(
            np.array([1, 0, 0]),
            np.array([0, 1, 0]),
            np.array([-1, 0, 0]),
            np.array([0, -1, 0])
        )
        self.play(ShowCreation(p), run_time=2)

class Polygons(Scene):
    def construct(self):
        temp_p = None
        radius = 3
        colors = [RED, BLUE, GREEN, PINK]
        for i, num in enumerate([4, 5, 6, 10, 20, 50]):
            if temp_p is None:
                temp_p = self.get_circle_polygon(radius, num)
                temp_p.set_fill(color=colors[i % len(colors)], opacity=0.75)
                self.play(Write(temp_p))
            else:
                cur_p = self.get_circle_polygon(radius, num)
                cur_p.set_fill(color=colors[i % len(colors)], opacity=0.75)
                self.play(ReplacementTransform(temp_p, cur_p))
                temp_p = cur_p
    
    def get_circle_polygon(self, radius, n : int):
        return Polygon(
            *[np.array([np.cos(i * 2 * PI / n), np.sin(i * 2 * PI / n), 0]) * radius for i in range(n)]
        )

class Regular_polygons(Scene):
    def construct(self):
        # p1 = RegularPolygon(3)
        # p2 = RegularPolygon(4)
        # p3 = RegularPolygon(5)
        # p4 = RegularPolygon(6)
        # p5 = RegularPolygon(7)

        # self.add(p1)
        # self.wait(DEFAULT_WAIT_TIME / 4.)
        # self.play(ReplacementTransform(p1, p2))
        # self.wait(DEFAULT_WAIT_TIME / 4.)
        # self.play(ReplacementTransform(p2, p3))
        # self.wait(DEFAULT_WAIT_TIME / 4.)
        # self.play(ReplacementTransform(p3, p4))
        # self.wait(DEFAULT_WAIT_TIME / 4.)
        # self.play(ReplacementTransform(p4, p5))
        # self.wait(DEFAULT_WAIT_TIME / 4.)

        ps = [RegularPolygon(i) for i in range(3,13)]
        self.add(ps[0])
        self.wait(DEFAULT_WAIT_TIME / 4.)
        for i in range(len(ps[1:-1])):
            self.play(ReplacementTransform(ps[i], ps[i+1]))
            self.wait(DEFAULT_WAIT_TIME / 4.)
        self.play(ReplacementTransform(ps[-1], ps[0]))
        self.wait(DEFAULT_WAIT_TIME / 4.)    

class Triangles(Scene):
    def construct(self):
        t = Triangle()
        t.set_fill(color=BLUE, opacity=0.9)
        t.set_stroke(color=BLUE_E, width=3)

        self.play(FadeIn(t))
        self.play(t.animate.scale(1.5), run_time=1.5)
        self.play(t.animate.scale(2), run_time=1.5)
        self.play(t.animate.scale(1 / 3), run_time=1.5)

class Arrow_tip(Scene):
    def construct(self):
        a = ArrowTip()
        self.play(FadeIn(a))
        text = Text("This is manim",font_size=32)
        self.play(a.animate.next_to(text, LEFT))
        self.play(Write(text))

class Retangles(Scene):
    def construct(self):
        r = Rectangle(
            width=4, 
            height=3,
            fill_color=RED,
            fill_opacity=0.9
        )
        r.move_to(LEFT * 3)
        s = Square(
            side_length=4,
            fill_color=GREEN,
            fill_opacity=0.9
        )
        s.move_to(RIGHT * 3)
        self.add(r, s)
        self.add(RoundedRectangle())

class Flow_graph(Scene):
    def construct(self):
        params = {
            "width" : 4,
            "heigth" : 2,
            "fill_color" : BLUE,
            "fill_opacity" : 0.75
        }
        exe1 = RoundedRectangle(**params)
        text1 = Text("拿起书", font="msyh", font_size=28)
        group1 = VGroup(exe1, text1)
        self.play(ShowCreation(group1))
        self.play(group1.animate.move_to(UP * 3))

        arrow = Arrow(
            start=UP * 2, 
            end=ORIGIN,
            stroke_color = RED_A
            )
        self.play(ShowCreation(arrow))

        exe2 = RoundedRectangle(**params)
        text2 = Text("打开书", font="msyh", font_size=28)
        group2 = VGroup(exe2, text2)
        group2.move_to(DOWN)
        self.play(ShowCreation(group2))

        total = VGroup(
            group1, arrow, group2
        )

        self.play(total.animate.move_to(ORIGIN))

class Texts(Scene):
    def construct(self):
        word = Text(
            text="I am a Text object",
            font="Times New Roman",
            font_size=56,
            gradient=[RED, ORANGE, YELLOW, GREEN, BLUE, BLUE_E, PURPLE]
        )
        self.add(word)
        word1 = Text(
            text="I am a Text object",
            font="Times New Roman",
            font_size=100,
            weight = BOLD,
            gradient=[RED, ORANGE, YELLOW, GREEN, BLUE, BLUE_E, PURPLE]
        )
        self.wait()
        self.play(ReplacementTransform(word, word1))

class Text2(Scene):
    def construct(self):
        word = Text(
            text="我是一个 Text 对象",
            font="msjh",
            font_size=56
        )
        word.set_color_by_t2c(t2c={
            "我是" : GREEN,
            "一个" : PURPLE,
            "Text" : YELLOW,
            "对象" : BLUE
        })
        self.add(word)

class Texes(Scene):
    def construct(self):
        color_dict = {"A" : BLUE, "B" : YELLOW, "C" : GREEN}
        split = ["A", "B", "C"]
        tex1 = Tex(
            r"A^2=B^2+C^2",
            font_size=80,
            isolate=split
        )
        tex2 = Tex(
            r"A=\sqrt{\,B^2+C^2 }",
            font_size=80,
            isolate=split
        )
        tex1.set_color_by_tex_to_color_map(color_dict)
        tex2.set_color_by_tex_to_color_map(color_dict)

        self.add(tex1)
        self.wait()
        self.play(ReplacementTransform(tex1, tex2), run_time=1)
        self.wait()

class Tex_text(Scene):
    def construct(self):
        tex = TexText(
            r"LSTM神经单元数学关系：",
            r"""
            $\begin{aligned} f_t&=\sigma(W_{f}x_t+U_fh_{t-1}+b_f)\\ 
            i_t&=\sigma(W_ix_t+U_ih_{t-1}+b_i)\\ 
            o_t&=\sigma(W_ox_t+U_oh_{t-1}+b_o)\\ 
            g_t&=\tanh(W_gx_t+U_gh_{t-1}+b_g)\\
                \\ 
            c_t&=c_{t-1}\odot f_t+i_t\odot g_t\\ 
            h_t&=o_t\odot \tanh(c_t) \end{aligned}$\\
            """
        )
        self.add(tex)

class Bulleted_list(Scene):
    def construct(self):
        tex = BulletedList(
            "contribution",
            "related work",
            "method"
        )
        self.add(tex)

class Title1(Scene):
    def construct(self):
        tex = Title(
            r"this is a title"
        )
        self.add(tex)

class Title2(Scene):
    def construct(self):
        tex = Title(
            r"this is first title",
            r"this is second title ",
            r"this is third title",
            arg_separator=r"\\"
        )
        self.add(tex)

class Title3(Scene):
    def construct(self):
        tex1 = Title(
            "我是正常标题"
        )
        tex2 = Title(
            "我是大了一倍的标题",
            scale_factor=2
        )
        tex2.next_to(tex1, DOWN)
        self.add(tex1)
        self.add(tex2)

class Title4(Scene):
    def construct(self):
        tex = Title(
            "I am a title without underline",
            include_underline=False
        )
        self.add(tex)

class Brace1(Scene):
    def construct(self):
        circle = Circle()
        b1 = Brace(circle, direction=DOWN, color=GREEN)
        b2 = Brace(circle, direction=UP, color=BLUE)
        self.add(b1, b2, circle)

class Brace2(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE_E, 1)

        brace = always_redraw(Brace, square, UP)
        text, number = label = VGroup(
            Text("Width = "),
            DecimalNumber(
                0,
                show_ellipsis=True,
                num_decimal_places=2,
                include_sign=True,
            )
        )
        label.arrange(RIGHT)

        always(label.next_to, brace, UP)
        f_always(number.set_value, square.get_width)

        self.add(square, brace, label)

        self.play(
            square.animate.scale(2),
            rate_func=there_and_back,
            run_time=2,
        )
        self.wait()
        self.play(
            square.animate.set_width(5, stretch=True),
            run_time=3,
        )
        self.wait()
        self.play(
            square.animate.set_width(2),
            run_time=3
        )
        self.wait()

        now = self.time
        w0 = square.get_width()
        square.add_updater(
            lambda m: m.set_width(w0 * math.cos(self.time - now))
        )
        self.wait(4 * PI)

class Brace_label(Scene):
    def construct(self):
        square = Square(side_length=2.0)
        brace = BraceLabel(
            obj=square,
            text="a = 2.0",
            brace_direction=UP
        )
        self.add(square, brace)

class Brace_text(Scene):
    def construct(self):
        square = Square(side_length=2.0)
        brace = BraceText(
            obj=square,
            text="我是一个BraceText",
            brace_direction=UP
        )
        self.add(square, brace)

class Brace_text2(Scene):
    def construct(self):
        square = Square(side_length=2.0)
        brace = BraceText(
            obj=square,
            text=["我是一个BraceText"],
            brace_direction=UP,
            color=GREEN,
            tex_to_color_map={"我是一个" : WHITE, "BraceText" : YELLOW}
        )
        
        self.add(square, brace)

# 无法使用 OSError: lightbulb not Found
class Light_bulb(Scene):
    def construct(self):
        light_bulb = Lightbulb()
        self.add(light_bulb)

# 无法使用 AttributeError: 'Cube' object has no attribute 'set_fill'
class Laptop1(Scene):
    def construct(self):
        self.add(Laptop())

class Check_mark(Scene):
    def construct(self):
        checkmark = Checkmark()
        exmark = Exmark()
        exmark.next_to(checkmark, DOWN)
        self.add(checkmark, exmark)

# 不能工作
class Check_mark(Scene):
    def construct(self):
        checkmark = Checkmark()
        exmark = Exmark()
        exmark.next_to(checkmark, UP)

        tex1 = TexText("干扰矩阵")
        tex2 = TexText("深黑幻想")
        tex1.next_to(exmark, LEFT)
        tex2.next_to(checkmark, LEFT)

        self.add(checkmark, exmark, tex1, tex2)

class Speed_meter(Scene):
    def construct(self):
        c = TexText("I am a speedmeter")
        s = Speedometer()
        self.play(FadeIn(c))
        self.wait()
        self.play(ReplacementTransform(c, s))
        self.wait(2)

class Clock1(Scene):
    def construct(self):
        clock = Clock()
        self.play(ClockPassesTime(clock), run_time=3)

