import os
import sys
import math
import unittest


sys.path.append(
    os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), os.path.pardir))

import basic.geometry as geometry


class TestGeometry(unittest.TestCase):
    def test_from_radians_to_degrees(self):
        angle_in_degrees = geometry.from_radians_to_degrees(math.pi / 2)
        self.assertAlmostEqual(angle_in_degrees, 90.0, delta=geometry.EPS)

    def test_from_degrees_to_radians(self):
        angle_in_radians = geometry.from_degrees_to_radians(270.0)
        self.assertAlmostEqual(angle_in_radians, 3 / 2 * math.pi, delta=geometry.EPS)

    def test_vector3d_add(self):
        v1 = geometry.Vector3d(10, 10, 20)
        v2 = geometry.Vector3d(5, 3, 10)
        v_sum = v1 + v2
        self.assertEqual(v_sum.x, v1.x + v2.x)
        self.assertEqual(v_sum.y, v1.y + v2.y)
        self.assertEqual(v_sum.z, v1.z + v2.z)

    def test_vector3d_sub(self):
        v1 = geometry.Vector3d(10, 10, 20)
        v2 = geometry.Vector3d(5, 3, 10)
        v_sum = v1 - v2
        self.assertEqual(v_sum.x, v1.x - v2.x)
        self.assertEqual(v_sum.y, v1.y - v2.y)
        self.assertEqual(v_sum.z, v1.z - v2.z)

    def test_vector3d_mul(self):
        v = geometry.Vector3d(10, 5, 20)
        k = 3
        scaled_v = v * k
        self.assertEqual(scaled_v.x, v.x * k)
        self.assertEqual(scaled_v.y, v.y * k)
        self.assertEqual(scaled_v.z, v.z * k)

    def test_vector3d_rmul(self):
        v = geometry.Vector3d(10, 5, 20)
        k = 3
        scaled_v = k * v
        self.assertEqual(scaled_v.x, v.x * k)
        self.assertEqual(scaled_v.y, v.y * k)
        self.assertEqual(scaled_v.z, v.z * k)

    def test_vector3d_scalar_prod(self):
        v1 = geometry.Vector3d(10, 10, 20)
        v2 = geometry.Vector3d(5, 3, 10)
        prod = v1.scalar_prod(v2)
        self.assertEqual(prod, 280)

    def test_vector3d_mixed_prod(self):
        v1 = geometry.Vector3d(1, 2, 3)
        v2 = geometry.Vector3d(5, 4, 3)
        v3 = geometry.Vector3d(1, 0, 2)
        prod = geometry.Vector3d.mixed_product(v1, v2, v3)
        self.assertEqual(prod, -18)

    def test_vector3d_length(self):
        v1 = geometry.Vector3d(1, 2, 3)
        length = v1.length()
        self.assertAlmostEqual(length, math.sqrt(14), geometry.EPS)

    def test_point3d_get_vector_to(self):
        p = geometry.Point3d(0, 1, 3)
        v = p.get_vector_to(geometry.Point3d(2, 1, 2))
        self.assertEqual(v.x, 2)
        self.assertEqual(v.y, 0)
        self.assertEqual(v.z, -1)


if __name__ == "__main__":
    unittest.main()