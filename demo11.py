from math import atan2
from manimlib import*
class Cone(Surface):
    CONFIG = {
        "u_range": (0,  TAU),
        "v_range": (-1,  1),
        "radius": 1,
        "height": 2,
    }

    def uv_func(self,  u,  v):
        P = np.array([math.cos(u),  math.sin(u),  0])
        return P*self.radius*(1-abs(v))+max(0, v)*self.height*OUT
class ThreeDArrow(Group):

    def __init__(self, start, end, max_tip_height=0.2, max_tip_radius=0.1,  **kwargs):
        self.start=start
        self.end=end
        self.height=max_tip_height
        self.radius=max_tip_radius
        super().__init__()
        self.add(self.get_line(), self.rotate_cone())
    def get_line(self):
        return Line3D(self.start, self.end, color=WHITE)
    def get_cone_by_start_and_end(self, start, end):
        cone=Cone(height=self.height, radius=self.radius, color=WHITE)
        cone.shift(self.end)
        return cone
    def rotate_cone(self):
        cone=self.get_cone_by_start_and_end(self.start, self.end)
        if get_norm(self.end-self.start)<4*self.height:
            cone.scale(get_norm(self.end-self.start)/4*self.height, about_point=self.end)
        rotate_angle=atan2((self.end-self.start)[2], np.sqrt((self.end-self.start)[1]**2+(self.end-self.start)[0]**2))-PI/2
        #       z   y
        #       |  /
        #       | /
        #       |/
        #-------|------- x
        #      /|
        #     / |
        #    /  |
        rotate_axis=normalize(np.array([(self.end-self.start)[1], -(self.end-self.start)[0], 0]))
        cone.rotate(rotate_angle, rotate_axis, about_point=self.end)
        return cone
class ThreeDaxes(Group):
    def __init__(self, ranges=[[-5, 5], [-5, 5], [-5, 5]],  **kwargs):
        super().__init__()
        self.add(
            ThreeDArrow(ranges[0][0]*RIGHT, ranges[0][1]*RIGHT),
            ThreeDArrow(ranges[1][0]*UP, ranges[1][1]*UP),
            ThreeDArrow(ranges[2][0]*OUT, ranges[2][1]*OUT),
        )
def get_acc(EARTH, PLANET):
    start=EARTH.get_center()
    dis=get_norm(EARTH.get_center()-PLANET.get_center())
    nor=normalize(PLANET.get_center()-EARTH.get_center())
    m=(PLANET.get_width())/2**3*1000
    return Arrow(start, start+nor*m/dis**2/5, buff=0).set_color(YELLOW)
G=5

moon_earth_color={
            "月球":GREY_BROWN,
            "地球":BLUE
        }
x_1x_2_color={
            r"\vec{\mathbf{x_1} }":BLUE,
            r"\vec{\mathbf{x_2} }":GREY_BROWN,
            r"\vec{\mathbf{x_i} }":GREY_BROWN,
            "m_1":BLUE,
            "m_2":GREY_BROWN,
            "m_i":GREY_BROWN,
            r"\vec{\mathbf{a} }":YELLOW,
            r"\vec{\mathbf{v} }":RED,
        }
class ArrayTracker(ValueTracker):
    CONFIG={
        "value_type":np.array,
    }
def arraytracker(array):
    list=Group()
    for i in array:
        list.add(ValueTracker(i))
    return list
def get_a(obja, objs, ms):
    """返回的是obja的加速度！"""
    acc=0
    for i, j in zip(objs, ms):
        acc+=G*j/get_norm(i-obja)**(2)*normalize(i-obja)
    return acc
