from manim import *
from Helper import *

set_frame_size()

class CoveringDimension(Scene):
    def setup(self):
        self.camera.background_color = WHITE
        self.add(Square(6, stroke_color=BLACK))
        
class Image01(CoveringDimension):
    def construct(self):
        self.setup()

class Image02(CoveringDimension):
    def construct(self):
        self.setup()
        self.add(Circle(radius=2.5, color=PRIMARY, fill_opacity=.5, stroke_width=0).shift(UL * 1.3))
        self.add(Circle(radius=2.5, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift(UR * 1.3))
        self.add(Circle(radius=2.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift(DL * 1.3))
        self.add(Circle(radius=2.5, color=QUATERNIARY, fill_opacity=.5, stroke_width=0).shift(DR * 1.3))

class Image03(CoveringDimension):
    def construct(self):
        self.setup()
        self.add(Intersection(Circle(radius=2.5).shift(UL * 1.3), Polygon([-4, -2, 0], [-4, 4, 0], [2, 4, 0]), color=PRIMARY, fill_opacity=.5, stroke_width=0))
        self.add(Circle(radius=2.5, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift(UR * 1.3))
        self.add(Circle(radius=2.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift(DL * 1.3))
        self.add(Circle(radius=2.5, color=QUATERNIARY, fill_opacity=.5, stroke_width=0).shift(DR * 1.3))

class Image04(CoveringDimension):
    def construct(self):
        self.setup()
        self.add(Intersection(Circle(radius=2.5).shift(UL * 1.3), Polygon([-4, -2, 0], [-4, 4, 0], [2, 4, 0]), color=PRIMARY, fill_opacity=.5, stroke_width=0))
        self.add(Circle(radius=2.5, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift(UR * 1.3))
        self.add(Circle(radius=2.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift(DL * 1.3))
        self.add(Intersection(Circle(radius=2.5).shift(DR * 1.3), Polygon([-2, -4, 0], [4, -4, 0], [4, 2, 0]), color=QUATERNIARY, fill_opacity=.5, stroke_width=0))

class Image05(CoveringDimension):
    def construct(self):
        self.setup()
        self.add(Intersection(Circle(radius=2.5).shift(UL * 1.3), Polygon([-4, -2, 0], [-4, 4, 0], [2, 4, 0]), color=PRIMARY, fill_opacity=.5, stroke_width=0))
        self.add(Intersection(Circle(radius=2.5).shift(UR * 1.3), Polygon([-4, 3.68, 0], [4, 4, 0], [3.68, -4, 0]), color=SECONDARY, fill_opacity=.5, stroke_width=0))
        self.add(Circle(radius=2.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift(DL * 1.3))
        self.add(Intersection(Circle(radius=2.5).shift(DR * 1.3), Polygon([-2, -4, 0], [4, -4, 0], [4, 2, 0]), color=QUATERNIARY, fill_opacity=.5, stroke_width=0))

class Image06(CoveringDimension):
    def construct(self):
        self.setup()
        self.add(Intersection(Circle(radius=2.5).shift(UL * 1.3), Polygon([-4, -2, 0], [-4, 4, 0], [2, 4, 0]), color=PRIMARY, fill_opacity=.5, stroke_width=0))
        self.add(Intersection(Circle(radius=2.5).shift(UR * 1.3), Polygon([-4, 3.68, 0], [4, 4, 0], [3.68, -4, 0]), color=SECONDARY, fill_opacity=.5, stroke_width=0))
        self.add(Intersection(Circle(radius=2.5).shift(DL * 1.3), Polygon([4, -3.68, 0], [-4, -4, 0], [-3.68, 4, 0]), color=TERTIARY, fill_opacity=.5, stroke_width=0))
        self.add(Intersection(Circle(radius=2.5).shift(DR * 1.3), Polygon([-2, -4, 0], [4, -4, 0], [4, 2, 0]), color=QUATERNIARY, fill_opacity=.5, stroke_width=0))