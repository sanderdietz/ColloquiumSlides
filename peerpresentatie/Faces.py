# manim -qh Intro.py Image01 Image02 Image03 Image04 Image05 Image06

from manim import *

config.frame_height = 8
config.frame_width = 8
config.frame_size = (1000, 1000)

BACKGROUND = "#ffffff"
PRIMARY = "#000000"
SECONDARY = "#00a6d6"
TERTIARY = "#e03c31"

ANGLE1 = .5 * PI
ANGLE2 = 1.1 * PI
ANGLE3 = -.2 * PI
ANGLE4 = -.6 * PI
ANGLE5 = .3 * PI
ANGLE6 = .8 * PI

class Image01(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND