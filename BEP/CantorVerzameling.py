from manim import *
from Helper import *

class Image01(Scene):
    def cantor(self, x, y, width):
        if width >= .001 and y > -4:
            self.add(Line((x, y, 0), (x + width, y, 0), color=BLACK, stroke_width=10))
            y -= 1
            self.cantor(x, y, width / 3)
            self.cantor(x + width * 2 / 3, y, width / 3)

    def construct(self):
        self.camera.background_color = WHITE
        self.cantor(-6, 3, 12)