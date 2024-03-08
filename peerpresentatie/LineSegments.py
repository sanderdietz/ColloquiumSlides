# manim -qh LineSegments.py Slide01 Slide02 Slide03

from manim import *

BACKGROUND = "#ffffff"
PRIMARY = "#000000"
SECONDARY = "#ff0000"


ANGLE1 = .5 * PI
ANGLE2 = 1.1 * PI
ANGLE3 = -.2 * PI
ANGLE4 = -.6 * PI
ANGLE5 = .3 * PI
ANGLE6 = .8 * PI

class Slide01(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=3.0, color=PRIMARY).shift(RIGHT * 2)
        self.add(circle)
        points = [
            Dot(circle.point_at_angle(ANGLE1), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE2), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE3), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE4), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE5), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE6), color=PRIMARY)
        ]
        for i in range(len(points)):
            for j in range(i, len(points)):
                line = Line(points[i], points[j], color=PRIMARY)
                self.add(line)
            self.add(points[i])

class Slide02(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=3.0, color=GRAY, stroke_width=2).shift(RIGHT * 2)
        self.add(circle)
        points = [
            Dot(circle.point_at_angle(ANGLE1), color=SECONDARY, radius=.1),
            Dot(circle.point_at_angle(ANGLE2), color=GRAY, radius=.05),
            Dot(circle.point_at_angle(ANGLE3), color=GRAY, radius=.05),
            Dot(circle.point_at_angle(ANGLE4), color=SECONDARY, radius=.1),
            Dot(circle.point_at_angle(ANGLE5), color=GRAY, radius=.05),
            Dot(circle.point_at_angle(ANGLE6), color=GRAY, radius=.05)
        ]
        for i in range(len(points)):
            for j in range(i, len(points)):
                if i == 0 and j == 3:
                    pass
                else:
                    line = Line(points[i], points[j], color=GRAY, stroke_width=2)
                self.add(line)
            self.add(points[i])
        line = Line(points[0], points[3], color=SECONDARY, stroke_width=8)
        self.add(line)
        
class Slide03(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=3.0, color=GRAY, stroke_width=2).shift(RIGHT * 2)
        self.add(circle)
        points = [
            Dot(circle.point_at_angle(ANGLE1), color=GRAY, radius=.05),
            Dot(circle.point_at_angle(ANGLE2), color=GRAY, radius=.05),
            Dot(circle.point_at_angle(ANGLE3), color=SECONDARY, radius=.1),
            Dot(circle.point_at_angle(ANGLE4), color=GRAY, radius=.05),
            Dot(circle.point_at_angle(ANGLE5), color=GRAY, radius=.05),
            Dot(circle.point_at_angle(ANGLE6), color=SECONDARY, radius=.1)
        ]
        for i in range(len(points)):
            for j in range(i, len(points)):
                if i == 2 and j == 5:
                    pass
                else:
                    line = Line(points[i], points[j], color=GRAY, stroke_width=2)
                self.add(line)
            self.add(points[i])
        line = Line(points[2], points[5], color=SECONDARY, stroke_width=8)
        self.add(line)
        text = MathTex(r"\text{Kies }2\text{ van de }n\\\text{ punten: }{n\choose 2}", color=PRIMARY).shift(LEFT * 3.5)
        self.add(text)

class Slide04(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        