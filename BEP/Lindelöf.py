from manim import *
from Helper import *
import random
from collections import deque

set_frame_size()

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(RoundedRectangle(height=7.5, width=6.5, color=PRIMARY, fill_opacity=.2, stroke_width=0))
        self.add(Rectangle(height=5, width=4, color=SECONDARY, fill_opacity=.5))

class Image02(Scene):
    def inCover(self, p, cover):
        for center_point in cover:
            if (center_point[0] - p[0]) * (center_point[0] - p[0]) + (center_point[1] - p[1]) * (center_point[1] - p[1]) < .2:
                return True
        return False
    
    def isCover(self, cover):
        for i in range(0, 100):
            for j in range(0, 80):
                y = -2.5 + .05 * i
                x = -2 + .05 * j
                if not self.inCover((x, y), cover):
                    return False
        return True
    
    def construct(self):
        self.camera.background_color = WHITE
        self.add(RoundedRectangle(height=7.5, width=6.5, color=PRIMARY, fill_opacity=.2, stroke_width=0))
        self.add(Rectangle(height=5, width=4, color=SECONDARY, fill_opacity=.5))
        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-2, 2)
            y = random.uniform(-2.5, 2.5)
            full_cover.append((x, y))
            self.add(Circle(radius=.5, color=TERTIARY, fill_opacity=.25, stroke_width=0).shift((x, y, 0)))
            if self.isCover(full_cover):
                break

class Image03(Scene):
    def inCover(self, p, cover):
        for center_point in cover:
            if (center_point[0] - p[0]) * (center_point[0] - p[0]) + (center_point[1] - p[1]) * (center_point[1] - p[1]) < .2:
                return True
        return False

    def isCover(self, cover):
        for i in range(0, 100):
            for j in range(0, 80):
                y = -2.5 + .05 * i
                x = -2 + .05 * j
                if not self.inCover((x, y), cover):
                    return False
        return True

    def construct(self):
        self.camera.background_color = WHITE
        self.add(RoundedRectangle(height=7.5, width=6.5, color=PRIMARY, fill_opacity=.2, stroke_width=0))
        self.add(Rectangle(height=5, width=4, color=SECONDARY, fill_opacity=.5))

        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-2, 2)
            y = random.uniform(-2.5, 2.5)
            full_cover.append((x, y))
            if self.isCover(full_cover):
                break

        countable_cover = deque(full_cover.copy())
        
        for _ in range(len(countable_cover)):
            center_point = countable_cover.pop()
            if not self.isCover(countable_cover):
                countable_cover.appendleft(center_point)

        for point in countable_cover:
            self.add(Circle(radius=.5, color=TERTIARY, fill_opacity=.35, stroke_width=0).shift((point[0], point[1], 0)))

class Image04(Scene):
    def inCover(self, p, cover):
        for center_point in cover:
            if (center_point[0] - p[0]) * (center_point[0] - p[0]) + (center_point[1] - p[1]) * (center_point[1] - p[1]) < .2:
                return True
        return False

    def isCover(self, cover):
        for i in range(0, 100):
            for j in range(0, 80):
                y = -2.5 + .05 * i
                x = -2 + .05 * j
                if not self.inCover((x, y), cover):
                    return False
        return True

    def construct(self):
        self.camera.background_color = WHITE
        self.add(RoundedRectangle(height=7.5, width=6.5, color=PRIMARY, fill_opacity=.2, stroke_width=0))
        self.add(Rectangle(height=5, width=4, color=SECONDARY, fill_opacity=.5))

        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-2, 2)
            y = random.uniform(-2.5, 2.5)
            full_cover.append((x, y))
            if self.isCover(full_cover):
                break

        countable_cover = deque(full_cover.copy())
        
        for _ in range(len(countable_cover)):
            center_point = countable_cover.pop()
            if not self.isCover(countable_cover):
                countable_cover.appendleft(center_point)

        interior = Circle(radius=.5).shift((countable_cover[0][0], countable_cover[0][1], 0))
        closure = Circle(radius=.525).shift((countable_cover[0][0], countable_cover[0][1], 0))
        for point in countable_cover:
            interior = Union(interior, Circle(radius=.5).shift((point[0], point[1], 0)))
            closure = Union(closure, Circle(radius=.525).shift((point[0], point[1], 0)))
            self.add(Circle(radius=.5, color=TERTIARY, fill_opacity=.35, stroke_width=0).shift((point[0], point[1], 0)))
        self.add(Difference(closure, interior, color=TERTIARY, fill_opacity=1))