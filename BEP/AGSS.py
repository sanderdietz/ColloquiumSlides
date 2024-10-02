from manim import *
from Helper import *
import random
from collections import deque

set_frame_size()

class BaseClass(Scene):
    def inCover(self, p, cover):
        for center_point in cover:
            if (center_point[0] - p[0]) * (center_point[0] - p[0]) + (center_point[1] - p[1]) * (center_point[1] - p[1]) < .5625:
                return True
        return False
    
    def isCover(self, cover):
        for i in range(0, 100):
            for j in range(0, 100):
                y = -3 + .06 * i
                x = -3 + .06 * j
                if not self.inCover((x, y), cover):
                    return False
        return True

class Image01(BaseClass):
    def construct(self):
        self.camera.background_color = WHITE
        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            full_cover.append((x, y))
            if self.isCover(full_cover):
                break

        subcover = deque(full_cover.copy())
        for _ in range(len(subcover)):
            center_point = subcover.pop()
            if not self.isCover(subcover):
                subcover.appendleft(center_point)
        subcover.append((-2.5, 0))
        for point in subcover:
            self.add(Circle(radius=.75, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0], point[1], 0)))

        self.add(Rectangle(width=6, height=6, color=BLACK))

class Image02(BaseClass):
    def construct(self):
        self.camera.background_color = WHITE
        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            full_cover.append((x, y))
            if self.isCover(full_cover):
                break

        subcover = deque(full_cover.copy())
        for _ in range(len(subcover)):
            center_point = subcover.pop()
            if not self.isCover(subcover):
                subcover.appendleft(center_point)
        subcover.append((-2.5, 0))
        for point in subcover:
            self.add(Circle(radius=.75, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0], point[1], 0)))
        
        self.add(Rectangle(width=3, height=2, color=SECONDARY, fill_opacity=.3).shift((1.6, 0, 0)))
        self.add(Rectangle(width=1.5, height=5, color=SECONDARY, fill_opacity=.3).shift((-.5, 0, 0)))
        self.add(Rectangle(width=4, height=.75, color=SECONDARY, fill_opacity=.3).shift((-1.6, -2.75, 0)))
        self.add(Rectangle(width=2, height=2.5, color=SECONDARY, fill_opacity=.3).shift((.8, -2.1, 0)))
        self.add(Rectangle(width=1.75, height=2.25, color=SECONDARY, fill_opacity=.3).shift((2.2, -2.1, 0)))
        self.add(Rectangle(width=6.5, height=.5, color=SECONDARY, fill_opacity=.3).shift((0, 1, 0)))
        self.add(Rectangle(width=2, height=3.5, color=SECONDARY, fill_opacity=.3).shift((-2.1, -.85, 0)))
        self.add(Rectangle(width=2, height=2, color=SECONDARY, fill_opacity=.3).shift((-2.2, 2.2, 0)))
        self.add(Rectangle(width=3.5, height=2, color=SECONDARY, fill_opacity=.3).shift((1.3, 2.1, 0)))
        self.add(Rectangle(width=1, height=.75, color=SECONDARY, fill_opacity=.3).shift((-.9, 2.8, 0)))

        self.add(Rectangle(width=6, height=6, color=BLACK))

class Image03(BaseClass):
    def construct(self):
        self.camera.background_color = WHITE
        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            full_cover.append((x, y))
            if self.isCover(full_cover):
                break

        subcover = deque(full_cover.copy())
        for _ in range(len(subcover)):
            center_point = subcover.pop()
            if not self.isCover(subcover):
                subcover.appendleft(center_point)
        subcover.append((-2.5, 0))
        for point in subcover:
            self.add(Circle(radius=.75, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0], point[1], 0)))
        
        self.add(Rectangle(width=3, height=2, color=SECONDARY, fill_opacity=.3).shift((1.6, 0, 0)))

        self.add(Rectangle(width=6, height=6, color=BLACK))

