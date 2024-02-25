# Render all images in high quality (1080x1920) using the following command:
# manim -qh AlternatingHarmonicSeries.py PartialSum1 PartialSum2 PartialSum2Intermediate PartialSum3 PartialSum3Intermediate PartialSum4 PartialSum4Intermediate PartialSum5 PartialSum5Intermediate PartialSum6 PartialSum6Intermediate PartialSum7 PartialSum7Intermediate PartialSum15Intermediate PartialSum31Intermediate Limit1 Limit2

from manim import *

BACKGROUND = "#031b2e"
PRIMARY = "#e1d2c5"
SECONDARY = "#f0a563"

class PartialSum1(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect_new = Rectangle(width=4.0, height=4.0, stroke_color=WHITE)
        brace_x = BraceLabel(obj=rect_new, text="1", brace_direction=DOWN)
        brace_y = BraceLabel(obj=rect_new, text="1", brace_direction=LEFT)
        brace_x.fill_color = WHITE
        brace_y.fill_color = WHITE

        text = MathTex(r"1", color=WHITE).to_edge(UL)
        box_text = MathTex(r"1", color=WHITE).move_to(rect_new.get_center())

        self.add(rect_new)
        self.add(brace_x)
        self.add(brace_y)

        self.add(text)
        self.add(box_text)

class PartialSum2(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=2.0, height=4.0, color=GRAY).shift(LEFT)
        rect_new = Rectangle(width=2.0, height=4.0, color=SECONDARY, stroke_width=10).shift(RIGHT)
        brace_x = BraceLabel(obj=rect_new, text=r"\frac{1}{2}", brace_direction=DOWN)
        brace_y = BraceLabel(obj=rect_new, text="1", brace_direction=RIGHT)
        brace_x.fill_color = SECONDARY
        brace_y.fill_color = SECONDARY

        text = MathTex(r"1\mathbf{-\frac{1}{2}}", color=WHITE).to_edge(UL)
        text[0][-4:].set_color(SECONDARY)
        box_text = MathTex(r"\mathbf{-\frac{1}{2}}", color=SECONDARY).move_to(rect_new.get_center())

        self.add(rect1)
        self.add(rect_new)
        self.add(brace_x)
        self.add(brace_y)
        
        self.add(text)
        self.add(box_text)

class PartialSum2Intermediate(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=2.0, height=4.0, stroke_color=WHITE).shift(LEFT)
        text = MathTex(r"1-\frac{1}{2}", color=WHITE).to_edge(UL)

        self.add(rect1)        
        self.add(text)

class PartialSum3(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=2.0, height=4.0, color=GRAY).shift(LEFT)
        rect_new = Rectangle(width=2.0, height=2.67, color=PRIMARY, stroke_width=10).shift(RIGHT).shift(DOWN * .67)
        brace_x = BraceLabel(obj=rect_new, text=r"\frac{1}{2}", brace_direction=DOWN)
        brace_y = BraceLabel(obj=rect_new, text=r"\frac{2}{3}", brace_direction=RIGHT)
        brace_x.fill_color = PRIMARY
        brace_y.fill_color = PRIMARY

        text = MathTex(r"1-\frac{1}{2}\mathbf{+\frac{1}{3}}", color=WHITE).to_edge(UL)
        text[0][-4:].set_color(PRIMARY)
        box_text = MathTex(r"\mathbf{+\frac{1}{3}}", color=PRIMARY).move_to(rect_new.get_center())

        self.add(rect1)
        self.add(rect_new)
        self.add(brace_x)
        self.add(brace_y)
        
        self.add(text)
        self.add(box_text)

class PartialSum3Intermediate(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=2.0, height=4.0, stroke_color=WHITE).shift(LEFT)
        rect2 = Rectangle(width=2.0, height=2.67, stroke_color=WHITE).shift(RIGHT).shift(DOWN * .67)
        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}", color=WHITE).to_edge(UL)

        self.add(rect1)
        self.add(rect2)
        self.add(text)

