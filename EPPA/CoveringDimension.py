from manim import *
from Helper import *

set_frame_size()

class CoveringDimension(Scene):
    def setup(self):
        self.camera.background_color = WHITE
        self.add(Line(UL * 2 * np.sqrt(2), DR * 2 * np.sqrt(2), stroke_color=BLACK))
        self.add(Line(UR * 2 * np.sqrt(2), DL * 2 * np.sqrt(2), stroke_color=BLACK))
        
class Image01(CoveringDimension):
    def construct(self):
        self.setup()

class Image02(CoveringDimension):
    def construct(self):
        self.setup()
        interval1 = RoundedRectangle(corner_radius=.1, height=.2, width=5).shift(RIGHT * 1.5).rotate(.25 * PI, about_point=ORIGIN)
        interval2 = RoundedRectangle(corner_radius=.1, height=.2, width=3).shift(RIGHT * 1).rotate(.75 * PI, about_point=ORIGIN)
        self.add(Union(interval1, interval2, stroke_width=0, color=PRIMARY, fill_opacity=.5))

class Image03(CoveringDimension):
    def construct(self):
        self.setup()
        interval1 = RoundedRectangle(corner_radius=.1, height=.2, width=5).shift(RIGHT * 1.5).rotate(.25 * PI, about_point=ORIGIN)
        interval2 = RoundedRectangle(corner_radius=.1, height=.2, width=3).shift(RIGHT * 1).rotate(.75 * PI, about_point=ORIGIN)
        self.add(Union(interval1, interval2, stroke_width=0, color=PRIMARY, fill_opacity=.5))
        self.add(RoundedRectangle(corner_radius=.1, height=.2, width=5.5, stroke_width=0, color=SECONDARY, fill_opacity=.5).shift(RIGHT * 1.25).rotate(-.25 * PI, about_point=ORIGIN))

class Image04(CoveringDimension):
    def construct(self):
        self.setup()
        interval1 = RoundedRectangle(corner_radius=.1, height=.2, width=5).shift(RIGHT * 1.5).rotate(.25 * PI, about_point=ORIGIN)
        interval2 = RoundedRectangle(corner_radius=.1, height=.2, width=3).shift(RIGHT * 1).rotate(.75 * PI, about_point=ORIGIN)
        self.add(Union(interval1, interval2, stroke_width=0, color=PRIMARY, fill_opacity=.5))
        self.add(RoundedRectangle(corner_radius=.1, height=.2, width=5.5, stroke_width=0, color=SECONDARY, fill_opacity=.5).shift(RIGHT * 1.25).rotate(-.25 * PI, about_point=ORIGIN))
        self.add(RoundedRectangle(corner_radius=.1, height=.2, width=6, stroke_width=0, color=TERTIARY, fill_opacity=.5).shift(RIGHT * 1).rotate(-.75 * PI, about_point=ORIGIN))

class Image05(CoveringDimension):
    def construct(self):
        self.setup()
        interval1 = RoundedRectangle(corner_radius=.1, height=.2, width=5).shift(RIGHT * 1.5).rotate(.25 * PI, about_point=ORIGIN)
        interval2 = RoundedRectangle(corner_radius=.1, height=.2, width=3).shift(RIGHT * 1).rotate(.75 * PI, about_point=ORIGIN)
        self.add(Union(interval1, interval2, stroke_width=0, color=PRIMARY, fill_opacity=.5))
        self.add(RoundedRectangle(corner_radius=.1, height=.2, width=5.5, stroke_width=0, color=SECONDARY, fill_opacity=.5).shift(RIGHT * 1.25).rotate(-.25 * PI, about_point=ORIGIN))
        self.add(RoundedRectangle(corner_radius=.1, height=.2, width=6, stroke_width=0, color=TERTIARY, fill_opacity=.5).shift(RIGHT * 1).rotate(-.75 * PI, about_point=ORIGIN))
        self.add(RoundedRectangle(corner_radius=.1, height=.2, width=2, stroke_width=0, color=QUATERNIARY, fill_opacity=.5).shift(RIGHT * 3).rotate(.75 * PI, about_point=ORIGIN))

class Image06(CoveringDimension):
    def construct(self):
        self.setup()
        interval1 = RoundedRectangle(corner_radius=.1, height=.2, width=5).shift(RIGHT * 1.5).rotate(.25 * PI, about_point=ORIGIN)
        interval2 = RoundedRectangle(corner_radius=.1, height=.2, width=3).shift(RIGHT * 1).rotate(.75 * PI, about_point=ORIGIN)
        self.add(Union(interval1, interval2, stroke_width=0, color=PRIMARY, fill_opacity=.5))
        self.add(RoundedRectangle(corner_radius=.1, height=.2, width=3.7, stroke_width=0, color=SECONDARY, fill_opacity=.5).shift(RIGHT * 2.15).rotate(-.25 * PI, about_point=ORIGIN))
        self.add(RoundedRectangle(corner_radius=.1, height=.2, width=3.2, stroke_width=0, color=TERTIARY, fill_opacity=.5).shift(RIGHT * 2.4).rotate(-.75 * PI, about_point=ORIGIN))
        self.add(RoundedRectangle(corner_radius=.1, height=.2, width=1.7, stroke_width=0, color=QUATERNIARY, fill_opacity=.5).shift(RIGHT * 3.15).rotate(.75 * PI, about_point=ORIGIN))

