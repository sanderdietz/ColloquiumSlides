import numpy as np

def linear_points(x1, y1, x2, y2):
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    return (a, b)

def linear_angles(r, angle1, angle2):
    y1 = r * np.sin(angle1)
    y2 = r * np.sin(angle2)
    x1 = r * np.cos(angle1)
    x2 = r * np.cos(angle2)
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    return (a, b)

def intersection(a1, b1, a2, b2):
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return (x, y, 0)