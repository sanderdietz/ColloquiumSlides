from manim import *
from Helper import *

config.frame_height = 8
config.frame_width = 8
config.frame_size = (1000, 1000)

class Image01(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        upper_line = Line(UP * 3, UR * 3, stroke_color=BLACK, stroke_width=10)
        middle_line = Line(ORIGIN, RIGHT * 3, stroke_color=BLACK, stroke_width=10)
        lower_line = Line(DOWN * 3, DR * 3, stroke_color=BLACK, stroke_width=10)
        vertical_line = Line(UP * 3.05, DOWN * 3.05, stroke_color=BLACK, stroke_width=10)
        self.add(upper_line, middle_line, lower_line, vertical_line)
        self.play(Uncreate(lower_line))

class Image02(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        upper_line = Line(UP * 3, UR * 3, stroke_color=BLACK, stroke_width=10)
        middle_line = Line(ORIGIN, RIGHT * 3, stroke_color=BLACK, stroke_width=10)
        vertical_line = Line(UP * 3.05, DOWN * 3.05, stroke_color=BLACK, stroke_width=10)
        letter = VGroup(middle_line, vertical_line)
        self.add(upper_line, letter)
        self.play(Uncreate(upper_line))
        self.wait()
        self.play(Rotate(letter, -.5 * PI, about_point=ORIGIN))

class Image03(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        left_line = Line(LEFT * 3.05, ORIGIN, stroke_color=BLACK, stroke_width=10)
        right_line = Line(RIGHT * 3.05, ORIGIN, stroke_color=BLACK, stroke_width=10)
        vertical_line = Line(ORIGIN, DOWN * 3, stroke_color=BLACK, stroke_width=10)
        self.add(left_line, right_line, vertical_line)
        self.play(Rotate(left_line, -.25 * PI, about_point=ORIGIN), Rotate(right_line, .25 * PI, about_point=ORIGIN))

class Image04(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        left_line = Line(LEFT * 3.05, ORIGIN, stroke_color=BLACK, stroke_width=10).rotate(-.25 * PI, about_point=ORIGIN)
        right_line = Line(RIGHT * 3.05, ORIGIN, stroke_color=BLACK, stroke_width=10).rotate(.25 * PI, about_point=ORIGIN)
        vertical_line = Line(ORIGIN, DOWN * 3, stroke_color=BLACK, stroke_width=10)
        self.add(left_line, right_line, vertical_line)
        self.play(Rotate(vertical_line, -.25 * PI, about_point=ORIGIN))
        self.wait()
        self.play(Create(Line(LEFT * 3.05, ORIGIN, stroke_color=BLACK, stroke_width=10).rotate(.75 * PI, about_point=ORIGIN)))

class Image05(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        left_line = Line(LEFT * 3.05, ORIGIN, stroke_color=BLACK, stroke_width=10).rotate(-.25 * PI, about_point=ORIGIN)
        right_line = Line(RIGHT * 3.05, ORIGIN, stroke_color=BLACK, stroke_width=10).rotate(.25 * PI, about_point=ORIGIN)
        bottom_left_line = Line(ORIGIN, DOWN * 3, stroke_color=BLACK, stroke_width=10).rotate(-.25 * PI, about_point=ORIGIN)
        bottom_right_line = Line(LEFT * 3.05, ORIGIN, stroke_color=BLACK, stroke_width=10).rotate(.75 * PI, about_point=ORIGIN)
        self.add(left_line, right_line, bottom_left_line, bottom_right_line)
        
# class Image01(Scene):
#     def construct(self):
#         self.camera.background_color = WHITE
#         vertical_line = Line(ORIGIN, DOWN * 3, stroke_color=BLACK, stroke_width=10)
#         left_line = Line(ORIGIN, UL * 1.5 * np.sqrt(2), stroke_color=BLACK, stroke_width=10)
#         right_line = Line(ORIGIN, UR * 1.5 * np.sqrt(2), stroke_color=BLACK, stroke_width=10)

#         self.add(vertical_line, left_line, right_line)
#         self.play(Rotate(left_line, .25 * PI, about_point=ORIGIN), Rotate(right_line, -.25 * PI, about_point=ORIGIN))
        
# class Image02(Scene):
#     def construct(self):
#         self.camera.background_color = WHITE
#         horizontal_line = Line(LEFT * 3, RIGHT * 3, stroke_color=BLACK, stroke_width=10)
#         vertical_line = Line(ORIGIN, DOWN * 3, stroke_color=BLACK, stroke_width=10)
#         letter = VGroup(horizontal_line, vertical_line)
#         self.add(letter)
#         self.play(Rotate(letter, .5 * PI, about_point=ORIGIN))
#         self.wait()
#         self.play(Create(Line(UP * 3, UR * 3, stroke_color=BLACK, stroke_width=10)))

# class Image03(Scene):
#     def construct(self):
#         self.camera.background_color = WHITE
#         upper_line = Line(UP * 3, UR * 3, stroke_color=BLACK, stroke_width=10)
#         middle_line = Line(ORIGIN, RIGHT * 3, stroke_color=BLACK, stroke_width=10)
#         vertical_line = Line(UP * 3, DOWN * 3, stroke_color=BLACK, stroke_width=10)
#         letter = VGroup(upper_line, middle_line, vertical_line)
#         self.add(letter)
#         self.play(Create(Line(DOWN * 3, DR * 3, stroke_color=BLACK, stroke_width=10)))

# class Image04(Scene):
#     def construct(self):
#         self.camera.background_color = WHITE
#         upper_line = Line(UP * 3, UR * 3, stroke_color=BLACK, stroke_width=10)
#         middle_line = Line(ORIGIN, RIGHT * 3, stroke_color=BLACK, stroke_width=10)
#         lower_line = Line(DOWN * 3, DR * 3, stroke_color=BLACK, stroke_width=10)
#         vertical_line = Line(UP * 3, DOWN * 3, stroke_color=BLACK, stroke_width=10)
#         self.add(upper_line, middle_line, lower_line, vertical_line)