from manim import *

PRIMARY = "#00a6d6"
SECONDARY = "#e03c31"

R = 3.5

ANGLE0 = .3 * PI
ANGLE1 = .5 * PI
ANGLE2 = .8 * PI
ANGLE3 = -.9 * PI
ANGLE4 = -.6 * PI
ANGLE5 = -.2 * PI

def set_frame_size():
    config.frame_height = 8
    config.frame_width = 8
    config.frame_size = (1000, 1000)

class MoserCircle(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.camera.background_color = WHITE
        self.circle = Circle(radius=R, color=GRAY, stroke_width=2)
        self.angles = [
            ANGLE0,
            ANGLE1,
            ANGLE2,
            ANGLE3,
            ANGLE4,
            ANGLE5
        ]
        self.points = [self.circle.point_at_angle(angle) for angle in self.angles]
        self.dots = [Dot(point, color=GRAY, radius=.05) for point in self.points]
        self.chords = self.calculate_chords()
    
    def get_alternate_point(self, intersection_point):
        a = (intersection_point[1] - R * np.sin(ANGLE3)) / (intersection_point[0] - R * np.cos(ANGLE3))
        b = intersection_point[1] - a * intersection_point[0]
        x = (-a * b + np.sqrt(a * a * b * b - (a * a + 1) * (b * b - R * R))) / (a * a + 1)
        y = a * x + b
        return (x, y, 0)

    def calculate_chords(self):
        chords = []
        for i, point_i in enumerate(self.points):
            for j, point_j in enumerate(self.points):
                if i < j:
                    chords.append(Line(point_i, point_j, color=GRAY, stroke_width=2))
        return chords

    def intersection(self, start1, end1, start2, end2):
        a1 = (end1[1] - start1[1]) / (end1[0] - start1[0])
        b1 = end1[1] - a1 * end1[0]
        a2 = (end2[1] - start2[1]) / (end2[0] - start2[0])
        b2 = end2[1] - a2 * end2[0]
        x = (b2 - b1) / (a1 - a2)
        y = a1 * x + b1
        return (x, y, 0)

    # def set_color(self, mobject, color):
    #     mobject.color = color
    
    # def set_stroke_width(self, mobject, stroke_width):
    #     mobject.stroke_width = stroke_width
    
    # def set_radius(self, mobject, radius):
    #     mobject.radius = radius
    # def draw_circle(self, color=GRAY, stroke_width=2)
    #     # circle = Circle(radius=R, color=color, stroke_width=stroke_width)
    #     self.add(circle)
    #     return circle