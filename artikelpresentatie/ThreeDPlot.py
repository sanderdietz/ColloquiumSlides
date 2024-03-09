from manim import *

class Slide1(ThreeDScene):
    def function(self, u, v):
        W = 1
        w = .66
        if (u == 0) and (v == 0):
            return np.array([0, 0, 0])
        return np.array([u,
                         v,
                         W * (v * v) / ((u + v) * (u + v)) + w * (u * u) / ((u + v) * (u + v))])

    def construct(self):
        axes = ThreeDAxes(x_range=[0, 1], y_range=[0, 1], z_range=[0, 1])
        surface = Surface(
            lambda u, v: axes.c2p(*self.function(u, v)),
            u_range=[0, 1],
            v_range=[0, 1]
        )
        self.set_camera_orientation(zoom=.5)
        self.add(axes, surface)
