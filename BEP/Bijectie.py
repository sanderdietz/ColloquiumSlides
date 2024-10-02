from manim import *
from Helper import *

config.frame_height = 8
config.frame_width = 6
config.frame_size = (750, 1000)

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Dot((-2, 3, 0), color=PRIMARY))
        self.add(Dot((-2, 1, 0), color=PRIMARY))
        self.add(Dot((-2, -1, 0), color=PRIMARY))
        self.add(Dot((-2, -3, 0), color=PRIMARY))

        self.add(Dot((2, 3, 0), color=SECONDARY))
        self.add(Dot((2, 1, 0), color=SECONDARY))
        self.add(Dot((2, -1, 0), color=SECONDARY))
        self.add(Dot((2, -3, 0), color=SECONDARY))

        self.add(DoubleArrow((-2, 3, 0), (2, 3, 0), color=BLACK))
        self.add(DoubleArrow((-2, 1, 0), (2, 1, 0), color=BLACK))
        self.add(DoubleArrow((-2, -1, 0), (2, -1, 0), color=BLACK))
        self.add(DoubleArrow((-2, -3, 0), (2, -3, 0), color=BLACK))

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Dot((-2, 3, 0), color=PRIMARY))
        self.add(Dot((-2, 1, 0), color=PRIMARY))
        self.add(Dot((-2, -1, 0), color=PRIMARY))
        self.add(Dot((-2, -3, 0), color=PRIMARY))

        self.add(Dot((2, 3, 0), color=SECONDARY))
        self.add(Dot((2, 1.5, 0), color=SECONDARY))
        self.add(Dot((2, 0, 0), color=SECONDARY))
        self.add(Dot((2, -1.5, 0), color=SECONDARY))
        self.add(Dot((2, -3, 0), color=SECONDARY))

        self.add(Arrow((-2, 3, 0), (2, 3, 0), color=BLACK))
        self.add(Arrow((-2, 1, 0), (2, 1.5, 0), color=BLACK))
        self.add(Arrow((-2, -1, 0), (2, 0, 0), color=BLACK))
        self.add(Arrow((-2, -3, 0), (2, -1.5, 0), color=BLACK))

class Image03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Dot((-2, 3, 0), color=PRIMARY))
        self.add(Dot((-2, 1, 0), color=PRIMARY))
        self.add(Dot((-2, -1, 0), color=PRIMARY))
        self.add(Dot((-2, -3, 0), color=PRIMARY))

        self.add(Dot((2, 3, 0), color=SECONDARY))
        self.add(Dot((2, 0, 0), color=SECONDARY))
        self.add(Dot((2, -3, 0), color=SECONDARY))

        self.add(Arrow((-2, 3, 0), (2, 3, 0), color=BLACK))
        self.add(Arrow((-2, 1, 0), (2, 0, 0), color=BLACK))
        self.add(Arrow((-2, -1, 0), (2, -3, 0), color=BLACK))
        self.add(Arrow((-2, -3, 0), (2, -3, 0), color=BLACK))