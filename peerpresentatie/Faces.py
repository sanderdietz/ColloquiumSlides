# manim -qh Intro.py Slide01 Slide02 Slide03 Slide04 Slide05 Slide06

from manim import *

BACKGROUND = "#ffffff"
PRIMARY = "#000000"
SECONDARY = "#f0a563"

ANGLE1 = .5 * PI
ANGLE2 = 1.1 * PI
ANGLE3 = -.2 * PI
ANGLE4 = -.6 * PI
ANGLE5 = .3 * PI
ANGLE6 = .8 * PI

class Slide01(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND