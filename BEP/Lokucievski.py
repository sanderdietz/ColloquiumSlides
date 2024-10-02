from manim import *
from Helper import *
import random

class Image01(Scene):
    def cantor(self, x, y, width):
        if width >= .001 and y > -4:
            self.add(Line((x, y, 0), (x + width, y, 0), color=BLACK, stroke_width=10))
            y -= 1
            self.cantor(x, y, width / 3)
            self.cantor(x + width * 2 / 3, y, width / 3)

    def construct(self):
        self.camera.background_color = WHITE
        self.cantor(-6, 3, 12)

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        step_size = .5
        for i in range(6):
            self.add(Line((-6 + i * step_size, -.25, 0), (-6 + i * step_size, .25, 0), color=BLACK))
            self.add(MathTex(i, color=BLACK).shift((-6 + i * step_size, -.5, 0)))
            if i == 5:
                self.add(MathTex("...", color=BLACK).shift((-6 + (i + 1) * step_size, -.5, 0)))
        
        self.add(Line((1, -.25, 0), (1, .25, 0), color=BLACK))
        self.add(MathTex("\omega_0", color=BLACK).shift((1, -.5, 0)))

        self.add(Line((6, -.25, 0), (6, .25, 0), color=BLACK))
        self.add(MathTex("\omega_1", color=BLACK).shift((6, -.5, 0)))
        
        self.add(Line((-6, 0, 0), (6, 0, 0), color=BLACK, stroke_width=10))

