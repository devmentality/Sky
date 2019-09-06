import math

EPS = 0.00001


def from_degrees_to_radians(degrees):
    return degrees * math.pi / 180


def from_radians_to_degrees(radians):
    return radians * 180 / math.pi


class Vector3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3d(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3d(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, t):
        return Vector3d(t * self.x, t * self.y, t * self.z)

    def __rmul__(self, t):
        return self * t

    def scalar_prod(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def normalized(self):
        return 1 / self.length() * self

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    @staticmethod
    def mixed_product(v1, v2, v3):
        return (v1.x * (v2.y * v3.z - v2.z * v3.y) -
                v1.y * (v2.x * v3.z - v2.z * v3.x) +
                v1.z * (v2.x * v3.y - v3.x * v2.y))

    def is_zero(self):
        return self.length() < EPS


class Point3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_vector_to(self, other):
        return Vector3d(other.x - self.x, other.y - self.y, other.z - self.z)


class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Plate3d:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
