from manim import *
from Helper import *

config.frame_height = 8
config.frame_width = 12
config.frame_size = (1500, 1000)

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(6, color=PRIMARY, fill_opacity=.5).shift(RIGHT * 1.5))
        self.add(Line((-4.5, 3, 0), (-4.5, -3, 0), color=PRIMARY))
        self.add(DoubleArrow((-4.5, 0, 0), (-1.5, 0, 0), color=BLACK))

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(6, color=PRIMARY, fill_opacity=.5).shift(RIGHT * 1.5))
        self.add(Line((-4.5, 3, 0), (-4.5, -3, 0), color=PRIMARY))
        self.add(Dot((-4.5, 1, 0), color=SECONDARY))
        self.add(Dot((2.5, -1, 0), color=SECONDARY))
        self.add(DoubleArrow((-4.5, 1, 0), (2.5, -1, 0), color=BLACK))