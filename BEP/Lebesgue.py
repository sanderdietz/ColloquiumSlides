from manim import *
from Helper import *

set_frame_size()

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(6, color=BLACK, fill_opacity=.2))

        buffer = .15

        for i in range(3):
            for j in range(3):
                brick = RoundedRectangle(buffer, width=2+buffer, height=1+buffer, color=PRIMARY, fill_opacity=.5).shift((-2 + 2 * j, 2.5 - 2 * i, 0))
                self.add(brick)
        
        for i in range(3):
            for j in range(2):
                brick = RoundedRectangle(buffer, width=2+buffer, height=1+buffer, color=PRIMARY, fill_opacity=.5).shift((-1 + 2 * j, 1.5 - 2 * i, 0))
                self.add(brick)
        
        for i in range(3):
            for j in range(2):
                brick = RoundedRectangle(buffer, width=1+buffer, height=1+buffer, color=PRIMARY, fill_opacity=.5).shift((-2.5 + 5 * j, 1.5 - 2 * i, 0))
                self.add(brick)

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Line((-3, 0, 0), (3, 0, 0), color=BLACK))

        buffer = .15

        self.add(RoundedRectangle(buffer, width=2+buffer, height=2*buffer, color=PRIMARY, fill_opacity=.5).shift((-2, 0, 0)))
        self.add(RoundedRectangle(buffer, width=2+buffer, height=2*buffer, color=PRIMARY, fill_opacity=.5))
        self.add(RoundedRectangle(buffer, width=2+buffer, height=2*buffer, color=PRIMARY, fill_opacity=.5).shift((2, 0, 0)))

