from manim import *
from Helper import *

set_frame_size()

class InductiveDimension(Scene):
    def setup(self):
        self.camera.background_color = WHITE
        
    def get_axes(self):
        axes = Axes(x_length=7.5, y_length=7.5, tips=False).set_color(BLACK)
        self.add(axes)
        return axes

class Image01(InductiveDimension):
    def construct(self):
        self.setup()
        axes = self.get_axes()

class Image02(InductiveDimension):
    def construct(self):
        self.setup()
        axes = self.get_axes()
        circle = Circle(radius=2, color=PRIMARY, fill_opacity=.5, stroke_width=0).shift(axes.c2p(1, 1))
        self.add(circle)

class Image03(InductiveDimension):
    def construct(self):
        self.setup()
        axes = self.get_axes()
        circle = Circle(radius=2, color=PRIMARY, fill_opacity=.5, stroke_width=10, stroke_color=SECONDARY).shift(axes.c2p(1, 1))
        self.add(circle)

class Image04(InductiveDimension):
    def construct(self):
        self.setup()
        circle = Circle(radius=3.5, stroke_color=BLACK)
        self.add(circle)

class Image05(InductiveDimension):
    def construct(self):
        self.setup()
        circle = Circle(radius=3.5, stroke_color=BLACK)
        self.add(circle)
        arc = Arc(radius=3.5, start_angle=1.1*PI, angle=.3*PI, stroke_width=15, stroke_color=PRIMARY)
        self.add(arc)

class Image06(InductiveDimension):
    def construct(self):
        self.setup()
        circle = Circle(radius=3.5, stroke_color=BLACK)
        self.add(circle)
        arc = Arc(radius=3.5, start_angle=1.1*PI, angle=.3*PI, stroke_width=15, stroke_color=PRIMARY)
        self.add(arc)
        self.add(Dot(circle.point_at_angle(1.1 * PI), radius=.15, color=SECONDARY))
        self.add(Dot(circle.point_at_angle(1.4 * PI), radius=.15, color=SECONDARY))
