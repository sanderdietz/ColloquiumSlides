# manim -qh Intro.py Image01 Image02 Image03 Image04 Image05 Image06

from manim import *
from MoserCircle import *

set_frame_size()

class Intro(MoserCircle):
    def image(self, chord_indices, dot_indices):
        self.circle.color = BLACK
        self.circle.stroke_width = 4
        self.add(self.circle)

        for i, chord in enumerate(self.chords):
            if i in chord_indices:
                chord.color = BLACK
                chord.stroke_width = 4
                self.add(chord)
        
        for i, dot in enumerate(self.dots):
            if i in dot_indices:
                dot._original__init__(self.points[i], color=BLACK)
                self.add(dot)

class Image01(Intro):
    def construct(self):
        self.image({}, {})

class Image02(Intro):
    def construct(self):
        self.image({6}, {1, 3})

class Image03(Intro):
    def construct(self):
        self.image({6, 8, 13}, {1, 3, 5})

class Image04(Intro):
    def construct(self):
        self.image({6, 7, 8, 12, 13, 14}, {1, 3, 4, 5})

class Image05(Intro):
    def construct(self):
        self.image({0, 2, 3, 4, 6, 7, 8, 12, 13, 14}, {0, 1, 3, 4, 5})

class Image06(Intro):
    def construct(self):
        self.image(range(15), range(6))

class Image07(MoserCircle):
    def construct(self):
        self.camera.background_color = PRIMARY
        self.circle.color = WHITE
        self.circle.stroke_width = 4
        self.add(self.circle)

        for i, chord in enumerate(self.chords):
            chord.color = WHITE
            chord.stroke_width = 4
            self.add(chord)
        
        for i, dot in enumerate(self.dots):
            dot._original__init__(self.points[i], color=WHITE)
            self.add(dot)
