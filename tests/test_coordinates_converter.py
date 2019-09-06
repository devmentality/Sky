import os
import sys
import math
import unittest

sys.path.append(
    os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), os.path.pardir))

import basic.coordinates_converter as converter
import basic.geometry as geometry

class CoordinatesConverterTest(unittest.TestCase):
    EPS = 0.0001

    def test_from_equatorial_to_horizontal_top_point(self):
        phi = 30.0
        alpha = 0.0
        delta = phi

        a, h = converter.from_equatorial_to_horizontal(alpha, delta, phi, 0)

        self.assertAlmostEqual(h, 90.0, delta=self.EPS)

    def test_from_equatorial_to_horizontal_ordinary(self):
        phi = 45
        alpha = 30
        delta = 18

        expected_h = 53.216974931
        expected_a = -52.575372956

        a, h = converter.from_equatorial_to_horizontal(alpha, delta, phi, 0)

        self.assertAlmostEqual(expected_h, h, delta=self.EPS)
        self.assertAlmostEqual(expected_a, a, delta=self.EPS)

    def test_from_horizontal_to_cartesian(self):
        a, h, r = 45, 45, 7
        expected_point = geometry.Point3d(3.5, 3.5, 3.5 * math.sqrt(2))

        actual_point = converter.from_horizontal_to_cartesian(a, h, r)

        self.assertAlmostEqual(actual_point.x, expected_point.x, delta=self.EPS)
        self.assertAlmostEqual(actual_point.y, expected_point.y, delta=self.EPS)


if __name__ == "__main__":
    unittest.main()