class LxC(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.endpoints = set()

    def cantor(self, start, width):
        if width > .025:
            self.endpoints.add(start)
            self.endpoints.add(start + width)
            self.cantor(start, width / 3)
            self.cantor(start + width * 2 / 3, width / 3)

class Image03(LxC):
    def construct(self):
        self.camera.background_color = WHITE

        self.cantor(-2, 4)
        for y in self.endpoints:
            self.add(Line((-3, y, 0), (3, y, 0), color=BLACK, stroke_width=1))

        self.add(MathTex("C", color=BLACK).shift((-3.25, 0, 0)))
        self.add(MathTex("L", color=BLACK).shift((0, 2.25, 0)))
        self.add(MathTex("0", color=BLACK).shift((-3, -2.25, 0)))
        self.add(MathTex("\omega_1", color=BLACK).shift((3, -2.25, 0)))

class Image08(LxC):
    def construct(self):
        self.camera.background_color = WHITE

        self.cantor(-3, 6)
        for y in self.endpoints:
            self.add(Dot((-3, y, 0), radius=.025, color=BLACK))
        
        self.add(Line((3, 3, 0), (3, -3, 0), color=BLACK))
        self.add(Arrow((-3, 1, 0), (3, 0, 0), color=BLACK))

class Image09(LxC):
    def construct(self):
        self.camera.background_color = WHITE

        self.cantor(-3, 6)
        for y in self.endpoints:
            self.add(Dot((-3, y, 0), radius=.025, color=BLACK))
        
        self.add(Line((3, 3, 0), (3, -3, 0), color=BLACK))
        self.add(Arrow((-3, 1, 0), (3, 0, 0), color=BLACK))
        self.add(Arrow((-3, -1, 0), (3, 0, 0), color=BLACK))

class Image04(LxC):
    def construct(self):
        self.camera.background_color = WHITE

        self.cantor(-2, 4)
        for y in self.endpoints:
            self.add(Line((-3, y, 0), (3, y, 0), color=BLACK, stroke_width=1))

        self.add(MathTex("C", color=BLACK).shift((-3.25, 0, 0)))
        self.add(MathTex("L", color=BLACK).shift((0, 2.25, 0)))
        self.add(MathTex("0", color=BLACK).shift((-3, -2.25, 0)))
        self.add(MathTex("\omega_1", color=BLACK).shift((3, -2.25, 0)))
        self.add(Ellipse(width=1.5, height=1, fill_opacity=.5, color=PRIMARY, stroke_width=0).shift((3, .5, 0)))

class Image05(LxC):
    def construct(self):
        self.camera.background_color = WHITE

        self.cantor(-2, 4)
        for y in self.endpoints:
            self.add(Line((-3, y, 0), (3, y, 0), color=BLACK, stroke_width=1))

        self.add(MathTex("C", color=BLACK).shift((-3.25, 0, 0)))
        self.add(MathTex("L", color=BLACK).shift((0, 2.25, 0)))
        self.add(MathTex("0", color=BLACK).shift((-3, -2.25, 0)))
        self.add(MathTex("\omega_1", color=BLACK).shift((3, -2.25, 0)))
        # self.add(Ellipse(width=1.5, height=1, fill_opacity=.5, color=PRIMARY, stroke_width=0).shift((3, .5, 0)))
        self.add(Ellipse(width=1, height=1.5, fill_opacity=.5, color=PRIMARY, stroke_width=0).shift((2.5275, .75, 0)))

class Image10(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.endpoints = set()

    def cantor(self, start, width):
        if width > .025:
            self.endpoints.add(start)
            self.endpoints.add(start + width)
            self.cantor(start, width / 3)
            self.cantor(start + width * 2 / 3, width / 3)

    def ternary(self, x):
        ternary = ""
        while x != 0 and len(ternary) <= 6:
            x *= 3
            digit = int(x)
            ternary += str(digit)
            x -= digit
        return ternary

    def binary(self, ternary):
        binary = 0
        for i in range(len(ternary)):
            binary += .5 ** (i + 1) * int(ternary[i]) / 2
        return binary

    def construct(self):
        self.camera.background_color = WHITE
        # self.cantor(-2, 4)
        # self.endpoints = sorted(list(self.endpoints))

        # for i in range(len(self.endpoints) // 2):
        #     self.add(Line((-1, self.endpoints[i * 2], 0), (-1, self.endpoints[i * 2 + 1], 0), color=BLACK))

        # self.add(Line((1, -2, 0), (1, 2, 0), color=BLACK))

        STROKE_WIDTH = 8
        index = 0

        for i in range(10000):
            x = .0001 * i
            ternary = self.ternary(x)
            # if "1" in ternary:
            #     print(x, ternary)
            #     if ternary.count("1") == 1 and ternary[-1] != "1":
            #         index = ternary.index("1")
            #         for j in range(index + 1, len(ternary)):
            #             if ternary[j] == "0":
            #                 break
            #         else:
            #             ternary = ternary[:index] + "2"

            if not "1" in ternary:
                y = -3 + 6 * x
                left_point = (-6, y, 0)
                start_point = (-3, y, 0)
                start_handle = (-.75, y, 0)
                end_point = (3, -3 + 6 * self.binary(ternary), 0)
                end_point_alt = (.25, -2 + 4 * self.binary(ternary), 0)

                eps = .01
                if abs(end_point[1] + 0.8782671535351252) < eps:
                    # self.add(Dot(end_point_alt, color=RED))
                    index = i

                self.add(Line(start_point, end_point, color=BLACK, stroke_width=1))
                self.add(Line((3, -3, 0), (3, 3, 0), color=BLACK))

class Image06(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.endpoints = set()

    def cantor(self, start, width):
        if width > .025:
            self.endpoints.add(start)
            self.endpoints.add(start + width)
            self.cantor(start, width / 3)
            self.cantor(start + width * 2 / 3, width / 3)

    def ternary(self, x):
        ternary = ""
        while x != 0 and len(ternary) <= 6:
            x *= 3
            digit = int(x)
            ternary += str(digit)
            x -= digit
        return ternary

    def binary(self, ternary):
        binary = 0
        for i in range(len(ternary)):
            binary += .5 ** (i + 1) * int(ternary[i]) / 2
        return binary

    def construct(self):
        self.camera.background_color = WHITE
        # self.cantor(-2, 4)
        # self.endpoints = sorted(list(self.endpoints))

        # for i in range(len(self.endpoints) // 2):
        #     self.add(Line((-1, self.endpoints[i * 2], 0), (-1, self.endpoints[i * 2 + 1], 0), color=BLACK))

        # self.add(Line((1, -2, 0), (1, 2, 0), color=BLACK))

        STROKE_WIDTH = 8
        index = 0

        for i in range(10000):
            x = .0001 * i
            ternary = self.ternary(x)
            # if "1" in ternary:
            #     print(x, ternary)
            #     if ternary.count("1") == 1 and ternary[-1] != "1":
            #         index = ternary.index("1")
            #         for j in range(index + 1, len(ternary)):
            #             if ternary[j] == "0":
            #                 break
            #         else:
            #             ternary = ternary[:index] + "2"

            if not "1" in ternary:
                y = -2 + 4 * x
                left_point = (-6, y, 0)
                start_point = (-1.25, y, 0)
                start_handle = (-.75, y, 0)
                end_point = (-.25, -2 + 4 * self.binary(ternary), 0)
                end_point_alt = (.25, -2 + 4 * self.binary(ternary), 0)

                eps = .01
                if abs(end_point[1] + 0.8782671535351252) < eps:
                    # self.add(Dot(end_point_alt, color=RED))
                    index = i

                self.add(Line(left_point, start_point, color=BLACK, stroke_width=1))
                self.add(CubicBezier(start_point, start_handle, end_point, end_point, color=BLACK, stroke_width=1))
                self.add(Line((6, y, 0), (1.25, y, 0), color=BLACK, stroke_width=1))
                self.add(CubicBezier((1.25, y, 0), (.75, y, 0), end_point_alt, end_point_alt, color=BLACK, stroke_width=1))

        random_point = 0
        random.seed(4)
        for i in range(100):
            left_point = (-.25, -2 + .04 * i, 0)
            right_point = (.25, -2 + 4 * random.random(), 0)
            if i == 50:
                random_point = right_point
            self.add(Line(left_point, right_point, color=BLACK, stroke_width=1))

        # self.add(Line((-.25, -2 + .04 * 50, 0), random_point, color=PRIMARY, stroke_width=STROKE_WIDTH))
        # print(random_point[1])

        # x = .0001 * index
        # ternary = self.ternary(x)
        # y = -2 + 4 * x
        # end_point_alt = (.25, -2 + 4 * self.binary(ternary), 0)
        # self.add(Line((2.5, y, 0), (1.25, y, 0), color=PRIMARY, stroke_width=STROKE_WIDTH))
        # self.add(CubicBezier((1.25, y, 0), (.75, y, 0), end_point_alt, end_point_alt, color=PRIMARY, stroke_width=STROKE_WIDTH))


        # x = .3333
        # ternary = self.ternary(x)
        # y = -2 + 4 * x
        # left_point = (-2.5, y, 0)
        # start_point = (-1.25, y, 0)
        # start_handle = (-.75, y, 0)
        # end_point = (-.25, -2 + 4 * self.binary(ternary), 0)
        # self.add(Line(left_point, start_point, color=PRIMARY, stroke_width=STROKE_WIDTH))
        # self.add(CubicBezier(start_point, start_handle, end_point, end_point, color=PRIMARY, stroke_width=STROKE_WIDTH))

        # x = .6667
        # ternary = self.ternary(x)
        # y = -2 + 4 * x
        # left_point = (-2.5, y, 0)
        # start_point = (-1.25, y, 0)
        # start_handle = (-.75, y, 0)
        # end_point = (-.25, -2 + 4 * self.binary(ternary), 0)
        # self.add(Line(left_point, start_point, color=PRIMARY, stroke_width=STROKE_WIDTH))
        # self.add(CubicBezier(start_point, start_handle, end_point, end_point, color=PRIMARY, stroke_width=STROKE_WIDTH))

        self.add(MathTex("0", color=BLACK).shift((-6, -2.25, 0)))
        self.add(MathTex("0", color=BLACK).shift((6, -2.25, 0)))
        self.add(MathTex("\omega_1", color=BLACK).shift((-.35, -2.25, 0)))
        self.add(MathTex("\omega_1", color=BLACK).shift((.35, -2.25, 0)))
        self.add(MathTex("[0,1]", color=BLACK).shift((0, 2.25, 0)))
        self.add(MathTex("C", color=BLACK).shift((-6.25, 0, 0)))
        self.add(MathTex("C", color=BLACK).shift((6.25, 0, 0)))
        self.add(MathTex("L", color=BLACK).shift((-3, 2.25, 0)))
        self.add(MathTex("L", color=BLACK).shift((3, 2.25, 0)))

class Image11(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.endpoints = set()

    def cantor(self, start, width):
        if width > .025:
            self.endpoints.add(start)
            self.endpoints.add(start + width)
            self.cantor(start, width / 3)
            self.cantor(start + width * 2 / 3, width / 3)

    def ternary(self, x):
        ternary = ""
        while x != 0 and len(ternary) <= 6:
            x *= 3
            digit = int(x)
            ternary += str(digit)
            x -= digit
        return ternary

    def binary(self, ternary):
        binary = 0
        for i in range(len(ternary)):
            binary += .5 ** (i + 1) * int(ternary[i]) / 2
        return binary

    def construct(self):
        self.camera.background_color = WHITE

        for i in range(10000):
            x = .0001 * i
            ternary = self.ternary(x)

            if not "1" in ternary:
                y = -3 + 6 * x
                left_point = (-6, y, 0)
                start_point = (4.5, y, 0)
                start_handle = (5.5, y, 0)
                end_point = (6, -3 + 6 * self.binary(ternary), 0)

                self.add(Line(left_point, start_point, color=BLACK, stroke_width=1))
                self.add(CubicBezier(start_point, start_handle, end_point, end_point, color=BLACK, stroke_width=1))

        self.add(Line((6, -3, 0), (6, 3, 0), color=BLACK))

        self.add(MathTex("0", color=BLACK).shift((-6, -3.25, 0)))
        self.add(MathTex("\omega_1", color=BLACK).shift((6, -3.25, 0)))
        self.add(MathTex("[0,1]", color=BLACK).shift((6.5, 0, 0)))
        self.add(MathTex("C", color=BLACK).shift((-6.25, 0, 0)))
        self.add(MathTex("L", color=BLACK).shift((0, 3.25, 0)))

class Image12(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.endpoints = set()

    def cantor(self, start, width):
        if width > .025:
            self.endpoints.add(start)
            self.endpoints.add(start + width)
            self.cantor(start, width / 3)
            self.cantor(start + width * 2 / 3, width / 3)

    def ternary(self, x):
        ternary = ""
        while x != 0 and len(ternary) <= 6:
            x *= 3
            digit = int(x)
            ternary += str(digit)
            x -= digit
        return ternary

    def binary(self, ternary):
        binary = 0
        for i in range(len(ternary)):
            binary += .5 ** (i + 1) * int(ternary[i]) / 2
        return binary

    def construct(self):
        self.camera.background_color = WHITE

        for i in range(10000):
            x = .0001 * i
            ternary = self.ternary(x)

            if not "1" in ternary:
                y = -3 + 6 * x
                left_point = (-6, y, 0)
                start_point = (4.5, y, 0)
                start_handle = (5.5, y, 0)
                end_point = (6, -3 + 6 * self.binary(ternary), 0)

                self.add(Line(left_point, start_point, color=BLACK, stroke_width=1))
                self.add(CubicBezier(start_point, start_handle, end_point, end_point, color=BLACK, stroke_width=1))

        self.add(Line((6, -3, 0), (6, 3, 0), color=BLACK))

        self.add(MathTex("0", color=BLACK).shift((-6, -3.25, 0)))
        self.add(MathTex("\omega_1", color=BLACK).shift((6, -3.25, 0)))
        self.add(MathTex("[0,1]", color=BLACK).shift((6.5, 0, 0)))
        self.add(MathTex("C", color=BLACK).shift((-6.25, 0, 0)))
        self.add(MathTex("L", color=BLACK).shift((0, 3.25, 0)))

        self.add(Ellipse(width=1.5, height=1, fill_opacity=.5, color=PRIMARY, stroke_width=0).shift((6, .5, 0)))

class Image13(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.endpoints = set()

    def cantor(self, start, width):
        if width > .025:
            self.endpoints.add(start)
            self.endpoints.add(start + width)
            self.cantor(start, width / 3)
            self.cantor(start + width * 2 / 3, width / 3)

    def ternary(self, x):
        ternary = ""
        while x != 0 and len(ternary) <= 6:
            x *= 3
            digit = int(x)
            ternary += str(digit)
            x -= digit
        return ternary

    def binary(self, ternary):
        binary = 0
        for i in range(len(ternary)):
            binary += .5 ** (i + 1) * int(ternary[i]) / 2
        return binary

    def construct(self):
        self.camera.background_color = WHITE

        for i in range(10000):
            x = .0001 * i
            ternary = self.ternary(x)

            if not "1" in ternary:
                y = -3 + 6 * x
                left_point = (-6, y, 0)
                start_point = (4.5, y, 0)
                start_handle = (5.5, y, 0)
                end_point = (6, -3 + 6 * self.binary(ternary), 0)

                self.add(Line(left_point, start_point, color=BLACK, stroke_width=1))
                self.add(CubicBezier(start_point, start_handle, end_point, end_point, color=BLACK, stroke_width=1))

        self.add(Line((6, -3, 0), (6, 3, 0), color=BLACK))

        self.add(MathTex("0", color=BLACK).shift((-6, -3.25, 0)))
        self.add(MathTex("\omega_1", color=BLACK).shift((6, -3.25, 0)))
        self.add(MathTex("[0,1]", color=BLACK).shift((6.5, 0, 0)))
        self.add(MathTex("C", color=BLACK).shift((-6.25, 0, 0)))
        self.add(MathTex("L", color=BLACK).shift((0, 3.25, 0)))

        self.add(Ellipse(width=1, height=1.5, fill_opacity=.5, color=PRIMARY, stroke_width=0).shift((5.5275, .75, 0)))

