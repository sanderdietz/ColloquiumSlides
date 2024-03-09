# manim -qh LineSegments.py Image01 Image02 Image03

from manim import *

config.frame_height = 8
config.frame_width = 8
config.frame_size = (1000, 1000)

BACKGROUND = "#ffffff"
PRIMARY = "#000000"
SECONDARY = "#00a6d6"
TERTIARY = "#e03c31"

R = 3.5
ANGLE1 = .5 * PI
ANGLE2 = 1.1 * PI
ANGLE3 = -.2 * PI
ANGLE4 = -.6 * PI
ANGLE5 = .3 * PI
ANGLE6 = .8 * PI

class Image01(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=R, color=PRIMARY)
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

class Image02(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=R, color=GRAY, stroke_width=2)
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
        
class Image03(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=R, color=GRAY, stroke_width=2)
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

class Image04(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        