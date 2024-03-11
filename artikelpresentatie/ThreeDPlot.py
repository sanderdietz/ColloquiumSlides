from manim import *

class Slide1(ThreeDScene):
    def function(self, u, v):
        W = 1
        w = .66
        if (u == 0) and (v == 0):
            return np.array([0, 0, 0])
        return np.array([u,
                         v,
                         w * u * (1 - v) + W * (1 - u) * v])

    def construct(self):
        axes = ThreeDAxes(x_range=[0, 1], y_range=[0, 1], z_range=[0, 1])
        surface = Surface(
            lambda u, v: axes.c2p(*self.function(u, v)),
            u_range=[0, 1],
            v_range=[0, 1],
            resolution=10
        )
        labels = axes.get_axis_labels(
            Text("x"), Text("y"), Text("z")
        )
        self.add(axes, surface, labels)
        # THETA 0 .25 * PI
        self.set_camera_orientation(phi=.25 * PI, theta=.25 * PI, zoom=.5)
        self.move_camera(phi=.5 * PI, theta=.25 * PI, zoom=.5)
        self.move_camera(phi=.5 * PI, theta=-.25 * PI, zoom=.5)
        # self.wait(.5)
        # self.begin_ambient_camera_rotation(rate=0.25)
        # self.wait(10)