class Image07(CoveringDimension):
    def construct(self):
        self.setup()
        interval1 = RoundedRectangle(corner_radius=.1, height=.2, width=8).rotate(.25 * PI, about_point=ORIGIN)
        interval2 = RoundedRectangle(corner_radius=.1, height=.2, width=7).shift(RIGHT * .5).rotate(-.25 * PI, about_point=ORIGIN)
        self.add(Union(interval1, interval2, stroke_width=0, color=PRIMARY, fill_opacity=.5))
        self.add(RoundedRectangle(corner_radius=.1, height=.2, width=3, stroke_width=0, color=SECONDARY, fill_opacity=.5).shift(RIGHT * 2.5).rotate(.75 * PI, about_point=ORIGIN))

class Image08(CoveringDimension):
    def construct(self):
        self.setup()
        interval1 = RoundedRectangle(corner_radius=.1, height=.2, width=8).rotate(.25 * PI, about_point=ORIGIN)
        interval2 = RoundedRectangle(corner_radius=.1, height=.2, width=7).shift(RIGHT * .5).rotate(-.25 * PI, about_point=ORIGIN)
        self.add(Union(interval1, interval2, stroke_width=0, color=PRIMARY, fill_opacity=.5))
        self.add(RoundedRectangle(corner_radius=.1, height=.2, width=1.2, stroke_width=0, color=SECONDARY, fill_opacity=.5).shift(RIGHT * 3.4).rotate(.75 * PI, about_point=ORIGIN))

# class CoveringDimension(Scene):
#     def setup(self):
#         self.camera.background_color = WHITE
#         self.add(Square(6, stroke_color=BLACK))
        
# class Image01(CoveringDimension):
#     def construct(self):
#         self.setup()

# class Image02(CoveringDimension):
#     def construct(self):
#         self.setup()
#         self.add(Circle(radius=2.5, color=PRIMARY, fill_opacity=.5, stroke_width=0).shift(UL * 1.3))
#         self.add(Circle(radius=2.5, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift(UR * 1.3))
#         self.add(Circle(radius=2.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift(DL * 1.3))
#         self.add(Circle(radius=2.5, color=QUATERNIARY, fill_opacity=.5, stroke_width=0).shift(DR * 1.3))

# class Image03(CoveringDimension):
#     def construct(self):
#         self.setup()
#         self.add(Intersection(Circle(radius=2.5).shift(UL * 1.3), Polygon([-4, -2, 0], [-4, 4, 0], [2, 4, 0]), color=PRIMARY, fill_opacity=.5, stroke_width=0))
#         self.add(Circle(radius=2.5, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift(UR * 1.3))
#         self.add(Circle(radius=2.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift(DL * 1.3))
#         self.add(Circle(radius=2.5, color=QUATERNIARY, fill_opacity=.5, stroke_width=0).shift(DR * 1.3))

# class Image04(CoveringDimension):
#     def construct(self):
#         self.setup()
#         self.add(Intersection(Circle(radius=2.5).shift(UL * 1.3), Polygon([-4, -2, 0], [-4, 4, 0], [2, 4, 0]), color=PRIMARY, fill_opacity=.5, stroke_width=0))
#         self.add(Circle(radius=2.5, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift(UR * 1.3))
#         self.add(Circle(radius=2.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift(DL * 1.3))
#         self.add(Intersection(Circle(radius=2.5).shift(DR * 1.3), Polygon([-2, -4, 0], [4, -4, 0], [4, 2, 0]), color=QUATERNIARY, fill_opacity=.5, stroke_width=0))

# class Image05(CoveringDimension):
#     def construct(self):
#         self.setup()
#         self.add(Intersection(Circle(radius=2.5).shift(UL * 1.3), Polygon([-4, -2, 0], [-4, 4, 0], [2, 4, 0]), color=PRIMARY, fill_opacity=.5, stroke_width=0))
#         self.add(Intersection(Circle(radius=2.5).shift(UR * 1.3), Polygon([-4, 3.68, 0], [4, 4, 0], [3.68, -4, 0]), color=SECONDARY, fill_opacity=.5, stroke_width=0))
#         self.add(Circle(radius=2.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift(DL * 1.3))
#         self.add(Intersection(Circle(radius=2.5).shift(DR * 1.3), Polygon([-2, -4, 0], [4, -4, 0], [4, 2, 0]), color=QUATERNIARY, fill_opacity=.5, stroke_width=0))

# class Image06(CoveringDimension):
#     def construct(self):
#         self.setup()
#         self.add(Intersection(Circle(radius=2.5).shift(UL * 1.3), Polygon([-4, -2, 0], [-4, 4, 0], [2, 4, 0]), color=PRIMARY, fill_opacity=.5, stroke_width=0))
#         self.add(Intersection(Circle(radius=2.5).shift(UR * 1.3), Polygon([-4, 3.68, 0], [4, 4, 0], [3.68, -4, 0]), color=SECONDARY, fill_opacity=.5, stroke_width=0))
#         self.add(Intersection(Circle(radius=2.5).shift(DL * 1.3), Polygon([4, -3.68, 0], [-4, -4, 0], [-3.68, 4, 0]), color=TERTIARY, fill_opacity=.5, stroke_width=0))
#         self.add(Intersection(Circle(radius=2.5).shift(DR * 1.3), Polygon([-2, -4, 0], [4, -4, 0], [4, 2, 0]), color=QUATERNIARY, fill_opacity=.5, stroke_width=0))