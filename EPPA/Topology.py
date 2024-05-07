from manim import *
from Helper import *

TWOSQRTTWO = 2 * np.sqrt(2)

set_frame_size()

class UnitInterval(Scene):
    def get_start(self, mobject):
        return Dot(mobject.start, radius=.1, color=BLACK)
    
    def get_end(self, mobject):
        return Dot(mobject.end, radius=.1, color=BLACK)

    def setup(self):
        self.camera.background_color = WHITE

class Image01(UnitInterval):
    def construct(self):
        self.setup()
        line = Line((-2, 0, 0), (2, 0, 0), stroke_width=10, stroke_color=BLACK)
        self.add(line, self.get_start(line), self.get_end(line))

class Image02(UnitInterval):
    def construct(self):
        self.setup()
        line = Line((-3.75, 0, 0), (3.75, 0, 0), stroke_width=10, stroke_color=BLACK)
        self.add(line, self.get_start(line), self.get_end(line))

class Image03(UnitInterval):
    def construct(self):
        self.setup()
        line = Line((-TWOSQRTTWO, TWOSQRTTWO, 0), (TWOSQRTTWO, -TWOSQRTTWO, 0), stroke_width=10, stroke_color=BLACK)
        self.add(line, self.get_start(line), self.get_end(line))

class Image04(UnitInterval):
    def construct(self):
        self.setup()
        arc = Arc(radius=TWOSQRTTWO, angle=.5 * PI, stroke_width=10, stroke_color=BLACK)
        line1 = arc.copy().shift(LEFT * TWOSQRTTWO)
        line2 = arc.rotate(PI).shift(DOWN * TWOSQRTTWO)
        dot1 = Dot((-TWOSQRTTWO, TWOSQRTTWO, 0), radius=.1, color=BLACK)
        dot2 = Dot((TWOSQRTTWO, -TWOSQRTTWO, 0), radius=.1, color=BLACK)
        self.add(line1, line2, dot1, dot2)

class Image05(UnitInterval):
    def construct(self):
        self.setup()
        line1 = Line((-TWOSQRTTWO, TWOSQRTTWO, 0), (.05, TWOSQRTTWO, 0), stroke_width=10, stroke_color=BLACK)
        line2 = Line((0, TWOSQRTTWO, 0), (0, -TWOSQRTTWO, 0), stroke_width=10, stroke_color=BLACK)
        line3 = Line((-.05, -TWOSQRTTWO, 0), (TWOSQRTTWO, -TWOSQRTTWO, 0), stroke_width=10, stroke_color=BLACK)
        self.add(line1, line2, line3, self.get_start(line1), self.get_end(line3))

class Image06(UnitInterval):
    def construct(self):
        self.setup()
        arc = Arc(radius=np.sqrt(2), angle=1.5*PI, stroke_width=10, stroke_color=BLACK).shift(UL * np.sqrt(2))
        line1 = Line((0, np.sqrt(2), 0), ORIGIN, stroke_width=10, stroke_color=BLACK)
        line2 = Line((-np.sqrt(2), 0, 0), (TWOSQRTTWO, 0, 0), stroke_width=10, stroke_color=BLACK)        
        self.add(line1, line2, arc, self.get_end(line1), self.get_end(line2))

class Image07(UnitInterval):
    def construct(self):
        self.setup()
        line1 = Line((-3, 0, 0), (-.25, 0, 0), stroke_width=10, stroke_color=BLACK)
        line2 = Line((.25, 0, 0), (3, 0, 0), stroke_width=10, stroke_color=BLACK)
        self.add(line1, line2, self.get_start(line1), self.get_end(line2))
