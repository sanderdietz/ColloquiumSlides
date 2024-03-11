# manim -qh Intro.py Image01 Image02 Image03 Image04 Image05 Image06

from manim import *
import helper

config.frame_height = 8
config.frame_width = 8
config.frame_size = (1000, 1000)

BACKGROUND = "#ffffff"
PRIMARY = "#000000"
SECONDARY = "#00a6d6"
TERTIARY = "#e03c31"
QUATERNARY = "#6F1D77"

R = 3.5
ANGLE1 = .5 * PI
ANGLE2 = 1.1 * PI
ANGLE3 = -.2 * PI
ANGLE4 = -.6 * PI
ANGLE5 = .3 * PI
ANGLE6 = .8 * PI

class Image00(Scene):
    def construct(self):
        self.camera.background_color = SECONDARY
        circle = Circle(radius=R, color=PRIMARY)
        self.add(Circle(radius=R, color=WHITE, fill_opacity=1))
        self.add(circle)
        coords = [
            circle.point_at_angle(ANGLE1),
            circle.point_at_angle(ANGLE2),
            circle.point_at_angle(ANGLE3),
            circle.point_at_angle(ANGLE4),
            circle.point_at_angle(ANGLE5),
            circle.point_at_angle(ANGLE6)
        ]
        points = []
        for coord in coords:
            points.append(Dot(coord, color=PRIMARY))
        for i in range(len(points)):
            for j in range(i, len(points)):
                line = Line(points[i], points[j], color=PRIMARY)
                self.add(line)
            self.add(points[i])

