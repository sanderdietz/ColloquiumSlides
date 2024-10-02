from manim import *

PRIMARY = "#00a6d6"
SECONDARY = "#e03c31"
TERTIARY = "#0c2340"

class Base3D(ThreeDScene):
    def function(self, u, v):
        W = 1
        w = 2 / 3
        return np.array([u, v, w * u * (1 - v) + W * (1 - u) * v])
    
    def setup_axes(self):
        axes = ThreeDAxes(
            x_range=[0, 1, .2],
            y_range=[0, 1, .2],
            z_range=[0, 1, .2],
            axis_config={
                "include_numbers": True,
                "include_tip": False
            })
        axes.color = BLACK
        labels = axes.get_axis_labels(
            MathTex(r"x"), MathTex(r"y"), MathTex(r"E")
        )
        return axes, labels
    
    def plot_surface(self, axes):
        surface = Surface(
            lambda u, v: axes.c2p(*self.function(u, v)),
            u_range=[0, 1],
            v_range=[0, 1],
            resolution=10,
            checkerboard_colors=[PRIMARY, TERTIARY]
        )
        return surface
    
    def setup(self):
        self.camera.background_color = WHITE
        axes, labels = self.setup_axes()
        surface = self.plot_surface(axes)
        self.add(axes, labels, surface)
        return axes

class Image01(Base3D):
    def construct(self):
        axes = self.setup()
        self.add(Line3D(start=axes.coords_to_point(.6, 0, .4), end=axes.coords_to_point(.6, 1, .4), color=SECONDARY, stroke_width=6))
        self.set_camera_orientation(phi=.35 * PI, theta=.1 * PI, zoom=.5)

class Image02(Base3D):
    def construct(self):
        axes = self.setup()
        self.add(Dot(point=axes.coords_to_point(.6, .4, .4), color=SECONDARY, stroke_width=6))
        self.set_camera_orientation(phi=.35 * PI, theta=.1 * PI, zoom=.5)