class thumbnail(ThreeDScene):
    def construct(self):
        frame=self.camera.frame
        self.play(frame.animate.move_to(ORIGIN).set_euler_angles(
            theta = -30 * DEGREES,
            phi = 70 * DEGREES,
        ),rate_func=exponential_decay,run_time=3)
        frame.add_updater(lambda obj, dt:obj.increment_theta(-0.1 * dt))
        self.add(frame)

        vg=Group(
            Sphere(radius = 0.1, color = RED),
            Sphere(radius = 0.2, color = GREEN),
            Sphere(radius = 0.15, color = BLUE)
        )
        self.a = np.array([np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0])])
        self.v = np.array([np.array([1, 0, 1]), np.array([0, -1, 0]), np.array([-1, 1, -1])])
        self.x = np.array([np.array([1, 2, 1]), np.array([-2, -2, 1]), np.array([1, 1, 0.5])])
        m = [1, 1, 1]

        for ball,x in zip(vg,self.x):
            ball.move_to(x)

        def update(obj, dt):
            for g in range(30):
                self.a = np.array([get_a(self.x[i], [*self.x[:i], *self.x[i+1:]], m) for i in range(len(self.x))])
                self.v = self.v+self.a*dt/30
                self.x = self.x+self.v*dt/30
                for ball, x in zip(obj, self.x):
                    ball.move_to(x)

        trace=VGroup(
            *[TracedPath(ball.get_center, min_distance_to_new_point = 0.01).set_color(color) for ball,color in zip(vg,[RED,GREEN,BLUE])]
        )
        self.play(*[GrowFromCenter(i) for i in vg])
        self.wait(0.1)
        vg.add_updater(update)
        self.add(vg, trace)
        self.wait(30)
        #self.embed()
class simulation(ThreeDScene):
    def construct(self):
        frame=self.camera.frame
        frame.set_euler_angles(
            theta = -30 * DEGREES,
            phi = 70 * DEGREES,
        )
        frame.add_updater(lambda obj, dt:obj.increment_theta(-0.1 * dt))
        self.add(frame)
        frame.set_color(BLACK)
        axes=ThreeDaxes()
        #self.add(axes)
        vg=Group(
            Sphere(radius = 0.1, color = RED),
            Sphere(radius = 0.2, color = GREEN),
            Sphere(radius = 0.15, color = BLUE)
        )
        self.a = np.array([np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0])])
        self.v = np.array([np.array([1, 0, 1]), np.array([0, -1, 0]), np.array([-1, 1, -1])])
        self.x = np.array([np.array([1, 2, 1]), np.array([-2, -2, 1]), np.array([1, 1, 0.5])])
        m = [1, 1, 1]
        for ball,x in zip(vg,self.x):
            ball.move_to(x)
        def update(obj, dt):
            for g in range(10):
                self.a = np.array([get_a(self.x[i], [*self.x[:i], *self.x[i+1:]], m) for i in range(len(self.x))])
                self.v = self.v+self.a*dt/10
                self.x = self.x+self.v*dt/10
            for ball, x in zip(obj, self.x):
                ball.move_to(x)


        trace=VGroup(*[TracedPath(ball.get_center, min_distance_to_new_point = 0.01).set_color(color) for ball,color in zip(vg,[RED,GREEN,BLUE])])

        def back(tex):
            return Rectangle(width=FRAME_WIDTH, height=tex.get_height()+0.5, fill_color=BLACK, stroke_width=0, fill_opacity=0.5)

        tex1=TexText(r"在网上我们会看到诸如此类的动画。").fix_in_frame()
        back1=back(tex1).fix_in_frame()
        tex2=TexText(r"你可能会好奇，\\这种没有解析解的$n(n\ge3)$体问题是如何模拟出来的。").fix_in_frame()
        back2=back(tex2).fix_in_frame()
        tex3=TexText("这期视频就将手把手教你如何模拟这种动画。").fix_in_frame()
        back3=back(tex3).fix_in_frame()
        tex4=TexText(r"注：你可能会需要一些$\mathrm{Python}$基础。\\在这里我将使用$\mathrm{Manim}$动画引擎作为演示。").fix_in_frame()
        back4=back(tex4).fix_in_frame()
        self.play(FadeIn(axes))
        self.wait(0.5)
        self.play(*[GrowFromCenter(i) for i in vg])
        self.wait(0.5)
        vg.add_updater(update)
        self.add(vg, trace)
        self.wait(5)
        self.play(frame.animate.set_opacity(0.3))
        self.wait()
        self.play(FadeIn(back1), Write(tex1))
        self.wait(5)
        self.play(FadeOut(tex1), FadeOut(back1), FadeIn(back2), Write(tex2))
        self.wait(5)
        self.play(FadeOut(tex2), FadeOut(back2), FadeIn(back3), Write(tex3))
        self.wait(5)
        self.play(FadeOut(tex3), FadeOut(back3), FadeIn(back4), Write(tex4))
        self.wait(10)
        self.play(FadeOut(tex4), FadeOut(back4))
        self.wait(10)
        self.play(*[FadeOut(i) for i in [axes, *vg, *trace]])

