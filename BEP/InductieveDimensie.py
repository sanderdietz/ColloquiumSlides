from manim import *
from Helper import *

set_frame_size()

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(color=BLACK, fill_opacity=.2).scale(3.5))
        self.add(Ellipse(width=5.25, height=3.75, color=PRIMARY, stroke_width=0, fill_opacity=.5).shift(UP * 1.25))
        self.add(Dot(UL * 1.25, radius=.15, color=SECONDARY))

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(color=BLACK, fill_opacity=.2).scale(3.5))
        self.add(Ellipse(width=5.25, height=3.75, color=PRIMARY, stroke_width=0, fill_opacity=.5).shift(UP * 1.25))
        self.add(Circle(radius=1.2, color=TERTIARY, stroke_width=10, fill_opacity=.5).shift(UL * 1.25))
        self.add(Dot(UL * 1.25, radius=.15, color=SECONDARY))

class Image03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Circle(radius=3.5, color=BLACK))
        self.add(Arc(radius=3.5, start_angle=PI/6, color=PRIMARY, stroke_width=35, stroke_opacity=.5))
        self.add(Dot(UP * 3.5 * np.sin(PI / 3) + RIGHT * 3.5 * np.cos(PI / 3), radius=.15, color=SECONDARY))

class Image04(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Circle(radius=3.5, color=BLACK))
        self.add(Arc(radius=3.5, start_angle=PI/6, color=PRIMARY, stroke_width=35, stroke_opacity=.5))
        self.add(Arc(radius=3.5, start_angle=PI/3-.3, angle=.6, color=TERTIARY, stroke_width=35, stroke_opacity=.5))
        self.add(Dot(UP * 3.5 * np.sin(PI / 3) + RIGHT * 3.5 * np.cos(PI / 3), radius=.15, color=SECONDARY))
        self.add(Dot(UP * 3.5 * np.sin(PI / 3 - .3) + RIGHT * 3.5 * np.cos(PI / 3 - .3), radius=.225, color=TERTIARY))
        self.add(Dot(UP * 3.5 * np.sin(PI / 3 + .3) + RIGHT * 3.5 * np.cos(PI / 3 + .3), radius=.225, color=TERTIARY))