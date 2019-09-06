import math
import basic.geometry as geometry


class Camera:
    EPS = 0.000001

    def __init__(self, a, h, angle, disp_width, disp_height):
        self.angle = angle
        self.display_width = disp_width
        self.display_height = disp_height
        self.azimuth = a
        self.height = h

    def _is_valid_angle(self, angle):
        return self.EPS <= angle <= 180
