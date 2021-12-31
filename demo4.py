from manimlib import *

class TexTransformExample(Scene):
    def construct(self):
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(
            # 将多个参数传递给Tex，这些参数看起来被连接在一起作为一个表达式
            # 但整个mobject的每个submobject为其中的一个字符串
            # 例如，下面的Tex物件将有5个子物件，对应于表达式[A^2，+，B^2，=，C^2]
            Tex("A^2", "+", "B^2", "=", "C^2"),
            # 这里同理
            Tex("A^2", "=", "C^2", "-", "B^2"),
            # 或者，你可以传入关键字参数isolate，其中包含一个字符串列表
            # 这些字符串应该作为它们自己的子物件存在
            # 因此，下面的一行相当于它下面注释掉的一行
            Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
            # Tex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
            Tex("A = \\sqrt{(C + B)(C - B)}", isolate=["A", *to_isolate])
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": TEAL,
                "C": GREEN,
            })

        play_kw = {"run_time": 2}
        self.add(lines[0])
        # TransformMatchingTex将源和目标中具有匹配tex字符串的部分对应变换
        # 传入path_arc，使每个部分旋转到它们的最终位置，这种效果对于重新排列一个方程是很好的
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()

        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]),
            **play_kw
        )
        self.wait()
        # …这看起来很好，但由于在lines[2]中没有匹配"C^2"或"B^2"的tex，这些子物件会淡出
        # 而C和B两个子物件会淡入，如果我们希望C^2转到C，而B^2转到B，我们可以用key_map来指定
        self.play(FadeOut(lines[2]))
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                }
            ),
            **play_kw
        )
        self.wait()

        # 也许我们想把^2上的指数转换成根号。目前，lines[2]将表达式A^2视为一个单元
        # 因此我们可能会需要创建同一line的新版本，该line仅分隔出A
        # 这样，当TransformMatchingTex将所有匹配的部分对应时，唯一的不匹配将是来自new_line2的"^2"
        # 和来自最终行的"\sqrt"之间的不匹配。通过传入transform_missmatches=True，它会将此"^2"转换为"\sqrt"
        new_line2 = Tex("A^2 = (C + B)(C - B)", isolate=["A", *to_isolate])
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                new_line2, lines[3],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(3)
        self.play(FadeOut(lines, RIGHT))

        # 或者，如果您不想故意分解tex字符串，您可以使用TransformMatchingShapes
        # 它将尝试将源mobject的所有部分与目标的部分对齐，而不考虑每个部分中的子对象层次结构
        # 根据这些部分是否具有相同的形状（尽其所能）来自动匹配变换
        source = Text("the morse code", height=1)
        target = Text("here come dots", height=1)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()