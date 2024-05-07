from manim import *
from Helper import *

def mobius_func(u, v):
    x = (1 + v / 2 * np.cos(u / 2)) * np.cos(u)
    y = (1 + v / 2 * np.cos(u / 2)) * np.sin(u)
    z = v / 2 * np.sin(u / 2)
    return np.array((x, y, z))

class Image01(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.set_camera_orientation(phi=50*DEGREES, theta=330*DEGREES, zoom=2.2)
        mobius = Surface(
            mobius_func,
            u_range=[0, 2 * PI],
            v_range=[-1, 1],
            resolution=(64, 16),
        )
        mobius.set_color(PRIMARY)
        self.add(mobius)