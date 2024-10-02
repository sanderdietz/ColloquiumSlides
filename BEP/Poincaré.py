from manim import *
from Helper import *

set_frame_size()

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Line((-3, 0, 0), (3, 0, 0), color=BLACK))

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Line((-3, 0, 0), (3, 0, 0), color=BLACK))
        self.add(Dot((0, 0, 0), color=SECONDARY))

class Image03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(6, color=BLACK, fill_opacity=.2))

class Image04(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(6, color=BLACK, fill_opacity=.2))
        self.add(Dot((0, 0, 0), color=SECONDARY))

class Image05(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(6, color=BLACK, fill_opacity=.2))
        self.add(Line((0, 3, 0), (0, -3, 0), color=SECONDARY))

class Image06(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        cube = Cube(fill_opacity=0.1, stroke_width=1)
        cube.color = BLACK
        self.add(cube)
        self.set_camera_orientation(phi=.35*PI, theta=.35*PI, zoom=2)

class Image07(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        cube = Cube(fill_opacity=0.1, stroke_width=1)
        cube.color = BLACK
        self.add(cube)
        surface = Surface(
            lambda u, v: (0, u, v),
            u_range=[-1, 1],
            v_range=[-1, 1],
            fill_opacity=.6,
            stroke_width=0
        )
        surface.color = SECONDARY
        self.add(surface)
        self.set_camera_orientation(phi=.35*PI, theta=.35*PI, zoom=2)

class Image08(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Line((-3.25, 0, 0), (-.25, 0, 0), color=BLACK))
        self.add(Line((.25, 0, 0), (3.25, 0, 0), color=BLACK))

class Image09(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # self.add(Square(6, color=BLACK, fill_opacity=.2))
        self.add(Rectangle(width=3, height=6, fill_opacity=.2, color=BLACK).shift(LEFT * 1.75))
        self.add(Rectangle(width=3, height=6, fill_opacity=.2, color=BLACK).shift(RIGHT * 1.75))
        self.add(Rectangle(width=.5, height=6, color=WHITE, fill_opacity=1))

class Image10(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        left = Prism(dimensions = (1, 2, 2), fill_opacity=.1, stroke_width=1).shift(LEFT * 1.1)
        left.color = BLACK
        self.add(left)

        right = Prism(dimensions = (1, 2, 2), fill_opacity=.1, stroke_width=1).shift(RIGHT * 1.1)
        right.color = BLACK
        self.add(right)

        # middle = Prism(dimensions = (1.2, 2, 2), fill_opacity=0, stroke_width=1)
        # middle.color = WHITE
        # self.add(middle)

        # cube = Cube(fill_opacity=0.1, stroke_width=1)
        # cube.color = BLACK
        # self.add(cube)
        
        self.set_camera_orientation(phi=.35*PI, theta=.35*PI, zoom=2)