class Image04(BaseClass):
    def construct(self):
        self.camera.background_color = WHITE
        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            full_cover.append((x, y))
            if self.isCover(full_cover):
                break

        subcover = deque(full_cover.copy())
        for _ in range(len(subcover)):
            center_point = subcover.pop()
            if not self.isCover(subcover):
                subcover.appendleft(center_point)
        subcover.append((-2.5, 0))
        for point in subcover:
            if (point[0] - 2.5) ** 2 + point[1] ** 2 < .5:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] + .15, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            self.add(Circle(radius=.75, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0], point[1], 0)))

        self.add(Rectangle(width=3, height=2, color=SECONDARY, fill_opacity=.3).shift((1.6, 0, 0)))

        self.add(Rectangle(width=6, height=6, color=BLACK))

class Image05(BaseClass):
    def construct(self):
        self.camera.background_color = WHITE
        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            full_cover.append((x, y))
            if self.isCover(full_cover):
                break

        subcover = deque(full_cover.copy())
        for _ in range(len(subcover)):
            center_point = subcover.pop()
            if not self.isCover(subcover):
                subcover.appendleft(center_point)
        subcover.append((-2.5, 0))
        for point in subcover:
            if (point[0] - 2.5) ** 2 + point[1] ** 2 < .5:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] + .15, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] - .5) ** 2 + (point[1] + .2) ** 2 < .4:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] - .2, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            self.add(Circle(radius=.75, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0], point[1], 0)))

        self.add(Rectangle(width=3, height=2, color=SECONDARY, fill_opacity=.3).shift((1.6, 0, 0)))

        self.add(Rectangle(width=6, height=6, color=BLACK))

class Image06(BaseClass):
    def construct(self):
        self.camera.background_color = WHITE
        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            full_cover.append((x, y))
            if self.isCover(full_cover):
                break

        subcover = deque(full_cover.copy())
        for _ in range(len(subcover)):
            center_point = subcover.pop()
            if not self.isCover(subcover):
                subcover.appendleft(center_point)
        subcover.append((-2.5, 0))
        for point in subcover:
            if (point[0] - 2.5) ** 2 + point[1] ** 2 < .5:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] + .15, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] - .5) ** 2 + (point[1] + .2) ** 2 < .4:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] - .2, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            self.add(Circle(radius=.75, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0], point[1], 0)))

        self.add(Rectangle(width=2, height=3.5, color=SECONDARY, fill_opacity=.3).shift((-2.1, -.85, 0)))

        self.add(Rectangle(width=6, height=6, color=BLACK))

class Image07(BaseClass):
    def construct(self):
        self.camera.background_color = WHITE
        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            full_cover.append((x, y))
            if self.isCover(full_cover):
                break

        subcover = deque(full_cover.copy())
        for _ in range(len(subcover)):
            center_point = subcover.pop()
            if not self.isCover(subcover):
                subcover.appendleft(center_point)
        subcover.append((-2.5, 0))
        for point in subcover:
            if (point[0] - 2.5) ** 2 + point[1] ** 2 < .5:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] + .15, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] - .5) ** 2 + (point[1] + .2) ** 2 < .4:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] - .2, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] + 1.4) ** 2 + (point[1] - 1.5) ** 2 < .025:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] - .1, point[1] + .125, 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            self.add(Circle(radius=.75, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0], point[1], 0)))

        self.add(Rectangle(width=2, height=3.5, color=SECONDARY, fill_opacity=.3).shift((-2.1, -.85, 0)))

        self.add(Rectangle(width=6, height=6, color=BLACK))
            
class Image08(BaseClass):
    def construct(self):
        self.camera.background_color = WHITE
        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            full_cover.append((x, y))
            if self.isCover(full_cover):
                break

        subcover = deque(full_cover.copy())
        for _ in range(len(subcover)):
            center_point = subcover.pop()
            if not self.isCover(subcover):
                subcover.appendleft(center_point)
        subcover.append((-2.5, 0))
        for point in subcover:
            if (point[0] - 2.5) ** 2 + point[1] ** 2 < .5:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] + .15, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] - .5) ** 2 + (point[1] + .2) ** 2 < .4:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] - .2, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] + 1.4) ** 2 + (point[1] - 1.5) ** 2 < .025:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] - .1, point[1] + .125, 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] + 2.5) ** 2 + point[1] ** 2 < .025:
                self.add(Circle(radius=.1, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0] + .25, point[1] - .25, 0)))
                continue
            self.add(Circle(radius=.75, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0], point[1], 0)))

        self.add(Rectangle(width=2, height=3.5, color=SECONDARY, fill_opacity=.3).shift((-2.1, -.85, 0)))

        self.add(Rectangle(width=6, height=6, color=BLACK))

class Image09(BaseClass):
    def construct(self):
        self.camera.background_color = WHITE
        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            full_cover.append((x, y))
            if self.isCover(full_cover):
                break

        subcover = deque(full_cover.copy())
        for _ in range(len(subcover)):
            center_point = subcover.pop()
            if not self.isCover(subcover):
                subcover.appendleft(center_point)
        subcover.append((-2.5, 0))
        for point in subcover:
            if (point[0] - 2.5) ** 2 + point[1] ** 2 < .5:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] + .15, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] - .5) ** 2 + (point[1] + .2) ** 2 < .4:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] - .2, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] + 1.4) ** 2 + (point[1] - 1.5) ** 2 < .025:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] - .1, point[1] + .125, 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] + 2.5) ** 2 + point[1] ** 2 < .025:
                self.add(Circle(radius=.1, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0] + .25, point[1] - .25, 0)))
                continue
            if (point[0] + 2) ** 2 + (point[1] + 2) ** 2 < .4:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] - .125, point[1] + .125, 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            self.add(Circle(radius=.75, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0], point[1], 0)))

        self.add(Rectangle(width=2, height=3.5, color=SECONDARY, fill_opacity=.3).shift((-2.1, -.85, 0)))

        self.add(Rectangle(width=6, height=6, color=BLACK))

class Image10(BaseClass):
    def construct(self):
        self.camera.background_color = WHITE
        random.seed(0)
        full_cover = []
        while True:
            x = random.uniform(-3, 3)
            y = random.uniform(-3, 3)
            full_cover.append((x, y))
            if self.isCover(full_cover):
                break

        subcover = deque(full_cover.copy())
        for _ in range(len(subcover)):
            center_point = subcover.pop()
            if not self.isCover(subcover):
                subcover.appendleft(center_point)
        subcover.append((-2.5, 0))
        for point in subcover:
            if (point[0] - 2.5) ** 2 + point[1] ** 2 < .5:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] + .15, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] - .5) ** 2 + (point[1] + .2) ** 2 < .4:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] - .2, point[1], 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] + 1.4) ** 2 + (point[1] - 1.5) ** 2 < .025:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] - .1, point[1] + .125, 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            if (point[0] + 2.5) ** 2 + point[1] ** 2 < .025:
                self.add(Circle(radius=.1, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0] + .25, point[1] - .25, 0)))
                continue
            if (point[0] + 2) ** 2 + (point[1] + 2) ** 2 < .4:
                self.add(Intersection(
                    Circle(radius=.75).shift((point[0], point[1], 0)),
                    Circle(radius=.75).shift((point[0] - .125, point[1] + .125, 0)),
                    color=PRIMARY, fill_opacity=.25, stroke_width=0
                ))
                continue
            self.add(Circle(radius=.75, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0], point[1], 0)))

        self.add(Rectangle(width=3, height=2, color=SECONDARY, fill_opacity=.3).shift((1.6, 0, 0)))
        self.add(Rectangle(width=1.5, height=5, color=SECONDARY, fill_opacity=.3).shift((-.5, 0, 0)))
        self.add(Rectangle(width=4, height=.75, color=SECONDARY, fill_opacity=.3).shift((-1.6, -2.75, 0)))
        self.add(Rectangle(width=2, height=2.5, color=SECONDARY, fill_opacity=.3).shift((.8, -2.1, 0)))
        self.add(Rectangle(width=1.75, height=2.25, color=SECONDARY, fill_opacity=.3).shift((2.2, -2.1, 0)))
        self.add(Rectangle(width=6.5, height=.5, color=SECONDARY, fill_opacity=.3).shift((0, 1, 0)))
        self.add(Rectangle(width=2, height=3.5, color=SECONDARY, fill_opacity=.3).shift((-2.1, -.85, 0)))
        self.add(Rectangle(width=2, height=2, color=SECONDARY, fill_opacity=.3).shift((-2.2, 2.2, 0)))
        self.add(Rectangle(width=3.5, height=2, color=SECONDARY, fill_opacity=.3).shift((1.3, 2.1, 0)))
        self.add(Rectangle(width=1, height=.75, color=SECONDARY, fill_opacity=.3).shift((-.9, 2.8, 0)))

        self.add(Rectangle(width=6, height=6, color=BLACK))

