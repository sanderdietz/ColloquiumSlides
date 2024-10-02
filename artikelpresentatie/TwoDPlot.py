# manim -qh TwoDPlot.py Image01 Image02 Image03 Image04 Image05 Image06 Image07

from manim import *

config.frame_height = 8
config.frame_width = 8
config.frame_size = (1000, 1000)

PRIMARY = "#00a6d6"
SECONDARY = "#e03c31"

class Base2D(Scene):
    def function(self, x, y):
        W = 1
        w = 2 / 3
        return x * (1 - y) * w + (1 - x) * y * W

    def setup_axes(self):
        axes = Axes(
            x_range=[0, 1, .2],
            y_range=[0, 1, .2],
            x_length=6,
            y_length=6,
            axis_config={
                "include_numbers": True,
                "include_tip": False
            })
        axes.color = BLACK
        labels = axes.get_axis_labels(MathTex(r"y", color=BLACK), MathTex(r"E", color=BLACK))
        return axes, labels
    
    def setup(self):
        self.camera.background_color = WHITE
        axes, labels = self.setup_axes()
        self.add(axes, labels)
        return axes

    def plot_n_lines(self, axes, n):
        for i in range(1, n):
            self.add(axes.plot(lambda y: self.function(.1 * i, y), color=GRAY, stroke_width=2))
        self.add(axes.plot(lambda y: self.function(.1 * n, y), color=PRIMARY, stroke_width=8))


class Image01(Base2D):
    def construct(self):
        axes = self.setup()
        self.plot_n_lines(axes, 1)

class Image02(Base2D):
    def construct(self):
        axes = self.setup()
        self.plot_n_lines(axes, 2)

class Image03(Base2D):
    def construct(self):
        axes = self.setup()
        self.plot_n_lines(axes, 3)

class Image04(Base2D):
    def construct(self):
        axes = self.setup()
        self.plot_n_lines(axes, 4)

class Image05(Base2D):
    def construct(self):
        axes = self.setup()
        self.plot_n_lines(axes, 5)

class Image06(Base2D):
    def construct(self):
        axes = self.setup()
        self.plot_n_lines(axes, 6)

class Image07(Base2D):
    def construct(self):
        axes = self.setup()
        self.plot_n_lines(axes, 7)