# manim -qh Intro.py Slide01 Slide02 Slide03 Slide04 Slide05 Slide06

from manim import *

BACKGROUND = "#ffffff"
PRIMARY = "#000000"
SECONDARY = "#f0a563"

ANGLE1 = .5 * PI
ANGLE2 = 1.1 * PI
ANGLE3 = -.2 * PI
ANGLE4 = -.6 * PI
ANGLE5 = .3 * PI
ANGLE6 = .8 * PI

class Slide01(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=3.0, color=PRIMARY).shift(LEFT * 2)
        self.add(circle)
        self.add(MathTex(r"1", color=PRIMARY).scale(2).shift(RIGHT * 3.5))

class Slide02(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=3.0, color=PRIMARY).shift(LEFT * 2)
        self.add(circle)
        points = [
            Dot(circle.point_at_angle(ANGLE1), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE2), color=PRIMARY)
        ]
        for i in range(len(points)):
            for j in range(i, len(points)):
                line = Line(points[i], points[j], color=PRIMARY)
                self.add(line)
            self.add(points[i])
        self.add(MathTex(r"2", color=PRIMARY).scale(2).shift(RIGHT * 3.5))

class Slide03(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=3.0, color=PRIMARY).shift(LEFT * 2)
        self.add(circle)
        points = [
            Dot(circle.point_at_angle(ANGLE1), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE2), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE3), color=PRIMARY)
        ]
        for i in range(len(points)):
            for j in range(i, len(points)):
                line = Line(points[i], points[j], color=PRIMARY)
                self.add(line)
            self.add(points[i])
        self.add(MathTex(r"4", color=PRIMARY).scale(2).shift(RIGHT * 3.5))

class Slide04(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=3.0, color=PRIMARY).shift(LEFT * 2)
        self.add(circle)
        points = [
            Dot(circle.point_at_angle(ANGLE1), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE2), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE3), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE4), color=PRIMARY)
        ]
        for i in range(len(points)):
            for j in range(i, len(points)):
                line = Line(points[i], points[j], color=PRIMARY)
                self.add(line)
            self.add(points[i])
        self.add(MathTex(r"8", color=PRIMARY).scale(2).shift(RIGHT * 3.5))

class Slide05(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=3.0, color=PRIMARY).shift(LEFT * 2)
        self.add(circle)
        points = [
            Dot(circle.point_at_angle(ANGLE1), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE2), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE3), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE4), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE5), color=PRIMARY)
        ]
        for i in range(len(points)):
            for j in range(i, len(points)):
                line = Line(points[i], points[j], color=PRIMARY)
                self.add(line)
            self.add(points[i])
        self.add(MathTex(r"16", color=PRIMARY).scale(2).shift(RIGHT * 3.5))
        
class Slide06(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=3.0, color=PRIMARY).shift(LEFT * 2)
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
        self.add(MathTex(r"31", color=PRIMARY).scale(2).shift(RIGHT * 3.5))
