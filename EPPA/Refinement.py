from manim import *
from Helper import *

set_frame_size()

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Triangle(stroke_color=BLACK).scale(3))
        circle1 = Circle(1.75, color=PRIMARY, stroke_width=0, fill_opacity=.5).shift(UP)
        circle2 = Circle(1.75, color=SECONDARY, stroke_width=0, fill_opacity=.5).shift(DOWN * 1.2 + RIGHT * 1.2)
        circle3 = Circle(1.75, color=TERTIARY, stroke_width=0, fill_opacity=.5).shift(DOWN * 1.2 + LEFT * 1.2)
        self.add(circle1, circle2, circle3)

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Triangle(stroke_color=BLACK).scale(3))
        circle1 = Circle(1.75)
        set1 = Intersection(circle1, Polygon(LEFT * 4 + DOWN, RIGHT * 4 + DOWN, UP * 4), color=PRIMARY, stroke_width=0, fill_opacity=.5).shift(UP)
        circle2 = Circle(1.75)
        set2 = Intersection(circle2, Polygon(LEFT * 1.25 + UP * 4, LEFT * 1.25 + DOWN * 4, RIGHT * 4 + DOWN * 4, RIGHT * 4 + UP * 4), color=SECONDARY, stroke_width=0, fill_opacity=.5).shift(DOWN * 1.2 + RIGHT * 1.2)
        circle3 = Circle(1.75)
        set3 = Intersection(circle3, Polygon(RIGHT * 1.25 + UP * 4, RIGHT * 1.25 + DOWN * 4, LEFT * 4 + DOWN * 4, LEFT * 4 + UP * 4), color=TERTIARY, stroke_width=0, fill_opacity=.5).shift(DOWN * 1.2 + LEFT * 1.2)
        self.add(set1, set2, set3)