class one_acc(ThreeDScene):
    def construct(self):
        self.t=0
        light = self.camera.light_source
        light.move_to(100*UP+30*OUT)
        def ro(obj, dt):
            obj.rotate(0.1*dt, about_point=ORIGIN)
            self.t+=1
        light.add_updater(ro)
        self.add(light)
        day="http://sq.k12.com.cn/discuz/attachments/month_0812/20081228_bd09baeec765b6c96822PEQQ3dhvkeOn.jpg"
        night="https://apod.nasa.gov/apod/image/0011/earthlights2_dmsp_big.jpg"
        moon="https://gss0.baidu.com/-Po3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/bd315c6034a85edfe622fb0d4b540923dd547575.jpg"
        #day="day"
        #night="night"
        #moon="moon"
        EARTH=TexturedSurface(Sphere(radius=0.5).move_to(UP+RIGHT), day, night)
        MOON=TexturedSurface(Sphere(radius=0.25).move_to(DOWN+LEFT*2), moon, "black")#准备一张纯黑图片并命名其为black
        self.wait()
        self.play(*[GrowFromCenter(i) for i in [EARTH, MOON]])
        text=[r"我们记地球坐标为{{$\vec{\mathbf{x_1} }$}}，月球坐标为{{$\vec{\mathbf{x_2} }$}}",
        r"地球质量为{{$m_1$}}，月球质量为{{$m_2$}}"]
        textvg=VGroup(*[TexText(i) for i in text])
        for i in textvg:
            i.to_edge(DOWN)
        self.wait()
        self.play(Write(textvg[0]))
        arrow=Arrow(EARTH.get_center(), MOON.get_center(), buff=0)
        arrow_label=Tex(r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", r"\over", r"|", r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} }", r"|")

        arrow_label.set_color_by_tex_to_color_map({
            r"\vec{\mathbf{x_1} }":BLUE,
            r"\vec{\mathbf{x_2} }":GREY_BROWN,
        })

        arrow_label.next_to(arrow.get_center(), UP).rotate(arrow.get_angle()-PI, about_point=arrow.get_center())
        self.wait()
        a=textvg[0][1].copy()
        b=textvg[0][3].copy()
        self.play(a.animate.next_to(EARTH, UP).set_color(BLUE), b.animate.next_to(MOON, UP).set_color(GREY_BROWN))
        self.wait()
        self.play(GrowArrow(arrow), FadeOut(textvg[0]))
        self.wait()
        self.play(Write(arrow_label[1]), *[ReplacementTransform(i, j) for i, j in [(a, arrow_label[2]), (b, arrow_label[0])]])
        self.wait()
        self.play(Write(arrow_label[3]), *[ReplacementTransform(arrow_label[i].copy(), arrow_label[i+5]) for i in range(3)])
        self.play(Write(arrow_label[4]), Write(arrow_label[-1]), arrow.animate.put_start_and_end_on(EARTH.get_center(), normalize(MOON.get_center()-EARTH.get_center())+EARTH.get_center()))
        direction=TexText("{{月球}}对{{地球}}引力方向：").move_to(np.array([-4, 3, 0]))
        direction.set_color_by_tex_to_color_map(moon_earth_color)
        self.wait()
        self.play(Write(direction), arrow_label.animate.next_to(direction).rotate(PI-arrow.get_angle()))
        self.wait()
        self.play(Write(textvg[1]))
        c=textvg[1][1].copy()
        d=textvg[1][3].copy()
        self.wait()
        self.play(c.animate.next_to(EARTH, DOWN).set_color(BLUE), d.animate.next_to(MOON, DOWN).set_color(GREY_BROWN))
        self.wait()
        magnitude=TexText("{{月球}}对{{地球}}引力大小：").move_to(UP*1).align_to(direction, LEFT).set_color_by_tex_to_color_map(moon_earth_color)
        self.play(Write(magnitude))
        mag1=Tex("F").next_to(magnitude)
        mag2=Tex("G", "{ {{m_1}} {{m_2}} ", "\over", "r", "^2}").next_to(magnitude).set_color_by_tex_to_color_map(x_1x_2_color)
        mag3=Tex("G", "{ {{m_1}} {{m_2}} ", "\over", r"|\vec{\mathbf{x_2} }-\vec{\mathbf{x_1} }|", "^2}").next_to(magnitude).set_color_by_tex_to_color_map(x_1x_2_color)
        mag3[4].set_color(WHITE)
        mag3[4][1:4].set_color(GREY_BROWN)
        mag3[4][5:8].set_color(BLUE)
        self.play(FadeIn(mag1))
        self.wait()
        self.play(FadeTransform(mag1, mag2))
        self.wait()
        self.play(TransformMatchingTex(
            mag2, mag3,
            key_map={
                "r":r"|\vec{\mathbf{x_2} }-\vec{\mathbf{x_1} }|"
            },
        ))
        self.wait()
        force=Tex(r"\vec{\mathbf{F} }", "=", "G", "{ {{m_1}} {{m_2}} ", "\over", r"|\vec{\mathbf{x_2} }-\vec{\mathbf{x_1} }|", "^2}", r"{\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", r"\over", r"|", r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} }", r"|}").set_color_by_tex_to_color_map(x_1x_2_color).move_to(np.array([-4, 2, 0]))
        force[6].set_color(WHITE)
        force[6][1:4].set_color(GREY_BROWN)
        force[6][5:8].set_color(BLUE)
        force[0].save_state()
        force[0].next_to(arrow, DL)
        self.play(Write(force[0]))
        self.wait()
        self.play(force[0].animate.restore(), Write(force[1]),
        *[ReplacementTransform(i, j) for i, j in zip(mag3, force[2:8])],
        *[ReplacementTransform(i, j) for i, j in zip(arrow_label, force[8:])],
        FadeOut(direction), FadeOut(magnitude),
        arrow.animate.put_start_and_end_on(EARTH.get_center(), EARTH.get_center()+arrow.get_vector()*get_norm(EARTH.get_center()-MOON.get_center())**(-2)*20))
        self.wait()
        self.play(FadeOut(textvg[1]), FadeOut(d))
        print(self.t/10)
class one_acc_p2(Scene):
    def construct(self):
        self.t=2073
        light = self.camera.light_source
        light.move_to(100*UP+30*OUT)
        light.rotate(207.3/60, about_point=ORIGIN)
        def ro(obj, dt):
            obj.rotate(0.1*dt, about_point=ORIGIN)
            self.t+=1
        light.add_updater(ro)
        self.add(light)
        day="http://sq.k12.com.cn/discuz/attachments/month_0812/20081228_bd09baeec765b6c96822PEQQ3dhvkeOn.jpg"
        night="https://apod.nasa.gov/apod/image/0011/earthlights2_dmsp_big.jpg"
        moon="https://gss0.baidu.com/-Po3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/bd315c6034a85edfe622fb0d4b540923dd547575.jpg"
        #day="day"
        #night="night"
        #moon="moon"
        EARTH=TexturedSurface(Sphere(radius=0.5).move_to(UP+RIGHT), day, night)
        MOON=TexturedSurface(Sphere(radius=0.25).move_to(DOWN+LEFT*2), moon,"black")
        c=Tex(r"m_1").set_color(BLUE).next_to(EARTH, DOWN)
        arrow=Arrow(EARTH.get_center(), EARTH.get_center()+normalize(MOON.get_center()-EARTH.get_center())*get_norm(EARTH.get_center()-MOON.get_center())**(-2)*20, buff=0)
        force=Tex(r"\vec{\mathbf{F} }", "=", "G", "{ {{m_1}} {{m_2}} ", "\over", r"|\vec{\mathbf{x_2} }-\vec{\mathbf{x_1} }|", "^2}", r"{\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", r"\over", r"|", r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} }", r"|}").set_color_by_tex_to_color_map(x_1x_2_color).move_to(np.array([-4, 2, 0]))
        force[6].set_color(WHITE)
        force[6][1:4].set_color(GREY_BROWN)
        force[6][5:8].set_color(BLUE)
        self.add(EARTH, MOON, arrow, force, c)
        self.wait()
        acc=get_acc(EARTH, MOON)
        acc_label=Tex(r"\vec{\mathbf{a} }").next_to(acc, DL).set_color(YELLOW)
        force2=Tex(r"\vec{\mathbf{F} }", "=", "m_1", r"\vec{\mathbf{a} }", "=", "G", "{ {{m_1}} {{m_2}} ", "\over", r"|\vec{\mathbf{x_2} }-\vec{\mathbf{x_1} }|", "^2}", r"{\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", r"\over", r"|", r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} }", r"|}").set_color_by_tex_to_color_map(x_1x_2_color).move_to(np.array([-4, 2, 0])).align_to(force, LEFT)
        force2[9].set_color(WHITE)
        force2[9][1:4].set_color(GREY_BROWN)
        force2[9][5:8].set_color(BLUE)
        self.play(ReplacementTransform(force[0], force2[0]),
        *[ReplacementTransform(i, j) for i, j in zip(force[1:], force2[4:])], )
        self.wait()
        self.play(ReplacementTransform(arrow, acc), Write(acc_label))
        self.wait(0.5)
        self.play(ReplacementTransform(acc_label.copy(), force2[3]), ReplacementTransform(c, force2[2]), Write(force2[1]))
        self.wait()
        self.play(FadeOut(force2[:2]))
        force3=Tex("m_1", r"\vec{\mathbf{a} }", "=", "G", "{m_1", " m_2", "\over", r"|", r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", "|", "^2}", r"{\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", r"\over", r"|", r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", r"|}").set_color_by_tex_to_color_map(x_1x_2_color).move_to(np.array([-4, 2, 0])).align_to(force2[2], LEFT)
        self.remove(force2)
        self.add(force3)
        self.wait()
        force4=Tex("m_1", r"\vec{\mathbf{a} }", "=", "G", "{m_1", "m_2", "(", r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", ")", "\over", r"|", r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", "|", "^3}", ).set_color_by_tex_to_color_map(x_1x_2_color).move_to(np.array([-4, 2, 0]))
        self.play(TransformMatchingTex(force3, force4))
        self.wait()
        force5=Tex(r"\vec{\mathbf{a} }", "=", "G", "{", "m_2", "(", r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", ")", "\over", r"|", r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", "|", "^3}", ).set_color_by_tex_to_color_map(x_1x_2_color).move_to(np.array([-4, 2, 0]))
        self.play(TransformMatchingTex(force4, force5))
        self.wait()
        print(self.t/10)

class lots_of_acc(Scene):
    def construct(self):
        """frame=self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )
        frame.add_updater(lambda obj, dt:obj.increment_theta(0.5 * dt))
        self.add(frame)"""
        self.t=2837
        light = self.camera.light_source
        light.move_to(100*UP+30*OUT)
        light.rotate(self.t/600, about_point=ORIGIN)
        def ro(obj, dt):
            obj.rotate(.1*dt, about_point=ORIGIN)
            self.t+=1
        light.add_updater(ro)
        self.add(light)
        day="http://sq.k12.com.cn/discuz/attachments/month_0812/20081228_bd09baeec765b6c96822PEQQ3dhvkeOn.jpg"
        night="https://apod.nasa.gov/apod/image/0011/earthlights2_dmsp_big.jpg"
        moon="https://gss0.baidu.com/-Po3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/bd315c6034a85edfe622fb0d4b540923dd547575.jpg"
        nasa_landing_sites="https://mars.nasa.gov/system/resources/detail_files/24729_PIA23518-Mars-landing-sites-web.jpg"
        #day="day"
        #night="night"
        #moon="moon"
        text=[
            "当然，加速度不可能只有一个\\\\我们需要全加起来",
            "我们知道速度增量/时间增量是加速度",
            "我们有知道位移/时间是速度",
            r"我们选取一个很小的{{$\mathrm{d}t$}}",
            "我们可以尝试写出这样的伪代码",
            "很好，有了大致思路，我们可以开始实践了！"
        ]
        textvg=VGroup(*[TexText(t).to_edge(DOWN) for t in text])
        EARTH=TexturedSurface(Sphere(radius=0.5).move_to(UP+RIGHT), day, night)
        MOON=TexturedSurface(Sphere(radius=0.25).move_to(DOWN+LEFT*2), moon, "black")#准备一张纯黑图片并命名其为black
        ballist=[Sphere(radius=random.uniform(0.1, 0.5)).move_to(np.array([random.uniform(-7, 7), random.uniform(-4, 4), 0])) for i in range(4)]
        balls=Group()
        for b, texture in zip(ballist, ["MK", "share", "starry", nasa_landing_sites]):
            balls.add(TexturedSurface(b, texture, "black"))
        force=Tex(r"\vec{\mathbf{a} }", "=", "G", "{", "m_2", "(", r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", ")", "\over", r"|", r"\vec{\mathbf{x_2} }", r"-", r"\vec{\mathbf{x_1} } ", "|", "^3}", ).set_color_by_tex_to_color_map(x_1x_2_color).move_to(np.array([-4, 2, 0]))

        self.add(EARTH, MOON, force)
        accs=VGroup(*[get_acc(EARTH, p) for p in [MOON, *balls]])
        acc_label=Tex(r"\vec{\mathbf{a} }").next_to(accs[0], DL).set_color(YELLOW)
        self.add(accs[0], acc_label)
        #self.wait(10)
        acc_labels=VGroup(*[Tex(r"\vec{\mathbf{a_"+str(i)+"} }").set_color(YELLOW).next_to(accs[i-1].get_end(), dir) for i, dir in zip(range(1, 6), [DL, DR, DOWN, LEFT, RIGHT])])
        self.wait()
        self.play(Write(textvg[0]))
        self.wait()
        self.play(*[GrowFromCenter(b) for b in balls])
        self.wait(0.5)
        self.remove(acc_label)
        self.play(ReplacementTransform(acc_label.copy(), acc_labels[0]))
        self.wait(0.5)
        self.play(*[GrowArrow(i) for i in accs[1:]])
        self.wait(0.5)
        self.play(*[Write(acc_) for acc_ in acc_labels[1:]])
        self.wait()
        force2=Tex(r"\vec{\mathbf{a} }", "=", r"\sum", "G", "{", "m_i", "(", r"\vec{\mathbf{x_i} }", r"-", r"\vec{\mathbf{x_1} } ", ")", "\over", r"|", r"\vec{\mathbf{x_i} }", r"-", r"\vec{\mathbf{x_1} } ", "|", "^3}", ).set_color_by_tex_to_color_map(x_1x_2_color).move_to(np.array([-4, 2, 0])).align_to(force, LEFT)
        self.play(TransformMatchingTex(force, force2,
        key_map={
            "m_2":"m_i", r"\vec{\mathbf{x_2} }":r"\vec{\mathbf{x_i} }"
        }))
        sum=Arrow(EARTH.get_center(), accs[0].get_end()+accs[1].get_end()+accs[2].get_end()+accs[3].get_end()+accs[4].get_end()-4*EARTH.get_center(), buff=0).set_color(YELLOW)
        self.wait()
        acc_label.next_to(sum.get_end(), DOWN)

        self.play(*[ReplacementTransform(i, sum) for i in accs], *[ReplacementTransform(i, acc_label) for i in acc_labels], self.camera.frame.animate.shift(DOWN))
        self.bring_to_front(textvg[0])
        self.wait()
        sur=SurroundingRectangle(force2)
        self.play(*[FadeOut(i) for i in [sum, acc_label, textvg[0], balls, MOON, EARTH]], ShowCreation(sur))
        light.clear_updaters()
        force_with_bound=VGroup(force2, sur)
        self.play(force_with_bound.animate.scale(0.5).to_corner(UL), self.camera.frame.animate.shift(UP))
        self.wait()
        velo=Tex(r"{", r"\mathrm{d}\vec{\mathbf{v} }", "\\over", r"\mathrm{d}t", "}", "=", r"\vec{\mathbf{a} }").set_color_by_tex_to_color_map(x_1x_2_color)
        velo2=Tex(r"\mathrm{d}\vec{\mathbf{v} }", "=", r"\vec{\mathbf{a} }", r"\mathrm{d}t").set_color_by_tex_to_color_map(x_1x_2_color)

        self.play(Write(textvg[1]))
        self.wait(0.5)
        self.play(Write(velo))
        self.wait()
        self.play(FadeOut(textvg[1]), TransformMatchingTex(velo, velo2))
        sur2=SurroundingRectangle(velo2)
        self.wait()
        self.play(ShowCreation(sur2))
        self.wait()
        velo_with_bound=VGroup(velo2, sur2)
        self.play(velo_with_bound.animate.scale(0.5).next_to(force_with_bound))
        self.wait()

        posi=Tex(r"{", r"\mathrm{d}\vec{\mathbf{x_1} }", "\\over", r"\mathrm{d}t", "}", "=", r"\vec{\mathbf{v} }").set_color_by_tex_to_color_map(x_1x_2_color)
        posi2=Tex(r"\mathrm{d}\vec{\mathbf{x_1} }", "=", r"\vec{\mathbf{v} }", r"\mathrm{d}t").set_color_by_tex_to_color_map(x_1x_2_color)

        self.play(Write(textvg[2]))
        self.wait(0.5)
        self.play(Write(posi))
        self.wait()
        self.play(TransformMatchingTex(posi, posi2), FadeOut(textvg[2]))
        self.wait()
        sur3=SurroundingRectangle(posi2)
        posi_with_bound=VGroup(posi2, sur3)
        self.play(ShowCreation(sur3))
        self.wait()
        self.play(posi_with_bound.animate.scale(0.5).next_to(velo_with_bound))
        self.wait()
        self.play(Write(textvg[3]))
        dt_amount=Tex("\mathrm{d}t", "=", "0.01").to_corner(UR)
        self.wait()
        self.play(ReplacementTransform(textvg[3][1].copy(), dt_amount[0]), Write(dt_amount[1:]))
        self.wait()
        self.play(Write(textvg[4]), FadeOut(textvg[3]))
        self.wait()
        self.play(force_with_bound.animate.move_to(UP*2), velo_with_bound.animate.move_to(UP), posi_with_bound.animate.move_to(DOWN))
        step3=TexText(r"$\vec{\mathbf{v} }$", "增加", r"$\mathrm{d}\vec{\mathbf{v} }$").set_color_by_tex_to_color_map(x_1x_2_color)
        sur4=SurroundingRectangle(step3)
        Step3=VGroup(step3, sur4).scale(0.5).move_to(ORIGIN)
        step5=TexText(r"$\vec{\mathbf{x_1} }$", "增加", r"$\mathrm{d}\vec{\mathbf{x_1} }$").set_color_by_tex_to_color_map(x_1x_2_color)
        sur5=SurroundingRectangle(step5)
        Step5=VGroup(step5, sur5).scale(0.5).move_to(DOWN*2)
        self.play(*[LaggedStart(Write(i[0]), ShowCreation(i[1]), lag_ratio=1) for i in [Step3, Step5]])
        steps=VGroup(force_with_bound, velo_with_bound, Step3, posi_with_bound, Step5)
        cycle_arrows=VGroup(*[Line(steps[i].get_bottom(), steps[i+1].get_top(), buff=0.06).add_tip() for i in range(4)], CurvedArrow(np.array([-2, steps[-1].get_left()[1], 0]), np.array([-2, steps[0].get_left()[1], 0]), angle=-PI/2))
        self.play(ShowCreation(cycle_arrows), run_time=5)
        self.wait()
        self.play(FadeOut(textvg[4]), Write(textvg[5]))
        self.wait()
        self.play(FadeOut(cycle_arrows),FadeOut(steps),FadeOut(dt_amount),FadeOut(textvg[5]))