class Image01(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        self.add(Circle(radius=R, color=QUATERNARY, fill_opacity=.8))
        circle = Circle(radius=R, color=SECONDARY, stroke_width=8)
        self.add(circle)
        coords = [
            circle.point_at_angle(ANGLE1),
            circle.point_at_angle(ANGLE2),
            circle.point_at_angle(ANGLE3),
            circle.point_at_angle(ANGLE4),
            circle.point_at_angle(ANGLE5),
            circle.point_at_angle(ANGLE6)
        ]
        points = []
        for coord in coords:
            points.append(Dot(coord, color=TERTIARY, radius=.1))
        for i in range(len(points)):
            for j in range(i, len(points)):
                line = Line(points[i], points[j], color=SECONDARY, stroke_width=8)
                self.add(line)
        
        for i1 in range(len(points)):
            for i2 in range(len(points)):
                for i3 in range(len(points)):
                    for i4 in range(len(points)):
                        x1, y1, _ = coords[i1]
                        x2, y2, _ = coords[i2]
                        x3, y3, _ = coords[i3]
                        x4, y4, _ = coords[i4]
                        a1, b1 = helper.linear_points(x1, y1, x2, y2)
                        a2, b2 = helper.linear_points(x3, y3, x4, y4)
                        self.add(Dot(helper.intersection(a1, b1, a2, b2), color=TERTIARY, radius=.1))
        
        for point in points:
            self.add(point)

class Image02(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=R, color=PRIMARY)
        self.add(circle)
        coords = [
            circle.point_at_angle(ANGLE1),
            circle.point_at_angle(ANGLE2),
            circle.point_at_angle(ANGLE3),
            circle.point_at_angle(ANGLE4),
            circle.point_at_angle(ANGLE5),
            circle.point_at_angle(ANGLE6)
        ]
        points = []
        for coord in coords:
            points.append(Dot(coord, color=SECONDARY, radius=.1))
        for i in range(len(points)):
            for j in range(i, len(points)):
                line = Line(points[i], points[j], color=PRIMARY)
                self.add(line)
        
        for i1 in range(len(points)):
            for i2 in range(len(points)):
                for i3 in range(len(points)):
                    for i4 in range(len(points)):
                        x1, y1, _ = coords[i1]
                        x2, y2, _ = coords[i2]
                        x3, y3, _ = coords[i3]
                        x4, y4, _ = coords[i4]
                        a1, b1 = helper.linear_points(x1, y1, x2, y2)
                        a2, b2 = helper.linear_points(x3, y3, x4, y4)
                        self.add(Dot(helper.intersection(a1, b1, a2, b2), color=TERTIARY, radius=.1))
        
        for point in points:
            self.add(point)

class Image03(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=R, color=GRAY, stroke_width=2)
        self.add(circle)
        coords = [
            circle.point_at_angle(ANGLE1),
            circle.point_at_angle(ANGLE2),
            circle.point_at_angle(ANGLE3),
            circle.point_at_angle(ANGLE4),
            circle.point_at_angle(ANGLE5),
            circle.point_at_angle(ANGLE6)
        ]
        points = []
        for coord in coords:
            points.append(Dot(coord, color=GRAY, radius=.05))
        for i in range(len(points)):
            for j in range(i, len(points)):
                line = Line(points[i], points[j], color=GRAY, stroke_width=2)
                self.add(line)
            self.add(points[i])

        for i1 in range(len(points)):
            for i2 in range(len(points)):
                for i3 in range(len(points)):
                    for i4 in range(len(points)):
                        x1, y1, _ = coords[i1]
                        x2, y2, _ = coords[i2]
                        x3, y3, _ = coords[i3]
                        x4, y4, _ = coords[i4]
                        a1, b1 = helper.linear_points(x1, y1, x2, y2)
                        a2, b2 = helper.linear_points(x3, y3, x4, y4)
                        if i1 == 0 and i2 == 3 and i3 == 1 and i4 == 4:
                            ip1 = helper.intersection(a1, b1, a2, b2)
                        if i1 == 2 and i2 == 5 and i3 == 1 and i4 == 4:
                            ip2 = helper.intersection(a1, b1, a2, b2)
                        if i1 == 3 and i2 == 4 and i3 == 2 and i4 == 5:
                            ip3 = helper.intersection(a1, b1, a2, b2)
                        if i1 == 1 and i2 == 2 and i3 == 0 and i4 == 3:
                            ip4 = helper.intersection(a1, b1, a2, b2)
                        if i1 == 0 and i2 == 3 and i3 == 2 and i4 == 5:
                            ip5 = helper.intersection(a1, b1, a2, b2)
                        self.add(Dot(helper.intersection(a1, b1, a2, b2), color=GRAY, radius=.05))
        self.add(Line(ip1, ip4, color=SECONDARY, stroke_width=8))
        self.add(Line(ip2, ip3, color=SECONDARY, stroke_width=8))
        self.add(Dot(ip5, color=TERTIARY, radius=.1))

class Image04(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=R, color=GRAY, stroke_width=2)
        self.add(circle)
        coords = [
            circle.point_at_angle(ANGLE1),
            circle.point_at_angle(ANGLE2),
            circle.point_at_angle(ANGLE3),
            circle.point_at_angle(ANGLE4),
            circle.point_at_angle(ANGLE5),
            circle.point_at_angle(ANGLE6)
        ]
        points = []
        for coord in coords:
            points.append(Dot(coord, color=GRAY, radius=.05))
        for i in range(len(points)):
            for j in range(i, len(points)):
                if i == 0 and j == 3:
                    line = Line(points[i], points[j], color=TERTIARY)
                else:
                    line = Line(points[i], points[j], color=GRAY, stroke_width=2)
                self.add(line)
            self.add(points[i])

        for i1 in range(len(points)):
            for i2 in range(len(points)):
                for i3 in range(len(points)):
                    for i4 in range(len(points)):
                        x1, y1, _ = coords[i1]
                        x2, y2, _ = coords[i2]
                        x3, y3, _ = coords[i3]
                        x4, y4, _ = coords[i4]
                        a1, b1 = helper.linear_points(x1, y1, x2, y2)
                        a2, b2 = helper.linear_points(x3, y3, x4, y4)
                        if i1 == 0 and i2 == 3 and i3 == 4 and i4 == 5:
                            ip1 = helper.intersection(a1, b1, a2, b2)
                        if i1 == 0 and i2 == 3 and i3 == 1 and i4 == 2:
                            ip2 = helper.intersection(a1, b1, a2, b2)
                        self.add(Dot(helper.intersection(a1, b1, a2, b2), color=GRAY, radius=.05))
        self.add(Line(coords[0], ip1, color=SECONDARY, stroke_width=8))
        self.add(Line(coords[3], ip2, color=SECONDARY, stroke_width=8))

class Image05(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=R, color=TERTIARY, stroke_width=8)
        self.add(circle)
        coords = [
            circle.point_at_angle(ANGLE1),
            circle.point_at_angle(ANGLE2),
            circle.point_at_angle(ANGLE3),
            circle.point_at_angle(ANGLE4),
            circle.point_at_angle(ANGLE5),
            circle.point_at_angle(ANGLE6)
        ]
        points = []
        for coord in coords:
            points.append(Dot(coord, color=GRAY, radius=.05))
        for i in range(len(points)):
            for j in range(i, len(points)):
                line = Line(points[i], points[j], color=SECONDARY, stroke_width=8)
                self.add(line)
            self.add(points[i])

        for i1 in range(len(points)):
            for i2 in range(len(points)):
                for i3 in range(len(points)):
                    for i4 in range(len(points)):
                        x1, y1, _ = coords[i1]
                        x2, y2, _ = coords[i2]
                        x3, y3, _ = coords[i3]
                        x4, y4, _ = coords[i4]
                        a1, b1 = helper.linear_points(x1, y1, x2, y2)
                        a2, b2 = helper.linear_points(x3, y3, x4, y4)
                        self.add(Circle(radius=.15, color=WHITE, fill_opacity=1).shift(helper.intersection(a1, b1, a2, b2)))

class Image06(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        circle = Circle(radius=R, color=SECONDARY, stroke_width=8)
        self.add(circle)
        coords = [
            circle.point_at_angle(ANGLE1),
            circle.point_at_angle(ANGLE2),
            circle.point_at_angle(ANGLE3),
            circle.point_at_angle(ANGLE4),
            circle.point_at_angle(ANGLE5),
            circle.point_at_angle(ANGLE6)
        ]
        points = []
        for coord in coords:
            points.append(Dot(coord, color=TERTIARY, radius=.1))
        for i in range(len(points)):
            for j in range(i, len(points)):
                line = Line(points[i], points[j], color=SECONDARY, stroke_width=8)
                self.add(line)
        
        for i1 in range(len(points)):
            for i2 in range(len(points)):
                for i3 in range(len(points)):
                    for i4 in range(len(points)):
                        x1, y1, _ = coords[i1]
                        x2, y2, _ = coords[i2]
                        x3, y3, _ = coords[i3]
                        x4, y4, _ = coords[i4]
                        a1, b1 = helper.linear_points(x1, y1, x2, y2)
                        a2, b2 = helper.linear_points(x3, y3, x4, y4)
                        self.add(Dot(helper.intersection(a1, b1, a2, b2), color=TERTIARY, radius=.1))
        
        for point in points:
            self.add(point)