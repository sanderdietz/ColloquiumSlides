# Render all images in high quality (1080x1920) using the following command:
# manim -qh AlternatingHarmonicSeries.py Slide01 Slide02 Slide03 Slide04 Slide05 Slide06 Slide07 Slide08 Slide09 Slide10 Slide11 Slide12 Slide13 Slide14 Slide15 Slide16 Slide17

from manim import *

BACKGROUND = "#031b2e"
PRIMARY = "#e1d2c5"
SECONDARY = "#f0a563"

class Slide01(Scene):
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

class Slide02(Scene):
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

class Slide03(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=2.0, height=4.0, stroke_color=WHITE).shift(LEFT)
        text = MathTex(r"1-\frac{1}{2}", color=WHITE).to_edge(UL)

        self.add(rect1)        
        self.add(text)

class Slide04(Scene):
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

class Slide05(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=2.0, height=4.0, stroke_color=WHITE).shift(LEFT)
        rect2 = Rectangle(width=2.0, height=2.67, stroke_color=WHITE).shift(RIGHT).shift(DOWN * .67)
        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}", color=WHITE).to_edge(UL)

        self.add(rect1)
        self.add(rect2)
        self.add(text)

class Slide06(Scene):
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

class Slide07(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=1.0, height=4.0, stroke_color=WHITE).shift(LEFT * 1.5)
        rect2 = Rectangle(width=2.0, height=2.67, stroke_color=WHITE).shift(RIGHT).shift(DOWN * .67)

        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}", color=WHITE).to_edge(UL)

        self.add(rect1)
        self.add(rect2)
        self.add(text)

class Slide08(Scene):
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

class Slide09(Scene):
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

class Slide10(Scene):
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

class Slide11(Scene):
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

class Slide12(Scene):
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

class Slide13(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        for i in range(4):
            height = 4.0 * 4 / (4 + i)
            rect = Rectangle(width=1.0, height=height)
            rect.shift(LEFT * (1.5 - i))
            rect.shift(DOWN * (.5 * (4 - height)))
            self.add(rect)

        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}", color=WHITE).to_edge(UL)
        self.add(text)

class Slide14(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        for i in range(8):
            height = 4.0 * 8 / (8 + i)
            rect = Rectangle(width=.5, height=height)
            rect.shift(LEFT * (1.75 - i * .5))
            rect.shift(DOWN * (.5 * (4 - height)))
            self.add(rect)

        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}-...+\frac{1}{15}", color=WHITE).to_edge(UL)
        self.add(text)

class Slide15(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        for i in range(16):
            height = 4.0 * 16 / (16 + i)
            rect = Rectangle(width=.25, height=height)
            rect.shift(LEFT * (1.875 - i * .25))
            rect.shift(DOWN * (.5 * (4 - height)))
            self.add(rect)

        text = MathTex(r"1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\frac{1}{5}-\frac{1}{6}+\frac{1}{7}-...+\frac{1}{31}", color=WHITE).to_edge(UL)
        self.add(text)

class Slide16(Scene):
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

class Slide17(Scene):
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