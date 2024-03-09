# manim -qh Assumptions.py Image01 Image02 Image03 Image04 Image05 Image06

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

def linear(angle1, angle2):
    y1 = R * np.sin(angle1)
    y2 = R * np.sin(angle2)
    x1 = R * np.cos(angle1)
    x2 = R * np.cos(angle2)
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    return (a, b)

def intersection(a1, b1, a2, b2):
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return (x, y, 0)

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
        a1, b1 = linear(ANGLE1, ANGLE4)
        a2, b2 = linear(ANGLE3, ANGLE6)
        intersection_point = intersection(a1, b1, a2, b2)
        a = (intersection_point[1] - R * np.sin(ANGLE2)) / (intersection_point[0] - R * np.cos(ANGLE2))
        b = intersection_point[1] - a * intersection_point[0]
        x = (-a * b + np.sqrt(a * a * b * b - (a * a + 1) * (b * b - R * R))) / (a * a + 1)
        y = a * x + b

        self.camera.background_color = BACKGROUND
        circle = Circle(radius=R, color=PRIMARY)
        self.add(circle)
        points = [
            Dot(circle.point_at_angle(ANGLE1), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE2), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE3), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE4), color=PRIMARY),
            Dot((x, y, 0), color=PRIMARY),
            Dot(circle.point_at_angle(ANGLE6), color=PRIMARY)
        ]
        for i in range(len(points)):
            for j in range(i, len(points)):
                line = Line(points[i], points[j], color=PRIMARY)
                self.add(line)
            self.add(points[i])
        
        self.add(Circle(.25, color=TERTIARY, stroke_width=6).shift(intersection_point))