class PartialSum4(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=1.0, height=4.0, color=GRAY).shift(LEFT * 1.5)
        rect2 = Rectangle(width=2.0, height=2.67, color=GRAY).shift(RIGHT).shift(DOWN * .67)
        rect_new = Rectangle(width=1.0, height=4.0, color=SECONDARY, stroke_width=10).shift(LEFT * .5)
        brace_x = BraceLabel(obj=rect_new, text=r"\frac{1}{4}", brace_direction=DOWN)
        brace_y = BraceLabel(obj=rect_new, text=r"1", brace_direction=RIGHT)
        brace_x.fill_color = SECONDARY
        brace_y.fill_color = SECONDARY

        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}\mathbf{-\frac{1}{4}}", color=WHITE).to_edge(UL)
        text[0][-4:].set_color(SECONDARY)
        box_text = MathTex(r"\mathbf{-\frac{1}{4}}", color=SECONDARY).move_to(rect_new.get_center())

        self.add(rect1)
        self.add(rect2)
        self.add(rect_new)
        self.add(brace_x)
        self.add(brace_y)
        
        self.add(text)
        self.add(box_text)

class PartialSum4Intermediate(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=1.0, height=4.0, stroke_color=WHITE).shift(LEFT * 1.5)
        rect2 = Rectangle(width=2.0, height=2.67, stroke_color=WHITE).shift(RIGHT).shift(DOWN * .67)

        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}", color=WHITE).to_edge(UL)

        self.add(rect1)
        self.add(rect2)
        self.add(text)

class PartialSum5(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=1.0, height=4.0, color=GRAY).shift(LEFT * 1.5)
        rect2 = Rectangle(width=2.0, height=2.67, color=GRAY).shift(RIGHT).shift(DOWN * .67)
        rect_new = Rectangle(width=1.0, height=3.2, color=PRIMARY, stroke_width=10).shift(LEFT * .5).shift(DOWN * .4)
        brace_x = BraceLabel(obj=rect_new, text=r"\frac{1}{4}", brace_direction=DOWN)
        brace_y = BraceLabel(obj=rect_new, text=r"\frac{4}{5}", brace_direction=RIGHT)
        brace_x.fill_color = PRIMARY
        brace_y.fill_color = PRIMARY

        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}\mathbf{+\frac{1}{5}}", color=WHITE).to_edge(UL)
        text[0][-4:].set_color(PRIMARY)
        box_text = MathTex(r"\mathbf{+\frac{1}{5}}", color=PRIMARY).move_to(rect_new.get_center())

        self.add(rect1)
        self.add(rect2)
        self.add(rect_new)
        self.add(brace_x)
        self.add(brace_y)
        
        self.add(text)
        self.add(box_text)

class PartialSum5Intermediate(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=1.0, height=4.0, stroke_color=WHITE).shift(LEFT * 1.5)
        rect2 = Rectangle(width=2.0, height=2.67, stroke_color=WHITE).shift(RIGHT).shift(DOWN * .67)
        rect3 = Rectangle(width=1.0, height=3.2, stroke_color=WHITE).shift(LEFT * .5).shift(DOWN * .4)
        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}", color=WHITE).to_edge(UL)

        self.add(rect1)
        self.add(rect2)
        self.add(rect3)
        self.add(text)

class PartialSum6(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=1.0, height=4.0, color=GRAY).shift(LEFT * 1.5)
        rect2 = Rectangle(width=1.0, height=3.2, color=GRAY).shift(LEFT * .5).shift(DOWN * .4)
        rect3 = Rectangle(width=1.0, height=2.67, color=GRAY).shift(RIGHT * .5).shift(DOWN * .67)
        rect_new = Rectangle(width=1.0, height=2.67, color=SECONDARY, stroke_width=10).shift(RIGHT * 1.5).shift(DOWN * .67)
        brace_x = BraceLabel(obj=rect_new, text=r"\frac{1}{4}", brace_direction=DOWN)
        brace_y = BraceLabel(obj=rect_new, text=r"\frac{2}{3}", brace_direction=RIGHT)
        brace_x.fill_color = SECONDARY
        brace_y.fill_color = SECONDARY

        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}\mathbf{-\frac{1}{6}}", color=WHITE).to_edge(UL)
        text[0][-4:].set_color(SECONDARY)
        box_text = MathTex(r"\mathbf{-\frac{1}{6}}", color=SECONDARY).move_to(rect_new.get_center())

        self.add(rect1)
        self.add(rect2)
        self.add(rect3)
        self.add(rect_new)
        self.add(brace_x)
        self.add(brace_y)
        
        self.add(text)
        self.add(box_text)

class PartialSum6Intermediate(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=1.0, height=4.0, stroke_color=WHITE).shift(LEFT * 1.5)
        rect2 = Rectangle(width=1.0, height=3.2, stroke_color=WHITE).shift(LEFT * .5).shift(DOWN * .4)
        rect3 = Rectangle(width=1.0, height=2.67, stroke_color=WHITE).shift(RIGHT * .5).shift(DOWN * .67)
        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}", color=WHITE).to_edge(UL)

        self.add(rect1)
        self.add(rect2)
        self.add(rect3)
        self.add(text)

class PartialSum7(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=1.0, height=4.0, color=GRAY).shift(LEFT * 1.5)
        rect2 = Rectangle(width=1.0, height=3.2, color=GRAY).shift(LEFT * .5).shift(DOWN * .4)
        rect3 = Rectangle(width=1.0, height=2.67, color=GRAY).shift(RIGHT * .5).shift(DOWN * .67)
        rect_new = Rectangle(width=1.0, height=2.29, color=PRIMARY, stroke_width=10).shift(RIGHT * 1.5).shift(DOWN * .86)
        brace_x = BraceLabel(obj=rect_new, text=r"\frac{1}{4}", brace_direction=DOWN)
        brace_y = BraceLabel(obj=rect_new, text=r"\frac{4}{7}", brace_direction=RIGHT)
        brace_x.fill_color = PRIMARY
        brace_y.fill_color = PRIMARY

        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}\mathbf{+\frac{1}{7}}", color=WHITE).to_edge(UL)
        text[0][-4:].set_color(PRIMARY)
        box_text = MathTex(r"\mathbf{+\frac{1}{7}}", color=PRIMARY).move_to(rect_new.get_center())

        self.add(rect1)
        self.add(rect2)
        self.add(rect3)
        self.add(rect_new)
        self.add(brace_x)
        self.add(brace_y)
        
        self.add(text)
        self.add(box_text)

class PartialSum7Intermediate(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=1.0, height=4.0, stroke_color=WHITE).shift(LEFT * 1.5)
        rect2 = Rectangle(width=1.0, height=3.2, stroke_color=WHITE).shift(LEFT * .5).shift(DOWN * .4)
        rect3 = Rectangle(width=1.0, height=2.67, stroke_color=WHITE).shift(RIGHT * .5).shift(DOWN * .67)
        rect4 = Rectangle(width=1.0, height=2.29, stroke_color=WHITE).shift(RIGHT * 1.5).shift(DOWN * .86)
        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}", color=WHITE).to_edge(UL)

        self.add(rect1)
        self.add(rect2)
        self.add(rect3)
        self.add(rect4)
        self.add(text)

class PartialSum15Intermediate(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=.5, height=4.0, stroke_color=WHITE).shift(LEFT * 1.75) # 1
        rect2 = Rectangle(width=.5, height=3.56, stroke_color=WHITE).shift(LEFT * 1.25).shift(DOWN * .22) # 8/9
        rect3 = Rectangle(width=.5, height=3.2, stroke_color=WHITE).shift(LEFT * .75).shift(DOWN * .4) # 8/10
        rect4 = Rectangle(width=.5, height=2.91, stroke_color=WHITE).shift(LEFT * .25).shift(DOWN * .55) # 8/11
        rect5 = Rectangle(width=.5, height=2.67, stroke_color=WHITE).shift(RIGHT * .25).shift(DOWN * .67) # 8/12
        rect6 = Rectangle(width=.5, height=2.46, stroke_color=WHITE).shift(RIGHT * .75).shift(DOWN * .77) # 8/13
        rect7 = Rectangle(width=.5, height=2.29, stroke_color=WHITE).shift(RIGHT * 1.25).shift(DOWN * .86) # 8/14
        rect8 = Rectangle(width=.5, height=2.13, stroke_color=WHITE).shift(RIGHT * 1.75).shift(DOWN * .93) # 8/15
        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}-...+\frac{1}{15}", color=WHITE).scale(.8).to_edge(UL)

        self.add(rect1)
        self.add(rect2)
        self.add(rect3)
        self.add(rect4)
        self.add(rect5)
        self.add(rect6)
        self.add(rect7)
        self.add(rect8)
        self.add(text)

class PartialSum31Intermediate(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=.25, height=4.0, stroke_color=WHITE).shift(LEFT * 1.875) # 1
        rect2 = Rectangle(width=.25, height=3.76, stroke_color=WHITE).shift(LEFT * 1.625).shift(DOWN * .12) # 16/17
        rect3 = Rectangle(width=.25, height=3.56, stroke_color=WHITE).shift(LEFT * 1.375).shift(DOWN * .22) # 16/18
        rect4 = Rectangle(width=.25, height=3.37, stroke_color=WHITE).shift(LEFT * 1.125).shift(DOWN * .32) # 16/19
        rect5 = Rectangle(width=.25, height=3.2, stroke_color=WHITE).shift(LEFT * .875).shift(DOWN * .4) # 16/20
        rect6 = Rectangle(width=.25, height=3.05, stroke_color=WHITE).shift(LEFT * .625).shift(DOWN * .48) # 16/21
        rect7 = Rectangle(width=.25, height=2.91, stroke_color=WHITE).shift(LEFT * .375).shift(DOWN * .55) # 16/22
        rect8 = Rectangle(width=.25, height=2.78, stroke_color=WHITE).shift(LEFT * .125).shift(DOWN * .61) # 16/23
        rect9 = Rectangle(width=.25, height=2.67, stroke_color=WHITE).shift(RIGHT * .125).shift(DOWN * .67) # 16/24
        rect10 = Rectangle(width=.25, height=2.56, stroke_color=WHITE).shift(RIGHT * .375).shift(DOWN * .72) # 16/25
        rect11 = Rectangle(width=.25, height=2.46, stroke_color=WHITE).shift(RIGHT * .625).shift(DOWN * .77) # 16/26
        rect12 = Rectangle(width=.25, height=2.37, stroke_color=WHITE).shift(RIGHT * .875).shift(DOWN * .81) # 16/27
        rect13 = Rectangle(width=.25, height=2.29, stroke_color=WHITE).shift(RIGHT * 1.125).shift(DOWN * .86) # 16/28
        rect14 = Rectangle(width=.25, height=2.21, stroke_color=WHITE).shift(RIGHT * 1.375).shift(DOWN * .90) # 16/29
        rect15 = Rectangle(width=.25, height=2.13, stroke_color=WHITE).shift(RIGHT * 1.625).shift(DOWN * .93) # 16/30
        rect16 = Rectangle(width=.25, height=2.06, stroke_color=WHITE).shift(RIGHT * 1.875).shift(DOWN * .97) # 16/31
        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}-...+\frac{1}{31}", color=WHITE).to_edge(UL)

        self.add(rect1)
        self.add(rect2)
        self.add(rect3)
        self.add(rect4)
        self.add(rect5)
        self.add(rect6)
        self.add(rect7)
        self.add(rect8)
        self.add(rect9)
        self.add(rect10)
        self.add(rect11)
        self.add(rect12)
        self.add(rect13)
        self.add(rect14)
        self.add(rect15)
        self.add(rect16)
        self.add(text)

class Limit1(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        grid = Axes(
            x_range=[1, 2],
            y_range=[0, 1],
            x_length=4,
            y_length=4,
            axis_config={"include_ticks": False},
            tips=False
        )
        graph = grid.plot(lambda x: 1 / x, x_range=[1, 2])
        area = grid.get_area(
            graph,
            x_range=(1, 2),
            color=WHITE,
            opacity=1
        )

        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}-...", color=WHITE).to_edge(UL)
        self.add(grid, graph, area, text)

class Limit2(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        grid = Axes(
            x_range=[0, 3],
            y_range=[0, 2],
            x_length=6,
            y_length=4,
            axis_config={"include_numbers": True},
            tips=False
        ).shift(DOWN * .5)
        graph = grid.plot(lambda x: 1 / x, x_range=[.5, 3])
        area = grid.get_area(
            graph,
            x_range=(1, 2),
            color=WHITE,
            opacity=1
        )

        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}-...=\int_1^2\frac{1}{x}\mathrm{d}x=\log(2)", color=WHITE).to_edge(UL)
        self.add(grid, graph, area, text)