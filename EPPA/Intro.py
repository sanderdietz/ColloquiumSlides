from manim import *

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Dot(color=BLACK))

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(NumberLine(length=12).set_color(BLACK))

class Image03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Axes(tips=False).set_color(BLACK))

class Image04(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(ThreeDAxes(tips=False).set_color(BLACK))
        self.set_camera_orientation(phi=.4 * PI, theta=.25 * PI, (0, 0, 0))