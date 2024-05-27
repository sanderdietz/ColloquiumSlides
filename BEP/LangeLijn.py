from manim import *
from Helper import *

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        step_size = .5
        for i in range(6):
            self.add(Line((-6 + i * step_size, -.25, 0), (-6 + i * step_size, .25, 0), color=BLACK))
            self.add(MathTex(i, color=BLACK).shift((-6 + i * step_size, -.5, 0)))
            if i == 5:
                self.add(MathTex("...", color=BLACK).shift((-6 + (i + 1) * step_size, -.5, 0)))
        
        self.add(Line((1, -.25, 0), (1, .25, 0), color=BLACK))
        self.add(MathTex(r"\omega_0", color=BLACK).shift((1, -.5, 0)))

        self.add(Line((6, -.25, 0), (6, .25, 0), color=BLACK))
        self.add(MathTex(r"\omega_1", color=BLACK).shift((6, -.5, 0)))
        
        self.add(Line((-6, 0, 0), (6, 0, 0), color=BLACK, stroke_width=10))