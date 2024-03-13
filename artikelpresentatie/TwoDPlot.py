from manim import *

config.frame_height = 8
config.frame_width = 8
config.frame_size = (1000, 1000)

PRIMARY = "#00a6d6"
SECONDARY = "#e03c31"

class Plot(Scene):
    def function(self, x, y):
        w = 2 / 3
        W = 1
        return x * (1 - y) * w + (1 - x) * y * W

    def SetupAxes(self):
        self.camera.background_color = WHITE
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

class Image01(Plot):
    def construct(self):
        axes, labels = self.SetupAxes()
        self.add(axes, labels)
        graph = axes.plot(lambda y: self.function(.1, y), color=PRIMARY, stroke_width=8)
        self.add(graph)

class Image02(Plot):
    def construct(self):
        axes, labels = self.SetupAxes()
        self.add(axes, labels)
        self.add(axes.plot(lambda y: self.function(.1, y), color=GRAY, stroke_width=2))
        self.add(axes.plot(lambda y: self.function(.2, y), color=PRIMARY, stroke_width=8))

class Image03(Plot):
    def construct(self):
        axes, labels = self.SetupAxes()
        self.add(axes, labels)
        for i in [.1, .2]:
            self.add(axes.plot(lambda y: self.function(i, y), color=GRAY, stroke_width=2))
        self.add(axes.plot(lambda y: self.function(.3, y), color=PRIMARY, stroke_width=8))

class Image04(Plot):
    def construct(self):
        axes, labels = self.SetupAxes()
        self.add(axes, labels)
        for i in [.1, .2, .3]:
            self.add(axes.plot(lambda y: self.function(i, y), color=GRAY, stroke_width=2))
        self.add(axes.plot(lambda y: self.function(.4, y), color=PRIMARY, stroke_width=8))

class Image05(Plot):
    def construct(self):
        axes, labels = self.SetupAxes()
        self.add(axes, labels)
        for i in [.1, .2, .3, .4]:
            self.add(axes.plot(lambda y: self.function(i, y), color=GRAY, stroke_width=2))
        self.add(axes.plot(lambda y: self.function(.5, y), color=PRIMARY, stroke_width=8))

class Image06(Plot):
    def construct(self):
        axes, labels = self.SetupAxes()
        self.add(axes, labels)
        for i in [.1, .2, .3, .4, .5]:
            self.add(axes.plot(lambda y: self.function(i, y), color=GRAY, stroke_width=2))
        self.add(axes.plot(lambda y: self.function(.6, y), color=PRIMARY, stroke_width=8))

class Image07(Plot):
    def construct(self):
        axes, labels = self.SetupAxes()
        self.add(axes, labels)
        for i in [.1, .2, .3, .4, .5, .6]:
            self.add(axes.plot(lambda y: self.function(i, y), color=GRAY, stroke_width=2))
        self.add(axes.plot(lambda y: self.function(.7, y), color=PRIMARY, stroke_width=8))