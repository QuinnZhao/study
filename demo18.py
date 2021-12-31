from manimlib import *
import numpy as np

class Shadow_circle(Scene):

    def construct(self):
        # return super().construct()
        arc1 = Arc(
            start_angle=TAU/4, 
            angle=TAU/4, 
            radius=2,
            fill_color=GREY,
            fill_opacity=1,
            stroke_color = BLACK)
        self.add(arc1)

        p1 = Polygon(
            np.array([0,0,0]),
            np.array([0,2,0]),
            np.array([-2,0,0]),
            fill_color= WHITE,
            fill_opacity = 1,
            stroke_color = BLACK
        )
        self.add(p1)

        arc2 = Arc(
            start_angle=0, 
            angle=TAU/4, 
            radius=1,
            arc_center = ORIGIN + LEFT,
            fill_color=GREY,
            fill_opacity=1,
            stroke_color= BLACK)
        self.add(arc2)

        p2 = Polygon(
            np.array([0,0,0]),
            np.array([-1,1,0]),
            np.array([-2,0,0]),
            fill_color= GREY,
            fill_opacity = 1,
            stroke_color = GREY
        )
        self.add(p2)

        arc3 = Arc(
            start_angle=TAU/4,
            angle = TAU/4,
            radius = 1,
            arc_center = ORIGIN + LEFT,
            fill_color = WHITE,
            fill_opacity = 1,
            stroke_color = BLACK
            )
        self.add(arc3)
        self.wait()
        l = DashedLine(start=ORIGIN, end = np.array([-1,1,0]), stroke_color = BLACK)
        self.add(l)
        
        arc4 = Arc(
            start_angle=TAU/4,
            angle = TAU/4,
            radius = 1,
            arc_center = ORIGIN + LEFT,
            fill_color = GREY,
            fill_opacity = 1,
            stroke_color = BLACK
            )

        arc5 =  Arc(
            start_angle=0,
            angle = TAU/4,
            radius = 1,
            arc_center = ORIGIN + LEFT,
            fill_color = WHITE,
            fill_opacity = 1,
            stroke_color = BLACK
            )

        # self.play(
        #     ReplacementTransform(arc3, arc4),
        #     ReplacementTransform(arc2, arc5),
        #     run_time = 4
        #     )
        
        # self.add(
        #     Line(np.array([-2,0,0]), np.array([-1,1,0]), stroke_color=BLACK),
        #     Line(np.array([-2,0,0]), ORIGIN, stroke_color=BLACK)
        #     )
        # # self.play(Write(p))
        # self.wait()

        # self.play(
        #     Rotating(
        #         arc5,
        #         angle =3 * PI /2,
        #         run_time = 2,
        #         axis= np.array([-1,1,0])
        #     )
        # )

        # m = np.array([
        #     [0, 1, 0],
        #     [-1, 0, 0],
        #     [0, 0, 1]]
        # )

        # m1 = np.array([[1,0,-1], [0,1,1], [0,0,1]])
        # m2 = m1 * np.array([[0,1,0],[-1,0,0],[0,0,1]])
        # m3 =m2 * np.array([[1,0,1],[0,1,-1],[0,0,1]])

        # self.play(
        #     ApplyMatrix(m1, arc5))
        # self.wait(2)
        # self.play(
        #     ApplyMatrix(m2, arc5),)
        # self.wait(2)
        # self.play(
        #     ApplyMatrix(m3,arc5),
        # )
        arc6 = arc2.rotate(angle= 1.5 * PI, about_point=np.array([-1,1,0]))
        self.play(FadeTransform(arc2, arc6), run_time=12)
        

class Demo18(Scene):

    def construct(self):
        # return super().construct()
        cp = Arc().add_line_to(ORIGIN + RIGHT)

        self.add(cp)

        self.wait()

        # 弧围绕一个点旋转，结果却是弧的圆心围绕这个点旋转，之后再画弧，与实际不符
        cp2 = cp.rotate(angle=3 * PI/2, about_point=UP)
        self.play(Transform(cp, cp2, run_time=5))