# class Image07(BaseClass):
#     def construct(self):
#         self.camera.background_color = WHITE
#         random.seed(0)
#         full_cover = []
#         while True:
#             x = random.uniform(-3, 3)
#             y = random.uniform(-3, 3)
#             full_cover.append((x, y))
#             if self.isCover(full_cover):
#                 break

#         subcover = deque(full_cover.copy())
#         for _ in range(len(subcover)):
#             center_point = subcover.pop()
#             if not self.isCover(subcover):
#                 subcover.appendleft(center_point)
#         subcover.append((-2.5, 0))
#         for point in subcover:
#             if (point[0] - 2.5) ** 2 + point[1] ** 2 < .5:
#                 self.add(Intersection(
#                     Circle(radius=.75).shift((point[0], point[1], 0)),
#                     Circle(radius=.75).shift((point[0] + .15, point[1], 0)),
#                     color=PRIMARY, fill_opacity=.25, stroke_width=0
#                 ))
#                 continue
#             if (point[0] - .5) ** 2 + (point[1] + .2) ** 2 < .4:
#                 self.add(Intersection(
#                     Circle(radius=.75).shift((point[0], point[1], 0)),
#                     Circle(radius=.75).shift((point[0] - .2, point[1], 0)),
#                     color=PRIMARY, fill_opacity=.25, stroke_width=0
#                 ))
#                 continue
#             self.add(Circle(radius=.75, color=PRIMARY, fill_opacity=.25, stroke_width=0).shift((point[0], point[1], 0)))

#         self.add(Rectangle(width=3, height=2, color=SECONDARY, fill_opacity=.3).shift((1.6, 0, 0)))
#         self.add(Rectangle(width=1.5, height=5, color=SECONDARY, fill_opacity=.3).shift((-.5, 0, 0)))
#         self.add(Rectangle(width=4, height=.75, color=SECONDARY, fill_opacity=.3).shift((-1.6, -2.75, 0)))
#         self.add(Rectangle(width=2, height=2.5, color=SECONDARY, fill_opacity=.3).shift((.8, -2.1, 0)))
#         self.add(Rectangle(width=1.75, height=2.25, color=SECONDARY, fill_opacity=.3).shift((2.2, -2.1, 0)))
#         self.add(Rectangle(width=6.5, height=.5, color=SECONDARY, fill_opacity=.3).shift((0, 1, 0)))
#         self.add(Rectangle(width=2, height=3.5, color=SECONDARY, fill_opacity=.3).shift((-2.1, -.85, 0)))
#         self.add(Rectangle(width=2, height=2, color=SECONDARY, fill_opacity=.3).shift((-2.2, 2.2, 0)))
#         self.add(Rectangle(width=3.5, height=2, color=SECONDARY, fill_opacity=.3).shift((1.3, 2.1, 0)))
#         self.add(Rectangle(width=1, height=.75, color=SECONDARY, fill_opacity=.3).shift((-.9, 2.8, 0)))

#         self.add(Rectangle(width=6, height=6, color=BLACK))