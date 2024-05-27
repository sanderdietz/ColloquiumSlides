from manim import *

class Space(Scene):
    def draw_neighborhood(self, axes, a, b, epsilon):
        dot = Dot(axes.c2p(a, b, 0), color=RED, radius=.125)

        bottom_boundary = max(b - epsilon, -1)
        top_boundary = min(b + epsilon, 1)

        bottom_point = axes.c2p(a, bottom_boundary)
        top_point = axes.c2p(a, top_boundary)

        line_segment = Line(bottom_point, top_point, color=TEAL, stroke_width=10)
        if bottom_boundary == -1:
            bottom = Line(bottom_point + LEFT * .125, bottom_point + RIGHT * .125, stroke_color=TEAL, stroke_width=10)
        else:
            bottom = Arc(radius=.125, start_angle=PI, angle=PI, arc_center=bottom_point+UP*.125, stroke_color=TEAL, stroke_width=10)
        
        if top_boundary == 1:
            top = Line(top_point + LEFT * .125, top_point + RIGHT * .125, stroke_color=TEAL, stroke_width=10)
        else:
            top = Arc(radius=.125, start_angle=0, angle=PI, arc_center=top_point+DOWN*.125, stroke_color=TEAL, stroke_width=10)

        curve_left = axes.plot(lambda x: np.sin(1 / (x - a)), x_range=[-1, -.001, .001], stroke_width=3, stroke_color=GRAY)
        curve_right = axes.plot(lambda x: np.sin(1 / (x - a)), x_range=[.001, 1, .001], stroke_width=3, stroke_color=GRAY)

        self.add(curve_left, curve_right)
        
        n = 20
        top_intersections = []
        bottom_intersections = []

        for i in range(-n, n + 1):
            x = a + 1 / (np.arcsin(top_boundary) + i * TAU)
            print(x)
            if abs(x - a) < epsilon and abs(x) < 1:
                top_intersections.append((x, top_boundary))
            
            x = a + 1 / (PI - np.arcsin(top_boundary) + i * TAU)
            if abs(x - a) < epsilon and abs(x) < 1:
                top_intersections.append((x, top_boundary))
            
            x = a + 1 / (np.arcsin(bottom_boundary) + i * TAU)
            if abs(x - a) < epsilon and abs(x) < 1:
                bottom_intersections.append((x, bottom_boundary))
            
            x = a + 1 / (PI - np.arcsin(bottom_boundary) + i * TAU)
            if abs(x - a) < epsilon and abs(x) < 1:
                bottom_intersections.append((x, bottom_boundary))

        top_intersections.sort(key=lambda v: v[0])
        bottom_intersections.sort(key=lambda v: v[0])

        for i in range(len(top_intersections)):
            self.add(Polygon(
                axes.c2p(top_intersections[i][0], 1),
                axes.c2p(top_intersections[i][0], -1),
                axes.c2p(bottom_intersections[i][0], -1),
                axes.c2p(bottom_intersections[i][0], 1),
                color=PURPLE,
                fill_color=PURPLE,
                fill_opacity=.5
            )) 

        self.add(line_segment, bottom, top)
        self.add(dot)

    def construct(self):
        axes = Axes(
            x_range=[-1, 1],
            y_range=[-1, 1], 
            tips=False,
            x_length=6,
            y_length=6,
            axis_config={"color": GRAY}
        )
        self.add(axes)

        self.draw_neighborhood(axes, -.75, .95, .15)
        