class CodeLines_with_index(VGroup):
    CONFIG = {
        'scale_factor': 0.3,
        'line_buff': 0.05,
    }

    def __init__(self,  *codes,  **kwargs):
        digest_config(self,  kwargs)
        super().__init__(*[CodeLine(str(i+1)+" "*(3-len(str(i+1)))+code,  **kwargs).scale(self.scale_factor) for i, code in enumerate(codes)])
        if len(codes) > 1:
            self.arrange(DOWN,  aligned_edge=LEFT,  buff=self.line_buff)

class coding(Scene):
    def construct(self):
        #注释掉text_mobject.py的85行:
        #space.move_to(submobs[max(char_index - 1,  0)].get_center())
        f=open("simulation.txt", "r")
        codes=f.readlines()
        f.close()
        self.text=CodeLines_with_index(
            *codes
        )
        tags=[
            ([2,2],"定义万有引力常数"),
            ([4,8],"定义加速度公式，可以直接导入列表并求和"),
            ([12,18],"让画面转起来"),
            ([20,24],"三个星球"),
            ([25,28],"存储星球加速度、速度、位置、质量的信息"),
            ([30,31],"初始化星球位置"),
            ([33,39],"定义$\\mathrm{updater}$所需函数，使三个星球随时间更新位置\\\\这里使用$\\mathrm{for}$循环是提高精度（即每帧运算十次）\\\\更多有关$\\mathrm{updater}$的内容可以看@$\\mathrm{widcardw}$的视频"),
            ([41,43],"星球们的轨迹"),
        ]

        def get_tag(range,tag):
            if len(range)==1:
                包住的玩意儿=VGroup(self.text[range[0]-1])
            else:
                包住的玩意儿=VGroup(self.text[range[0]-1],self.text[range[1]-1])
            brace=Brace(包住的玩意儿,direction=LEFT)
            text=TexText(tag).scale(0.3).next_to(brace,LEFT)
            return VGroup(brace,text)

        real_tags=Group(*[get_tag(r,tag) for r,tag in tags])

        segments=[[1,1],[2,2],[3,3],[4,8],[9,11],[12,18],[19,19],[20,24],[25,28],[29,29],[30,31],[32,32],[33,39],[40,40],[41,43],[44,-1]]
        count=0
        Group(real_tags,self.text).move_to(ORIGIN).set_width(13)
        for seg in segments:

            if seg in [tag[0] for tag in tags]:
                self.play(Write(self.text[seg[0]-1:seg[1]]),self.camera.frame.animate.move_to( VGroup(self.text[seg[0]-1:seg[1]],real_tags[count]).get_y()*UP ))

                self.play(Write(real_tags[count][1]),GrowFromCenter(real_tags[count][0]))
                count+=1
                self.wait(5)
            else:
                if seg[1]==-1:
                    self.play(Write(self.text[seg[0]-1:]),self.camera.frame.animate.move_to( VGroup(self.text[seg[0]-1:seg[1]]).get_y()*UP ))
                else:
                    self.play(Write(self.text[seg[0]-1:seg[1]]),self.camera.frame.animate.move_to( VGroup(self.text[seg[0]-1:seg[1]]).get_y()*UP ))
                self.wait(5)

        frame=self.camera.frame
        self.play(frame.animate.move_to(ORIGIN).set_euler_angles(
            theta = -30 * DEGREES,
            phi = 70 * DEGREES,
        ),rate_func=exponential_decay,run_time=3)
        frame.add_updater(lambda obj, dt:obj.increment_theta(-0.1 * dt))
        self.add(frame)

        vg=Group(
            Sphere(radius = 0.1, color = RED),
            Sphere(radius = 0.2, color = GREEN),
            Sphere(radius = 0.15, color = BLUE)
        )
        self.a = np.array([np.array([0, 0, 0]), np.array([0, 0, 0]), np.array([0, 0, 0])])
        self.v = np.array([np.array([1, 0, 1]), np.array([0, -1, 0]), np.array([-1, 1, -1])])
        self.x = np.array([np.array([1, 2, 1]), np.array([-2, -2, 1]), np.array([1, 1, 0.5])])
        m = [1, 1, 1]

        for ball,x in zip(vg,self.x):
            ball.move_to(x)

        def update(obj, dt):
            for g in range(30):
                self.a = np.array([get_a(self.x[i], [*self.x[:i], *self.x[i+1:]], m) for i in range(len(self.x))])
                self.v = self.v+self.a*dt/30
                self.x = self.x+self.v*dt/30
                for ball, x in zip(obj, self.x):
                    ball.move_to(x)

        trace=VGroup(
            *[TracedPath(ball.get_center, min_distance_to_new_point = 0.01).set_color(color) for ball,color in zip(vg,[RED,GREEN,BLUE])]
        )
        self.play(*[GrowFromCenter(i) for i in vg])
        self.wait(0.1)
        vg.add_updater(update)
        self.add(vg, trace)
        self.wait(100)
