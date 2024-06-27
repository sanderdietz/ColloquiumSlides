from manim import *
from Helper import *
import random

set_frame_size()

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(RoundedRectangle(height=7.5, width=6.5, color=PRIMARY, fill_opacity=.2, stroke_width=0))
        self.add(Rectangle(height=5, width=4, color=SECONDARY, fill_opacity=.5))

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(RoundedRectangle(height=7.5, width=6.5, color=PRIMARY, fill_opacity=.2, stroke_width=0))
        self.add(Rectangle(height=5, width=4, color=SECONDARY, fill_opacity=.5))
        random.seed(2)
        for i in range(150):
            x = random.uniform(-2, 2)
            y = random.uniform(-2.5, 2.5)
            self.add(Circle(radius=.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift((x, y, 0)))
        x = -.6
        y = 1.1
        self.add(Circle(radius=.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift((x, y, 0)))
        x = 1.8
        y = -2.35
        self.add(Circle(radius=.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift((x, y, 0)))

class Image03(Scene):
    def inCover(self, p, cover):
        for center_point in cover:
            if (center_point[0] - p[0]) * (center_point[0] - p[0]) + (center_point[1] - p[1]) * (center_point[1] - p[1]) < .25:
                return True
        return False

    def construct(self):
        self.camera.background_color = WHITE
        self.add(RoundedRectangle(height=7.5, width=6.5, color=PRIMARY, fill_opacity=.2, stroke_width=0))
        self.add(Rectangle(height=5, width=4, color=SECONDARY, fill_opacity=.5))

        full_cover = [(-.6, 1.1), (1.8, -2.35)]

        random.seed(2)
        for i in range(150):
            x = random.uniform(-2, 2)
            y = random.uniform(-2.5, 2.5)
            full_cover.append((x, y))
        x = -.6
        y = 1.1
        self.add(Circle(radius=.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift((x, y, 0)))
        x = 1.8
        y = -2.35
        self.add(Circle(radius=.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift((x, y, 0)))

        countable_cover = [(-.6, 1.1), (1.8, -2.35)]

        for i in range(0, 100):
            for j in range(0, 80):
                y = -2.5 + .05 * i
                x = -2 + .05 * j
                if not self.inCover((x, y), countable_cover):
                    for center_point in full_cover:
                        if (x - center_point[0]) * (x - center_point[0]) + (y - center_point[1]) * (y - center_point[1]) < .15:
                            countable_cover.append(center_point)
                            break
                    else:
                        continue
        for point in countable_cover:
            self.add(Circle(radius=.5, color=TERTIARY, fill_opacity=.5, stroke_width=0).shift((point[0], point[1], 0)))
                