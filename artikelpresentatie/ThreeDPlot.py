from manim import *

PRIMARY = "#00a6d6"
SECONDARY = "#e03c31"
TERTIARY = "#0c2340"

class Image01(ThreeDScene):
    def function(self, u, v):
        W = 1
        w = .66
        if (u == 0) and (v == 0):
            return np.array([0, 0, 0])
        return np.array([u,
                         v,
                         w * u * (1 - v) + W * (1 - u) * v])

    def construct(self):
        self.camera.background_color = WHITE

        axes = ThreeDAxes(
            x_range=[0, 1, .2],
            y_range=[0, 1, .2],
            z_range=[0, 1, .2],
            axis_config={
                "include_numbers": True,
                "include_tip": False
            })
        axes.color = BLACK
        surface = Surface(
            lambda u, v: axes.c2p(*self.function(u, v)),
            u_range=[0, 1],
            v_range=[0, 1],
            resolution=10,
            checkerboard_colors=[PRIMARY, TERTIARY]
        )
        labels = axes.get_axis_labels(
            MathTex(r"x"), MathTex(r"y"), MathTex(r"\mathbb{R}")
        )
        self.add(axes, surface, labels)
        self.add(Line3D(start=axes.coords_to_point(.6, 0, .4), end=axes.coords_to_point(.6, 1, .4), color=SECONDARY, stroke_width=6))
        self.set_camera_orientation(phi=.35 * PI, theta=.1 * PI, zoom=.5)
