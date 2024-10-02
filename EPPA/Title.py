from manim import *
from Helper import *

set_frame_size()

class Image01(Scene):
    def construct(self):
        self.camera.background_color = PRIMARY
        self.add(Dot().shift(UL * 2))
        self.add(Line((-1, 0, 0), (1, 0, 0)).shift(UR * 2))
        self.add(Square().shift(DL * 2))
        
        square = Square()

        line1 = Line((-1, 1, 0), (1, 1, 0)).shift(UR * .25)
        line2 = Line((1, 1, 0), (1, -1, 0)).shift(UR * .25)
        line3 = DashedLine((-1, -1, 0), (-1, 1, 0)).shift(UR * .25)
        line4 = DashedLine((-1, -1, 0), (1, -1, 0)).shift(UR * .25)

        line5 = Line((-1, 1, 0), (-.75, 1.25, 0))
        line6 = Line((1, 1, 0), (1.25, 1.25, 0))
        line7 = Line((1, -1, 0), (1.25, -.75, 0))
        line8 = DashedLine((-1, -1, 0), (-.75, -.75, 0))
        
        self.add(VGroup(square, line1, line2, line3, line4, line5, line6, line7, line8).shift(DOWN * 2.125 + RIGHT * 1.875))
        