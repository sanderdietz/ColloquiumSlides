# Render all images in high quality (1080x1920) using the following command:
# manim -qh PSeries.py Slide00 Slide01 Slide02 Slide03


from manim import *

BACKGROUND = "#031b2d"
PRIMARY = "#f0a563"
SECONDARY = "#e1d2c5"

class Slide00(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        XMAX = 4.0 + 10.0 / 27.0
        YMAX = 9.0 * 4.0 / 16.0
        WIDTH = 12.0 + 10.0 / 9.0
        HEIGHT = 9.0 * 12.0 / 16.0
        UNITX = WIDTH / XMAX
        UNITY = HEIGHT / YMAX

        grid = Axes(x_range=[0, XMAX], y_range=[0, YMAX], x_length=WIDTH, y_length=HEIGHT, axis_config={"include_numbers": False}, tips=False).shift(RIGHT * 5.0 / 9.0)
        graph = grid.plot(lambda x: 1 / (x * x) , x_range=[1 / np.sqrt(YMAX), XMAX], color=SECONDARY)
        self.add(grid)
        for i in range(1, int(XMAX) + 1):
            rect = Rectangle(width=UNITX, height=UNITY/(i*i), color=PRIMARY).shift(DOWN * UNITY * .5 * (YMAX - 1 / (i * i))).shift(LEFT * UNITX * (.5 * (XMAX + 1) - i)).shift(RIGHT * 5.0 / 9.0)
            self.add(rect)
        self.add(graph)

class Slide01(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        XMAX = 4.0
        YMAX = 9.0 * XMAX / 16.0
        WIDTH = 12.0
        HEIGHT = 9.0 * WIDTH / 16.0
        UNITX = WIDTH / XMAX
        UNITY = HEIGHT / YMAX

        for i in range(1, int(XMAX) + 1):
            rect = Rectangle(width=UNITX, height=UNITY/(i*i), color=PRIMARY).shift(DOWN * UNITY * .5 * (YMAX - 1 / (i * i))).shift(LEFT * UNITX * (.5 * (XMAX + 1) - i))
            text = MathTex(r"\frac{1}{{" + str(i) + r"}^p}").move_to(rect).shift(UP * UNITY * .5 * (1 / (i * i))).shift(UP * .75)
            self.add(rect, text)

class Slide02(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        XMAX = 4.0 + 10.0 / 27.0
        YMAX = 9.0 * 4.0 / 16.0
        WIDTH = 12.0 + 10.0 / 9.0
        HEIGHT = 9.0 * 12.0 / 16.0
        UNITX = WIDTH / XMAX
        UNITY = HEIGHT / YMAX

        grid = Axes(x_range=[0, XMAX], y_range=[0, YMAX], x_length=WIDTH, y_length=HEIGHT, axis_config={"include_numbers": True}, tips=False).shift(RIGHT * 5.0 / 9.0)
        graph = grid.plot(lambda x: 1 / (x * x) , x_range=[1 / np.sqrt(YMAX), XMAX], color=SECONDARY)
        self.add(grid)
        for i in range(1, int(XMAX) + 1):
            rect = Rectangle(width=UNITX, height=UNITY/(i*i), color=PRIMARY).shift(DOWN * UNITY * .5 * (YMAX - 1 / (i * i))).shift(LEFT * UNITX * (.5 * (XMAX + 1) - i)).shift(RIGHT * 5.0 / 9.0)
            text = MathTex(r"\frac{1}{{" + str(i) + r"}^p}").move_to(rect).scale(.5).shift(RIGHT * UNITX * .5).shift(UP * UNITY * .5 * (1 / (i * i))).shift(UR * .35)
            self.add(rect, text)
        self.add(graph)
        function = MathTex(r"y=\frac{1}{x^p}", color=SECONDARY).scale(.75).shift(LEFT * 4.25 + UP)
        self.add(function)

class Slide03(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        XMAX = 4.0 + 10.0 / 27.0
        YMAX = 9.0 * 4.0 / 16.0
        WIDTH = 12.0 + 10.0 / 9.0
        HEIGHT = 9.0 * 12.0 / 16.0
        UNITX = WIDTH / XMAX
        UNITY = HEIGHT / YMAX

        grid = Axes(x_range=[0, XMAX], y_range=[0, YMAX], x_length=WIDTH, y_length=HEIGHT, axis_config={"include_numbers": True}, tips=False).shift(RIGHT * 5.0 / 9.0)
        graph = grid.plot(lambda x: 1 / (x * x) , x_range=[1 / np.sqrt(YMAX), XMAX], color=SECONDARY)
        self.add(grid)
        for i in range(1, int(XMAX) + 1):
            rect = Rectangle(width=UNITX, height=UNITY/(i*i), color=PRIMARY).shift(DOWN * UNITY * .5 * (YMAX - 1 / (i * i))).shift(LEFT * UNITX * (.5 * (XMAX + 1) - i)).shift(RIGHT * 5.0 / 9.0)
            text = MathTex(r"\frac{1}{{" + str(i) + r"}^p}").move_to(rect).scale(.5).shift(RIGHT * UNITX * .5).shift(UP * UNITY * .5 * (1 / (i * i))).shift(UR * .35)
            self.add(rect, text)
        self.add(graph)
        function = MathTex(r"y=\frac{1}{x^p}", color=SECONDARY).scale(.75).shift(LEFT * 4.25 + UP)
        self.add(function)
        eq = MathTex(r"1+\frac{1}{2^p}+\frac{1}{3^p}+\frac{1}{4^p}+...\leq1+\int_1^\infty\frac{1}{x^p}\mathrm{d}x").to_edge(UR)
        self.add(eq)
