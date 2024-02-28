# Render all images in high quality (1080x1920) using the following command:
# manim -qh HarmonicSeries.py Slide1 Slide2 Slide3 Slide4 Slide5 Slide6 Slide7 Slide8 Slide9 Slide10 Slide11


from manim import *

BACKGROUND = "#031b2d"
PRIMARY = "#f0a563"
SECONDARY = "#e1d2c5"

class Slide0(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        WIDTH = 12.0
        HEIGHT = 5.0
        n = 8
        corners = []

        for i in range(1, n + 2):
            rect = Rectangle(width=WIDTH/n, height=HEIGHT/i).shift(LEFT * (WIDTH * .5 + .5 * WIDTH / n - i * WIDTH / n)).shift(DOWN * (HEIGHT - .5 - .5 * HEIGHT / i)).shift(UP)
            corners.append(rect.get_corner(UL))
            corners.append(rect.get_corner(UR))
            if i == 1:
                text = MathTex(r"1").move_to(rect)
            else:
                text = MathTex(r"\frac{1}{" + str(i) + r"}").move_to(rect)
                if i > 2:
                    text.scale(3 / i)
            self.add(rect, text)
        
        self.add(Tex(r"Harmonische reeks ($p=1$)").scale(2).to_edge(UP))

class Slide1(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=4.0, height=4.0).shift(LEFT * 2.0) # 1
        rect2 = Rectangle(width=2.0, height=4.0).shift(RIGHT * 2.0) # 1/2
        text1 = MathTex(r"1").shift(LEFT * 2.0).shift(UP * 3.0)
        text2 = MathTex(r"\geq").shift(RIGHT * .5).shift(UP * 3.0)
        text3 = MathTex(r"\frac{1}{2}").shift(RIGHT * 2.0).shift(UP * 3.0)

        self.add(rect1, rect2, text1, text2, text3)

class Slide2(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND
        rect1 = Rectangle(width=2.0, height=4.0).shift(LEFT * 2.0) # 1/2
        rect2 = Rectangle(width=2.0, height=4.0).shift(RIGHT * 2.0) # 1/2
        text1 = MathTex(r"\frac{1}{2}").shift(LEFT * 2.0).shift(UP * 3.0)
        text2 = MathTex(r"\geq").shift(UP * 3.0)
        text3 = MathTex(r"\frac{1}{2}").shift(RIGHT * 2.0).shift(UP * 3.0)

        self.add(rect1, rect2, text1, text2, text3)

class Slide3(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        toprect1 = Rectangle(width=2.0, height=2.0).shift(UP * 1.5).shift(LEFT * 3.5) # 1/3
        toprect2 = Rectangle(width=2.0, height=1.5).shift(UP * 1.25).shift(LEFT * .5) # 1/4
        toprect3 = Rectangle(width=2.0, height=3.0).shift(UP * 2.0).shift(RIGHT * 3.5) # 1/2

        toptext1 = MathTex(r"\frac{1}{3}").move_to(toprect1.get_center())
        toptext2 = MathTex(r"\frac{1}{4}").move_to(toprect2.get_center())
        toptext3 = MathTex(r"\frac{1}{2}").move_to(toprect3.get_center())

        eq1 = MathTex(r"+").shift(LEFT * 2.0).shift(UP * 1.25)
        eq2 = MathTex(r"\geq").shift(RIGHT * 1.5).shift(UP * 1.25)

        self.add(toprect1, toprect2, toprect3)
        self.add(toptext1, toptext2, toptext3, eq1, eq2)

class Slide4(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        toprect1 = Rectangle(width=2.0, height=2.0).shift(UP * 1.5).shift(LEFT * 3.5) # 1/3
        toprect2 = Rectangle(width=2.0, height=1.5).shift(UP * 1.25).shift(LEFT * .5) # 1/4
        toprect3 = Rectangle(width=2.0, height=3.0).shift(UP * 2.0).shift(RIGHT * 3.5) # 1/2

        toptext1 = MathTex(r"\frac{1}{3}").move_to(toprect1.get_center())
        toptext2 = MathTex(r"\frac{1}{4}").move_to(toprect2.get_center())
        toptext3 = MathTex(r"\frac{1}{2}").move_to(toprect3.get_center())

        eq1 = MathTex(r"+").shift(LEFT * 2.0).shift(UP * 1.25)
        eq2 = MathTex(r"\geq").shift(RIGHT * 1.5).shift(UP * 1.25)

        geq1 = MathTex(r"\geq").shift(LEFT * 3.5).shift(DOWN * .5).rotate(-PI / 2.0)
        geq2 = MathTex(r"\geq").shift(LEFT * .5).shift(DOWN * .5).rotate(-PI / 2.0)

        bottomrect1 = Rectangle(width=2.0, height=2.0, color=GRAY).shift(DOWN * 2.5).shift(LEFT * 3.5) # 1/3
        bottomrect2 = Rectangle(width=2.0, height=1.5, color=PRIMARY, stroke_width=10).shift(DOWN * 2.75).shift(LEFT * 3.5) # 1/4
        bottomrect3 = Rectangle(width=2.0, height=1.5, color=PRIMARY, stroke_width=10).shift(DOWN * 2.75).shift(LEFT * .5) # 1/4
        bottomrect4 = Rectangle(width=2.0, height=3.0, color=PRIMARY, stroke_width=10).shift(DOWN * 2.0).shift(RIGHT * 3.5) # 1/2

        eq3 = MathTex(r"+").shift(LEFT * 2.0).shift(DOWN * 2.75)
        eq4 = MathTex(r"=").shift(RIGHT * 1.5).shift(DOWN * 2.75)

        bottomtext1 = MathTex(r"\mathbf{\frac{1}{4}}", color=PRIMARY).move_to(bottomrect2.get_center())
        bottomtext2 = MathTex(r"\mathbf{\frac{1}{4}}", color=PRIMARY).move_to(bottomrect3.get_center())
        bottomtext3 = MathTex(r"\mathbf{\frac{1}{2}}", color=PRIMARY).move_to(bottomrect4.get_center())

        self.add(toprect1, toprect2, toprect3, bottomrect1, bottomrect2, bottomrect3, bottomrect4)
        self.add(toptext1, toptext2, toptext3, bottomtext1, bottomtext2, bottomtext3, geq1, geq2, eq1, eq2, eq3, eq4)

class Slide5(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        C = 128.0 / 153.0

        toprect1 = Rectangle(width=2.0 * C, height=1.2).shift(UP * 1.1).shift(LEFT * 6.5 * C) # 1/5
        toprect2 = Rectangle(width=2.0 * C, height=1.0).shift(UP).shift(LEFT * 3.5 * C) # 1/6
        toprect3 = Rectangle(width=2.0 * C, height=6.0/7.0).shift(UP * 13.0 / 14.0).shift(LEFT * .5 * C) # 1/7
        toprect4 = Rectangle(width=2.0 * C, height=.75).shift(UP * .875).shift(RIGHT * 2.5 * C) # 1/8
        toprect5 = Rectangle(width=2.0 * C, height=3.0).shift(UP * 2.0).shift(RIGHT * 6.5 * C) # 1/2

        toptext1 = MathTex(r"\frac{1}{5}").move_to(toprect1.get_center()).scale(.8)
        toptext2 = MathTex(r"\frac{1}{6}").move_to(toprect2.get_center()).scale(2.0 / 3.0)
        toptext3 = MathTex(r"\frac{1}{7}").move_to(toprect3.get_center()).scale(12.0 / 21.0)
        toptext4 = MathTex(r"\frac{1}{8}").move_to(toprect4.get_center()).scale(.5)
        toptext5 = MathTex(r"\frac{1}{2}").move_to(toprect5.get_center())

        eq1 = MathTex(r"+").shift(LEFT * 5 * C).shift(UP * .875)
        eq2 = MathTex(r"+").shift(LEFT * 2 * C).shift(UP * .875)
        eq3 = MathTex(r"+").shift(RIGHT * C).shift(UP * .875)
        eq4 = MathTex(r"\geq").shift(RIGHT * 4.5 * C).shift(UP * .875)

        self.add(toprect1, toprect2, toprect3, toprect4, toprect5)
        self.add(toptext1, toptext2, toptext3, toptext4, toptext5)
        self.add(eq1, eq2, eq3, eq4)

class Slide6(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        C = 128.0 / 153.0

        toprect1 = Rectangle(width=2.0 * C, height=1.2).shift(UP * 1.1).shift(LEFT * 6.5 * C) # 1/5
        toprect2 = Rectangle(width=2.0 * C, height=1.0).shift(UP).shift(LEFT * 3.5 * C) # 1/6
        toprect3 = Rectangle(width=2.0 * C, height=6.0/7.0).shift(UP * 13.0 / 14.0).shift(LEFT * .5 * C) # 1/7
        toprect4 = Rectangle(width=2.0 * C, height=.75).shift(UP * .875).shift(RIGHT * 2.5 * C) # 1/8
        toprect5 = Rectangle(width=2.0 * C, height=3.0).shift(UP * 2.0).shift(RIGHT * 6.5 * C) # 1/2

        toptext1 = MathTex(r"\frac{1}{5}").move_to(toprect1.get_center()).scale(.8)
        toptext2 = MathTex(r"\frac{1}{6}").move_to(toprect2.get_center()).scale(2.0 / 3.0)
        toptext3 = MathTex(r"\frac{1}{7}").move_to(toprect3.get_center()).scale(12.0 / 21.0)
        toptext4 = MathTex(r"\frac{1}{8}").move_to(toprect4.get_center()).scale(.5)
        toptext5 = MathTex(r"\frac{1}{2}").move_to(toprect5.get_center())

        eq1 = MathTex(r"+").shift(LEFT * 5 * C).shift(UP * .875)
        eq2 = MathTex(r"+").shift(LEFT * 2 * C).shift(UP * .875)
        eq3 = MathTex(r"+").shift(RIGHT * C).shift(UP * .875)
        eq4 = MathTex(r"\geq").shift(RIGHT * 4.5 * C).shift(UP * .875)


        geq1 = MathTex(r"\geq").shift(LEFT * 6.5 * C).shift(DOWN * .9).rotate(-PI / 2.0)
        geq2 = MathTex(r"\geq").shift(LEFT * 3.5 * C).shift(DOWN * .9).rotate(-PI / 2.0)
        geq3 = MathTex(r"\geq").shift(LEFT * .5 * C).shift(DOWN * .9).rotate(-PI / 2.0)
        geq4 = MathTex(r"\geq").shift(RIGHT * 2.5 * C).shift(DOWN * .9).rotate(-PI / 2.0)

        bottomrect1 = Rectangle(width=2.0 * C, height=1.2, color=GRAY).shift(DOWN * 2.9).shift(LEFT * 6.5 * C) # 1/5
        bottomrect2 = Rectangle(width=2.0 * C, height=.75, color=PRIMARY, stroke_width=10).shift(DOWN * 3.125).shift(LEFT * 6.5 * C) # 1/8
        bottomrect3 = Rectangle(width=2.0 * C, height=1.0, color=GRAY).shift(DOWN * 3.0).shift(LEFT * 3.5 * C) # 1/6
        bottomrect4 = Rectangle(width=2.0 * C, height=.75, color=PRIMARY, stroke_width=10).shift(DOWN * 3.125).shift(LEFT * 3.5 * C) # 1/8
        bottomrect5 = Rectangle(width=2.0 * C, height=6.0/7.0, color=GRAY).shift(DOWN * 43.0 / 14.0).shift(LEFT * .5 * C) # 1/7
        bottomrect6 = Rectangle(width=2.0 * C, height=.75, color=PRIMARY, stroke_width=10).shift(DOWN * 3.125).shift(LEFT * .5 * C) # 1/8
        bottomrect7 = Rectangle(width=2.0 * C, height=.75, color=PRIMARY, stroke_width=10).shift(DOWN * 3.125).shift(RIGHT * 2.5 * C) # 1/8
        bottomrect8 = Rectangle(width=2.0 * C, height=3.0, color=PRIMARY, stroke_width=10).shift(DOWN * 2.0).shift(RIGHT * 6.5 * C) # 1/2
        
        bottomtext1 = MathTex(r"\mathbf{\frac{1}{8}}", color=PRIMARY).move_to(bottomrect2.get_center()).scale(.5)
        bottomtext2 = MathTex(r"\mathbf{\frac{1}{8}}", color=PRIMARY).move_to(bottomrect4.get_center()).scale(.5)
        bottomtext3= MathTex(r"\mathbf{\frac{1}{8}}", color=PRIMARY).move_to(bottomrect6.get_center()).scale(.5)
        bottomtext4 = MathTex(r"\mathbf{\frac{1}{8}}", color=PRIMARY).move_to(bottomrect7.get_center()).scale(.5)
        bottomtext5 = MathTex(r"\mathbf{\frac{1}{2}}", color=PRIMARY).move_to(bottomrect8.get_center())

        eq5 = MathTex(r"+").shift(LEFT * 5 * C).shift(DOWN * 3.125)
        eq6 = MathTex(r"+").shift(LEFT * 2 * C).shift(DOWN * 3.125)
        eq7 = MathTex(r"+").shift(RIGHT * C).shift(DOWN * 3.125)
        eq8 = MathTex(r"=").shift(RIGHT * 4.5 * C).shift(DOWN * 3.125)

        self.add(toprect1, toprect2, toprect3, toprect4, toprect5)
        self.add(toptext1, toptext2, toptext3, toptext4, toptext5)
        self.add(eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8)
        self.add(bottomrect1, bottomrect2, bottomrect3, bottomrect4, bottomrect5, bottomrect6, bottomrect7, bottomrect8)
        self.add(geq1, geq2, geq3, geq4)
        self.add(bottomtext1, bottomtext2, bottomtext3, bottomtext4, bottomtext5)

class Slide7(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        C = 128.0 / 153.0

        toprect1 = Rectangle(width=2.0 * C, height=1.2).shift(UP * 1.1).shift(LEFT * 6.5 * C) # 1/5
        toprect2 = Rectangle(width=2.0 * C, height=1.0).shift(UP).shift(LEFT * 3.5 * C) # 1/6
        # toprect3 = Rectangle(width=2.0 * C, height=6.0/7.0).shift(UP * 13.0 / 14.0).shift(LEFT * .5 * C) # 1/7
        toprect4 = Rectangle(width=2.0 * C, height=.75).shift(UP * .875).shift(RIGHT * 2.5 * C) # 1/8
        toprect5 = Rectangle(width=2.0 * C, height=3.0).shift(UP * 2.0).shift(RIGHT * 6.5 * C) # 1/2

        toptext1 = MathTex(r"\frac{1}{2^n+1}").move_to(toprect1.get_center()).scale(.8)
        toptext2 = MathTex(r"\frac{1}{2^n+2}").move_to(toprect2.get_center()).scale(2.0 / 3.0)
        # toptext3 = MathTex(r"...").move_to(toprect3.get_center()).scale(12.0 / 21.0)
        toptext4 = MathTex(r"\frac{1}{2^{n+1}}").move_to(toprect4.get_center()).scale(.5)
        toptext5 = MathTex(r"\frac{1}{2}").move_to(toprect5.get_center())

        eq1 = MathTex(r"+").shift(LEFT * 5 * C).shift(UP * .875)
        eq2 = MathTex(r"+").shift(LEFT * 2 * C).shift(UP * .875)
        dotdotdot = MathTex(r"...").shift(LEFT * .5 * C).shift(UP * .75)
        eq3 = MathTex(r"+").shift(RIGHT * C).shift(UP * .875)
        eq4 = MathTex(r"\geq").shift(RIGHT * 4.5 * C).shift(UP * .875)

        brace = BraceBetweenPoints([-7.5 * C, 1.7, 0], [3.5 * C, 1.7, 0], [0, 1, 0])
        bracelabel = MathTex(r"2^n\text{ keer}").shift(LEFT * 2.0 * C).shift(UP * 2.75)

        self.add(toprect1, toprect2, toprect4, toprect5)
        self.add(toptext1, toptext2, toptext4, toptext5)
        self.add(eq1, eq2, eq3, eq4, dotdotdot, brace, bracelabel)

class Slide8(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        C = 128.0 / 153.0

        toprect1 = Rectangle(width=2.0 * C, height=1.2).shift(UP * 1.1).shift(LEFT * 6.5 * C) # 1/5
        toprect2 = Rectangle(width=2.0 * C, height=1.0).shift(UP).shift(LEFT * 3.5 * C) # 1/6
        # toprect3 = Rectangle(width=2.0 * C, height=6.0/7.0).shift(UP * 13.0 / 14.0).shift(LEFT * .5 * C) # 1/7
        toprect4 = Rectangle(width=2.0 * C, height=.75).shift(UP * .875).shift(RIGHT * 2.5 * C) # 1/8
        toprect5 = Rectangle(width=2.0 * C, height=3.0).shift(UP * 2.0).shift(RIGHT * 6.5 * C) # 1/2

        toptext1 = MathTex(r"\frac{1}{2^n+1}").move_to(toprect1.get_center()).scale(.8)
        toptext2 = MathTex(r"\frac{1}{2^n+2}").move_to(toprect2.get_center()).scale(2.0 / 3.0)
        # toptext3 = MathTex(r"\frac{1}{7}").move_to(toprect3.get_center()).scale(12.0 / 21.0)
        toptext4 = MathTex(r"\frac{1}{2^{n+1}}").move_to(toprect4.get_center()).scale(.5)
        toptext5 = MathTex(r"\frac{1}{2}").move_to(toprect5.get_center())

        eq1 = MathTex(r"+").shift(LEFT * 5 * C).shift(UP * .875)
        eq2 = MathTex(r"+").shift(LEFT * 2 * C).shift(UP * .875)
        dotdotdot1 = MathTex(r"...").shift(LEFT * .5 * C).shift(UP * .75)
        eq3 = MathTex(r"+").shift(RIGHT * C).shift(UP * .875)
        eq4 = MathTex(r"\geq").shift(RIGHT * 4.5 * C).shift(UP * .875)


        geq1 = MathTex(r"\geq").shift(LEFT * 6.5 * C).shift(DOWN * .9).rotate(-PI / 2.0)
        geq2 = MathTex(r"\geq").shift(LEFT * 3.5 * C).shift(DOWN * .9).rotate(-PI / 2.0)
        geq3 = MathTex(r"\geq").shift(LEFT * .5 * C).shift(DOWN * .9).rotate(-PI / 2.0)
        geq4 = MathTex(r"\geq").shift(RIGHT * 2.5 * C).shift(DOWN * .9).rotate(-PI / 2.0)

        bottomrect1 = Rectangle(width=2.0 * C, height=1.2, color=GRAY).shift(DOWN * 2.9).shift(LEFT * 6.5 * C) # 1/5
        bottomrect2 = Rectangle(width=2.0 * C, height=.75, color=PRIMARY, stroke_width=10).shift(DOWN * 3.125).shift(LEFT * 6.5 * C) # 1/8
        bottomrect3 = Rectangle(width=2.0 * C, height=1.0, color=GRAY).shift(DOWN * 3.0).shift(LEFT * 3.5 * C) # 1/6
        bottomrect4 = Rectangle(width=2.0 * C, height=.75, color=PRIMARY, stroke_width=10).shift(DOWN * 3.125).shift(LEFT * 3.5 * C) # 1/8
        # bottomrect5 = Rectangle(width=2.0 * C, height=6.0/7.0, color=GRAY).shift(DOWN * 43.0 / 14.0).shift(LEFT * .5 * C) # 1/7
        # bottomrect6 = Rectangle(width=2.0 * C, height=.75, color=PRIMARY, stroke_width=10).shift(DOWN * 3.125).shift(LEFT * .5 * C) # 1/8
        bottomrect7 = Rectangle(width=2.0 * C, height=.75, color=PRIMARY, stroke_width=10).shift(DOWN * 3.125).shift(RIGHT * 2.5 * C) # 1/8
        bottomrect8 = Rectangle(width=2.0 * C, height=3.0, color=PRIMARY, stroke_width=10).shift(DOWN * 2.0).shift(RIGHT * 6.5 * C) # 1/2
        
        bottomtext1 = MathTex(r"\mathbf{\frac{1}{2^{n+1}}}", color=PRIMARY).move_to(bottomrect2.get_center()).scale(.5)
        bottomtext2 = MathTex(r"\mathbf{\frac{1}{2^{n+1}}}", color=PRIMARY).move_to(bottomrect4.get_center()).scale(.5)
        # bottomtext3= MathTex(r"\mathbf{\frac{1}{8}}", color=PRIMARY).move_to(bottomrect6.get_center()).scale(.5)
        bottomtext4 = MathTex(r"\mathbf{\frac{1}{2^{n+1}}}", color=PRIMARY).move_to(bottomrect7.get_center()).scale(.5)
        bottomtext5 = MathTex(r"\mathbf{\frac{1}{2}}", color=PRIMARY).move_to(bottomrect8.get_center())

        eq5 = MathTex(r"+").shift(LEFT * 5 * C).shift(DOWN * 3.125)
        eq6 = MathTex(r"+").shift(LEFT * 2 * C).shift(DOWN * 3.125)
        dotdotdot2 = MathTex(r"...").shift(LEFT * .5 * C).shift(DOWN * 3.25)
        eq7 = MathTex(r"+").shift(RIGHT * C).shift(DOWN * 3.125)
        eq8 = MathTex(r"=").shift(RIGHT * 4.5 * C).shift(DOWN * 3.125)

        brace = BraceBetweenPoints([-7.5 * C, 1.7, 0], [3.5 * C, 1.7, 0], [0, 1, 0])
        bracelabel = MathTex(r"2^n\text{ keer}").shift(LEFT * 2.0 * C).shift(UP * 2.75)

        self.add(toprect1, toprect2, toprect4, toprect5)
        self.add(toptext1, toptext2, toptext4, toptext5)
        self.add(eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8)
        self.add(bottomrect1, bottomrect2, bottomrect3, bottomrect4, bottomrect7, bottomrect8)
        self.add(geq1, geq2, geq3, geq4)
        self.add(bottomtext1, bottomtext2, bottomtext4, bottomtext5)
        self.add(dotdotdot1, dotdotdot2, brace, bracelabel)

class Slide9(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        WIDTH = 12.0
        HEIGHT = 5.0
        n = 8
        corners = []

        for i in range(1, n + 2):
            rect = Rectangle(width=WIDTH/n, height=HEIGHT/i).shift(LEFT * (WIDTH * .5 + .5 * WIDTH / n - i * WIDTH / n)).shift(DOWN * (HEIGHT - .5 - .5 * HEIGHT / i)).shift(UP)
            corners.append(rect.get_corner(UL))
            corners.append(rect.get_corner(UR))
            if i == 1:
                text = MathTex(r"1").move_to(rect)
            else:
                text = MathTex(r"\frac{1}{" + str(i) + r"}").move_to(rect)
                if i > 2:
                    text.scale(3 / i)
            self.add(rect, text)

class Slide10(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        WIDTH = 12.0
        HEIGHT = 5.0
        n = 8
        corners = []

        for i in range(1, n + 2):
            rect = Rectangle(width=WIDTH/n, height=HEIGHT/i).shift(LEFT * (WIDTH * .5 + .5 * WIDTH / n - i * WIDTH / n)).shift(DOWN * (HEIGHT - .5 - .5 * HEIGHT / i)).shift(UP)
            corners.append(rect.get_corner(UL))
            corners.append(rect.get_corner(UR))
            if i == 1:
                text = MathTex(r"1").move_to(rect)
            else:
                text = MathTex(r"\frac{1}{" + str(i) + r"}").move_to(rect)
                if i > 2:
                    text.scale(3 / i)
            self.add(rect, text)
        brace1 = BraceBetweenPoints(corners[0], corners[1], direction=[0, 1, 0])
        brace2 = BraceBetweenPoints(corners[2], corners[3], direction=[0, 1, 0])
        brace3 = BraceBetweenPoints(corners[4], [corners[7][0], corners[4][1], 0], direction=[0, 1, 0])
        brace4 = BraceBetweenPoints(corners[8], [corners[16][0], corners[8][1], 0], direction=[0, 1, 0])

        geq1 = MathTex(r"\geq\frac{1}{2}").move_to(brace1).shift(UP * .75)
        geq2 = MathTex(r"\geq\frac{1}{2}").move_to(brace2).shift(UP * .75)
        geq3 = MathTex(r"\geq\frac{1}{2}").move_to(brace3).shift(UP * .75)
        geq4 = MathTex(r"\geq\frac{1}{2}").move_to(brace4).shift(UP * .75)
        self.add(brace1, brace2, brace3, brace4, geq1, geq2, geq3, geq4)

class Slide11(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND

        WIDTH = 12.0
        HEIGHT = 5.0
        n = 8
        corners = []

        for i in range(1, n + 2):
            rect = Rectangle(width=WIDTH/n, height=HEIGHT/i).shift(LEFT * (WIDTH * .5 + .5 * WIDTH / n - i * WIDTH / n)).shift(DOWN * (HEIGHT - .5 - .5 * HEIGHT / i)).shift(UP)
            corners.append(rect.get_corner(UL))
            corners.append(rect.get_corner(UR))
            if i == 1:
                text = MathTex(r"1").move_to(rect)
            else:
                text = MathTex(r"\frac{1}{" + str(i) + r"}").move_to(rect)
                if i > 2:
                    text.scale(3 / i)
            self.add(rect, text)
        brace1 = BraceBetweenPoints(corners[0], corners[1], direction=[0, 1, 0])
        brace2 = BraceBetweenPoints(corners[2], corners[3], direction=[0, 1, 0])
        brace3 = BraceBetweenPoints(corners[4], [corners[7][0], corners[4][1], 0], direction=[0, 1, 0])
        brace4 = BraceBetweenPoints(corners[8], [corners[16][0], corners[8][1], 0], direction=[0, 1, 0])

        geq1 = MathTex(r"\geq\frac{1}{2}").move_to(brace1).shift(UP * .75)
        geq2 = MathTex(r"\geq\frac{1}{2}").move_to(brace2).shift(UP * .75)
        geq3 = MathTex(r"\geq\frac{1}{2}").move_to(brace3).shift(UP * .75)
        geq4 = MathTex(r"\geq\frac{1}{2}").move_to(brace4).shift(UP * .75)
        self.add(brace1, brace2, brace3, brace4, geq1, geq2, geq3, geq4)

        eq = MathTex(r"&1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+...\\\geq&\frac{1}{2}+\frac{1}{2}+\frac{1}{2}+...\text{ divergeert}").to_edge(UR)
        self.add(eq)