from manim import *
from Helper import *

config.frame_height = 2
config.frame_width = 8
config.frame_size = (1920, 480)

class RationalNumbers(Scene):
    def setup(self):
        self.camera.background_color = WHITE
        self.add(NumberLine(x_range=[-10, 10, 1], include_numbers=True, font_size=14, length=8, stroke_width=1).set_color(BLACK))
        
class Image01(RationalNumbers):
    def construct(self):
        self.setup()

class Image02(RationalNumbers):
    def construct(self):
        self.setup()
        self.add(RoundedRectangle(corner_radius=.05, height=.1, width=4, color=PRIMARY, fill_opacity=.5, stroke_width=0).shift(RIGHT * 2))
        self.add(RoundedRectangle(corner_radius=.05, height=.1, width=7, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift(LEFT * 1.5))

class Image03(RationalNumbers):
    def construct(self):
        C = .4
        self.setup()
        self.add(RoundedRectangle(corner_radius=.05, height=.1, width=10*C, color=PRIMARY, fill_opacity=.5, stroke_width=0).shift(RIGHT * .4 * (PI + 5)))
        self.add(RoundedRectangle(corner_radius=.05, height=.1, width=20*C, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift(LEFT * .4 * (10 - PI)))
