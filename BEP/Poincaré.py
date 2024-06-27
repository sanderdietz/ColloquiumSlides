from manim import *
from Helper import *

set_frame_size()

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Line((-3, 0, 0), (3, 0, 0), color=BLACK))
        self.add(Dot((-1.5, 0, 0), color=PRIMARY))
        self.add(Dot((1.5, 0, 0), color=PRIMARY))

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Line((-3, 0, 0), (3, 0, 0), color=BLACK))
        self.add(Dot((-1.5, 0, 0), color=PRIMARY))
        self.add(Dot((1.5, 0, 0), color=PRIMARY))
        self.add(Dot((0, 0, 0), color=SECONDARY))

class Image03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(6, color=BLACK, fill_opacity=.2))
        self.add(Dot((-1.5, 1, 0), color=PRIMARY))
        self.add(Dot((.5, 2, 0), color=PRIMARY))

class Image04(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(6, color=BLACK, fill_opacity=.2))
        self.add(Dot((-1.5, 1, 0), color=PRIMARY))
        self.add(Dot((.5, 2, 0), color=PRIMARY))
        self.add(Dot((-.5, 1.5, 0), color=SECONDARY))

class Image05(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.add(Square(6, color=BLACK, fill_opacity=.2))
        self.add(Dot((-1.5, 1, 0), color=PRIMARY))
        self.add(Dot((.5, 2, 0), color=PRIMARY))
        self.add(Line((-.5, 3, 0), (-.5, -3, 0), color=SECONDARY))

class Image06(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        cube = Cube(fill_opacity=0.1, stroke_width=1)
        cube.color = BLACK
        self.add(cube)
        self.add(Dot3D((-.75, .75, .75), color=PRIMARY))
        self.add(Dot3D((.75, -.75, -.75), color=PRIMARY))
        self.set_camera_orientation(phi=.35*PI, theta=.35*PI, zoom=2)

class Image07(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        cube = Cube(fill_opacity=0.1, stroke_width=1)
        cube.color = BLACK
        self.add(cube)
        self.add(Dot3D((-.75, .75, .75), color=PRIMARY))
        self.add(Dot3D((.75, -.75, -.75), color=PRIMARY))
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