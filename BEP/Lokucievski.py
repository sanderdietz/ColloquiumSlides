from manim import *
from Helper import *

class Image01(Scene):
    def cantor(self, x, y, width):
        if width >= .001 and y > -4:
            self.add(Line((x, y, 0), (x + width, y, 0), color=BLACK, stroke_width=10))
            y -= 1
            self.cantor(x, y, width / 3)
            self.cantor(x + width * 2 / 3, y, width / 3)

    def construct(self):
        self.camera.background_color = WHITE
        self.cantor(-6, 3, 12)

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        step_size = .5
        for i in range(6):
            self.add(Line((-6 + i * step_size, -.25, 0), (-6 + i * step_size, .25, 0), color=BLACK))
            self.add(MathTex(i, color=BLACK).shift((-6 + i * step_size, -.5, 0)))
            if i == 5:
                self.add(MathTex("...", color=BLACK).shift((-6 + (i + 1) * step_size, -.5, 0)))
        
        self.add(Line((1, -.25, 0), (1, .25, 0), color=BLACK))
        self.add(MathTex("\omega_0", color=BLACK).shift((1, -.5, 0)))

        self.add(Line((6, -.25, 0), (6, .25, 0), color=BLACK))
        self.add(MathTex("\omega_1", color=BLACK).shift((6, -.5, 0)))
        
        self.add(Line((-6, 0, 0), (6, 0, 0), color=BLACK, stroke_width=10))

class Image03(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.endpoints = set()

    def cantor(self, start, width):
        if width > .025:
            self.endpoints.add(start)
            self.endpoints.add(start + width)
            self.cantor(start, width / 3)
            self.cantor(start + width * 2 / 3, width / 3)

    def construct(self):
        self.camera.background_color = WHITE

        self.cantor(-2, 4)
        for y in self.endpoints:
            self.add(Line((-6, y, 0), (6, y, 0), color=BLACK, stroke_width=1))
        
        self.add(Line((0, -2, 0), (0, 2, 0), color=BLACK))

        self.add(MathTex("0", color=BLACK).shift((-6, -2.25, 0)))
        self.add(MathTex("0", color=BLACK).shift((6, -2.25, 0)))
        self.add(MathTex("\omega_1", color=BLACK).shift((0, -2.25, 0)))
        self.add(MathTex("C", color=BLACK).shift((-6.25, 0, 0)))
        self.add(MathTex("C", color=BLACK).shift((6.25, 0, 0)))
        self.add(MathTex("L", color=BLACK).shift((-3, 2.25, 0)))
        self.add(MathTex("L", color=BLACK).shift((3, 2.25, 0)))

