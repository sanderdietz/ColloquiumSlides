from manim import *
from Helper import *

set_frame_size()

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        self.add(Rectangle(width=3, height=2, color=PRIMARY, fill_opacity=.5))
        self.add(Rectangle(width=3.5, height=2.5, color=PRIMARY, fill_opacity=.5).shift((1.2, 1.5, 0)))
        self.add(Rectangle(width=2, height=2.5, color=PRIMARY, fill_opacity=.5).shift((-1, 1.25, 0)))
        self.add(Rectangle(width=2.2, height=3, color=PRIMARY, fill_opacity=.5).shift((-2, -1, 0)))
        self.add(Rectangle(width=1.5, height=3, color=PRIMARY, fill_opacity=.5).shift((1.8, -.7, 0)))
        self.add(Rectangle(width=2.8, height=1.2, color=PRIMARY, fill_opacity=.5).shift((-.2, -1.4, 0)))


class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        self.add(Rectangle(width=3, height=2, color=PRIMARY, fill_opacity=0, stroke_width=2))
        self.add(Rectangle(width=3.5, height=2.5, color=PRIMARY, fill_opacity=0, stroke_width=2).shift((1.2, 1.5, 0)))
        self.add(Rectangle(width=2, height=2.5, color=PRIMARY, fill_opacity=0, stroke_width=2).shift((-1, 1.25, 0)))
        self.add(Rectangle(width=2.2, height=3, color=PRIMARY, fill_opacity=0, stroke_width=2).shift((-2, -1, 0)))
        self.add(Rectangle(width=1.5, height=3, color=PRIMARY, fill_opacity=0, stroke_width=2).shift((1.8, -.7, 0)))
        self.add(Rectangle(width=2.8, height=1.2, color=PRIMARY, fill_opacity=0, stroke_width=2).shift((-.2, -1.4, 0)))

        buffer = .125

        self.add(RoundedRectangle(buffer, width=3+2*buffer, height=2+2*buffer, color=SECONDARY, fill_opacity=.5, stroke_width=0))
        self.add(RoundedRectangle(buffer, width=3.5+2*buffer, height=2.5+2*buffer, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift((1.2, 1.5, 0)))
        self.add(RoundedRectangle(buffer, width=2+2*buffer, height=2.5+2*buffer, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift((-1, 1.25, 0)))
        self.add(RoundedRectangle(buffer, width=2.2+2*buffer, height=3+2*buffer, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift((-2, -1, 0)))
        self.add(RoundedRectangle(buffer, width=1.5+2*buffer, height=3+2*buffer, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift((1.8, -.7, 0)))
        self.add(RoundedRectangle(buffer, width=2.8+2*buffer, height=1.2+2*buffer, color=SECONDARY, fill_opacity=.5, stroke_width=0).shift((-.2, -1.4, 0)))

class Image03(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        buffer = .125

        self.add(RoundedRectangle(buffer, width=3+2*buffer, height=2+2*buffer, color=SECONDARY, fill_opacity=.2, stroke_width=0))
        self.add(RoundedRectangle(buffer, width=3.5+2*buffer, height=2.5+2*buffer, color=SECONDARY, fill_opacity=.2, stroke_width=0).shift((1.2, 1.5, 0)))
        self.add(RoundedRectangle(buffer, width=2+2*buffer, height=2.5+2*buffer, color=SECONDARY, fill_opacity=.2, stroke_width=0).shift((-1, 1.25, 0)))
        self.add(RoundedRectangle(buffer, width=2.2+2*buffer, height=3+2*buffer, color=SECONDARY, fill_opacity=.2, stroke_width=0).shift((-2, -1, 0)))
        self.add(RoundedRectangle(buffer, width=1.5+2*buffer, height=3+2*buffer, color=SECONDARY, fill_opacity=.2, stroke_width=0).shift((1.8, -.7, 0)))
        self.add(RoundedRectangle(buffer, width=2.8+2*buffer, height=1.2+2*buffer, color=SECONDARY, fill_opacity=.2, stroke_width=0).shift((-.2, -1.4, 0)))

        buffer = .05
        self.add(Rectangle(width=3+2*buffer, height=2+2*buffer, color=TERTIARY, fill_opacity=.25))
        self.add(Rectangle(width=3.5+2*buffer, height=2.5+2*buffer, color=TERTIARY, fill_opacity=.25).shift((1.2, 1.5, 0)))
        self.add(Rectangle(width=2+2*buffer, height=2.5+2*buffer, color=TERTIARY, fill_opacity=.25).shift((-1, 1.25, 0)))
        self.add(Rectangle(width=2.2+2*buffer, height=3+2*buffer, color=TERTIARY, fill_opacity=.25).shift((-2, -1, 0)))
        self.add(Rectangle(width=1.5+2*buffer, height=3+2*buffer, color=TERTIARY, fill_opacity=.25).shift((1.8, -.7, 0)))
        self.add(Rectangle(width=2.8+2*buffer, height=1.2+2*buffer, color=TERTIARY, fill_opacity=.25).shift((-.2, -1.4, 0)))
