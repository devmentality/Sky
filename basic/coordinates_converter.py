import math
from .geometry import (
    EPS, Point3d,
    from_degrees_to_radians, from_radians_to_degrees)
from math import sin, cos


def from_equatorial_to_horizontal(alpha, delta, phi, star_time):
    rad_delta = from_degrees_to_radians(delta)
    rad_phi = from_degrees_to_radians(phi)
    rad_t = from_degrees_to_radians(star_time - alpha)

    rad_z = math.acos(sin(rad_delta) * sin(rad_phi) +
                      cos(rad_delta) * cos(rad_phi) * cos(rad_t))

    if math.fabs(rad_z) < EPS:
        return 0.0, 90.0

    sin_a = cos(rad_delta) * sin(rad_t) / sin(rad_z)
    cos_a = (-cos(rad_phi) * sin(rad_delta) +
             sin(rad_phi) * cos(rad_delta) * cos(rad_t)) / sin(rad_z)

    rad_a = math.atan2(sin_a, cos_a)

    return (from_radians_to_degrees(rad_a),
            90 - from_radians_to_degrees(rad_z))


def from_horizontal_to_cartesian(a, h, r):
    rad_a = from_degrees_to_radians(a)
    rad_h = from_degrees_to_radians(h)

    x = r * sin(rad_a) * cos(rad_h)
    y = r * cos(rad_a) * cos(rad_h)
    z = r * sin(rad_h)
    return Point3d(x, y, z)


def from_equatorial_to_cartesian(alpha, delta, phi, star_time, r):
    return from_horizontal_to_cartesian(
        *from_equatorial_to_horizontal(alpha, delta, phi, star_time), r)
