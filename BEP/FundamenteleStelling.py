from manim import *
from Helper import *

set_frame_size()

class Image01(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = ThreeDAxes(
            x_range=[-5, 5],
            y_range=[-5, 5],
            z_range=[-5, 5],
            axis_config={
                "include_numbers": False,
                "include_tip": False
            }
        )
        axes.color = BLACK
        self.add(axes)

        point = axes.c2p(-1, 1, 2)
        x = Dot3D(point, color=SECONDARY)
        U = Sphere(
            axes.c2p(-.5, .5, 1),
            radius=1.5,
            resolution=(50, 25),
            fill_opacity=.2,
            stroke_width=.2
        ).set_color(PRIMARY)

        V = Sphere(
            point,
            radius=.5,
            resolution=(50, 25),
            fill_opacity=.2,
            stroke_width=.2
        ).set_color(TERTIARY)

        self.add(x, U, V)

        self.set_camera_orientation(phi=.35*PI, theta=.25*PI, zoom=.8)

class Image02(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE

        space = Sphere(
            radius=4,
            resolution=(50,25),
            stroke_color=BLACK,
            stroke_width=.5
        ).set_color(GRAY_A)
        self.add(space)

        phi = .35 * PI
        theta = .25 * PI
        point = (4 * np.cos(phi) * np.sin(theta), 4 * np.sin(phi) * np.sin(theta), 4 * np.cos(theta))
        x = Dot3D(point, radius=.25, color=SECONDARY)
        self.add(x)

        sphere1 = Sphere(
            radius=4,
            resolution=(50,25),
        )
        sphere2 = Sphere(
            center=(4, 0, 0),
            radius=4,
            resolution=(50,25)
        )
        Torus()
        shape = Intersection(sphere1, sphere2, color=BLUE)
        self.add(shape)
        self.add(Circle().shift((0, 0, 4)).rotate_about_origin(.25 * PI))

        # U = Sphere(
        #     axes.c2p(-.5, .5, 1),
        #     radius=1.5,
        #     resolution=(50, 25),
        #     fill_opacity=.2,
        #     stroke_width=.2
        # ).set_color(PRIMARY)

        # V = Sphere(
        #     point,
        #     radius=.5,
        #     resolution=(50, 25),
        #     fill_opacity=.2,
        #     stroke_width=.2
        # ).set_color(TERTIARY)

        # self.add(x, U, V)

        self.set_camera_orientation(phi=.35*PI, theta=.25*PI, zoom=.8)
