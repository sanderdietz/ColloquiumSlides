from manim import *
from Helper import *

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        step_size = .5

        for i in range(6):
            self.add(Line((-6 + i * step_size, 1.75, 0), (-6 + i * step_size, 2.25, 0), color=BLACK))
            self.add(MathTex(i, color=BLACK).shift((-6 + i * step_size, 1.5, 0)))
            if i == 5:
                self.add(MathTex("...", color=BLACK).shift((-6 + (i + 1) * step_size, 1.5, 0)))
        
        self.add(Line((1, 1.75, 0), (1, 2.25, 0), color=BLACK))
        self.add(MathTex(r"n", color=BLACK).shift((1, 1.5, 0)))

        self.add(Line((6, 1.75, 0), (6, 2.25, 0), color=BLACK))
        self.add(MathTex(r"\infty", color=BLACK).shift((6, 1.5, 0)))
        
        self.add(Line((-6, 2, 0), (6, 2, 0), color=BLACK, stroke_width=10))

        self.add(Brace(Line((-6, 2.25, 0), (1, 2.25, 0)), color=BLACK, direction=UP))
        self.add(Brace(Line((1, 2.25, 0), (6, 2.25, 0)), color=BLACK, direction=UP))



        for i in range(6):
            self.add(Line((-6 + i * step_size, -1.75, 0), (-6 + i * step_size, -2.25, 0), color=BLACK))
            self.add(MathTex(i, color=BLACK).shift((-6 + i * step_size, -2.5, 0)))
            if i == 5:
                self.add(MathTex("...", color=BLACK).shift((-6 + (i + 1) * step_size, -2.5, 0)))
        
        self.add(Line((-.5, -2.25, 0), (-.5, -1.75, 0), color=BLACK))
        self.add(MathTex(r"\omega_0", color=BLACK).shift((-.5, -2.5, 0)))

        self.add(Line((3, -2.25, 0), (3, -1.75, 0), color=BLACK))
        self.add(MathTex(r"\alpha", color=BLACK).shift((3, -2.5, 0)))

        self.add(Line((6, -2.25, 0), (6, -1.75, 0), color=BLACK))
        self.add(MathTex(r"\omega_1", color=BLACK).shift((6, -2.5, 0)))
        
        self.add(Line((-6, -2, 0), (6, -2, 0), color=BLACK, stroke_width=10))

        self.add(Brace(Line((-6, -1.75, 0), (3, -1.75, 0)), color=BLACK, direction=UP))
        self.add(Brace(Line((3, -1.75, 0), (6, -1.75, 0)), color=BLACK, direction=UP))