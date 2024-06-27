from manim import *
from Helper import *

set_frame_size()

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(6, color=PRIMARY, fill_opacity=.5))

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(6, color=PRIMARY, fill_opacity=.5))
        self.add(Arrow((-3, -3.5, 0), (3, -3.5, 0), color=BLACK))
        self.add(Arrow((-3.5, -3, 0), (-3.5, 3, 0), color=BLACK))

class Image03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(6, color=PRIMARY, fill_opacity=.5))
        self.add(Arrow((-3, -3.5, 0), (3, -3.5, 0), color=BLACK))
        self.add(Arrow((-3.5, -3, 0), (-3.5, 3, 0), color=BLACK))
        self.add(Dot((1.5, 1, 0), color=BLACK))
        self.add(MathTex(r"(x,y)", color=BLACK).shift((2.125, 1.25, 0)))