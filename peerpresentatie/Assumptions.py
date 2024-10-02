# manim -qh Assumptions.py Image01 Image02

from manim import *
from MoserCircle import *

set_frame_size()

class Image01(MoserCircle):
    def construct(self):
        self.circle.color = BLACK
        self.circle.stroke_width = 4
        self.add(self.circle)

        for chord in self.chords:
            chord.color = BLACK
            chord.stroke_width = 4
            self.add(chord)
        
        for i, dot in enumerate(self.dots):
            dot._original__init__(self.points[i], color=BLACK)
            self.add(dot)

class Image02(MoserCircle):
    def construct(self):
        self.circle.color = BLACK
        self.circle.stroke_width = 4
        self.add(self.circle)

        intersection_point = self.intersection(self.points[1], self.points[4], self.points[2], self.points[5])
        alternate_point = self.get_alternate_point(intersection_point)
        self.points[0] = alternate_point
        self.dots[0] = Dot(alternate_point, color=GRAY, radius=.05)
        self.chords = self.calculate_chords()

        for chord in self.chords:
            chord.color = BLACK
            chord.stroke_width = 4
            self.add(chord)
        
        for i, dot in enumerate(self.dots):
            dot._original__init__(self.points[i], color=BLACK)
            self.add(dot)
        
        self.add(Circle(.25, color=SECONDARY, stroke_width=6).shift(intersection_point))
