from manim import *
from Helper import *

set_frame_size()

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        triangle = Polygon(UP * 2.5, LEFT * 1.25 * np.sqrt(3) + DOWN * 1.25, RIGHT * 1.25 * np.sqrt(3) + DOWN * 1.25, color=BLACK, fill_opacity=.2)
        circle1 = Circle(1.75, color=PRIMARY, stroke_width=0, fill_opacity=.5).shift(UP)
        circle2 = Circle(1.75, color=SECONDARY, stroke_width=0, fill_opacity=.5).shift(UP).rotate(PI * 2 / 3, about_point=ORIGIN)
        circle3 = Circle(1.75, color=TERTIARY, stroke_width=0, fill_opacity=.5).shift(UP).rotate(PI * 4 / 3, about_point=ORIGIN)

        group = VGroup(triangle, circle1, circle2, circle3).scale(1.5)
        self.add(group)

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        triangle = Polygon(UP * 2.5, LEFT * 1.25 * np.sqrt(3) + DOWN * 1.25, RIGHT * 1.25 * np.sqrt(3) + DOWN * 1.25, color=BLACK, fill_opacity=.2)

        kite = Union(Triangle().shift(DOWN).rotate(PI * 7 / 6, about_point=ORIGIN),
                      Triangle().shift(DOWN).rotate(PI * 5 / 6, about_point=ORIGIN), color=TEAL
        ).scale(2).shift(UP * .75)
        circle = Circle(1.75).shift(UP)

        shape1 = Intersection(circle, kite, color=PRIMARY, stroke_width=0, fill_opacity=.5)
        shape2 = Intersection(circle, kite, color=SECONDARY, stroke_width=0, fill_opacity=.5).rotate(PI * 2 / 3, about_point=ORIGIN)
        shape3 = Intersection(circle, kite, color=TERTIARY, stroke_width=0, fill_opacity=.5).rotate(PI * 4 / 3, about_point=ORIGIN)

        group = VGroup(triangle, shape1, shape2, shape3).scale(1.5)
        self.add(group)
