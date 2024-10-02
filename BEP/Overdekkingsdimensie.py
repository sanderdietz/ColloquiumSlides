from manim import *
from Helper import *

set_frame_size()

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(color=BLACK, fill_opacity=.2).scale(3))
        self.add(Circle(color=PRIMARY, fill_opacity=.5, stroke_width=0).scale(3.225).shift(UL * .75))
        self.add(Ellipse(2.75, 7.0, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift(RIGHT * 2.5))
        self.add(Ellipse(5.5, 2.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift(UP * 2.5 + RIGHT))
        self.add(Circle(color=QUATERNIARY, fill_opacity=.5, stroke_width=0).scale(2).shift(DR * 1.5))
        self.add(Ellipse(5.5, 5, color=QUINARY, fill_opacity=.5, stroke_width=0).shift(DL + DOWN * .375))
        self.add(Ellipse(2, 4, color=SENARY, fill_opacity=.5, stroke_width=0).shift(UR + RIGHT))

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(color=BLACK, fill_opacity=.2).scale(3))
        self.add(Circle(color=PRIMARY, fill_opacity=.5, stroke_width=0).scale(3.225).shift(UL * .75))
        self.add(Ellipse(2.75, 7.0, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift(RIGHT * 2.5))
        self.add(Ellipse(5.5, 2.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift(UP * 2.5 + RIGHT))
        self.add(Circle(color=QUATERNIARY, fill_opacity=.5, stroke_width=0).scale(2).shift(DR * 1.5))
        self.add(Ellipse(5.5, 5, color=QUINARY, fill_opacity=.5, stroke_width=0).shift(DL + DOWN * .375))

class Image03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(color=BLACK, fill_opacity=.2).scale(3))
        self.add(Circle(color=PRIMARY, fill_opacity=.5, stroke_width=0).scale(3.225).shift(UL * .75))
        self.add(Ellipse(2.75, 7.0, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift(RIGHT * 2.5))
        self.add(Ellipse(5.5, 2.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift(UP * 2.5 + RIGHT))
        self.add(Circle(color=QUATERNIARY, fill_opacity=.5, stroke_width=0).scale(2).shift(DR * 1.5))
        self.add(Intersection(
            Ellipse(5.5, 5).shift(DL + DOWN * .375),
            Circle().scale(2.5).shift(DL * 1.5),
            color=QUINARY, fill_opacity=.5, stroke_width=0
        ))

class Image04(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(color=BLACK, fill_opacity=.2).scale(3))
        self.add(RoundedRectangle(.25, height=3.0, width=6.5, color=PRIMARY, fill_opacity=.5, stroke_width=0).shift(UP * 1.75))
        self.add(RoundedRectangle(.25, height=3.75, width=3.375, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift(DOWN * 1.375 + LEFT * 1.55))
        self.add(RoundedRectangle(.25, height=3.75, width=3.375, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift(DOWN * 1.375 + RIGHT * 1.55))
