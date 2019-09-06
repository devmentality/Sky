import os
import sys
import unittest

sys.path.append(os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)), os.path.pardir))

import basic.geometry as geometry
from projecting.projector import Projector


class ProjectorTest(unittest.TestCase):
    EPS = 0.0001

    def test_get_central_projection_when_exists(self):
        center = geometry.Point3d(-2, 1, 3)
        point = geometry.Point3d(-1, 0, 5)
        plate = geometry.Plate3d(1, 2, 3, -10)

        result = Projector._get_central_projection_on_plate(center, point, plate)

        to_result = center.get_vector_to(result)
        to_point = center.get_vector_to(point)

        self.assertAlmostEqual(
            to_result.y * to_point.z - to_result.z * to_point.y, 0,
            delta=self.EPS)
        self.assertAlmostEqual(
            to_result.x * to_point.z - to_result.z * to_point.x, 0,
            delta=self.EPS)
        self.assertAlmostEqual(
            to_result.x * to_point.y - to_result.y * to_point.x, 0,
            delta=self.EPS)

        self.assertAlmostEqual(
            plate.a * result.x + 
            plate.b * result.y + 
            plate.c * result.z + 
            plate.d, 0, delta=self.EPS)

    def test_get_central_projection_none_when_opposite(self):
        center = geometry.Point3d(0, 0, 0)
        point = geometry.Point3d(-1, 0, 5)
        plate = geometry.Plate3d(1, 2, 3, 10)

        result = Projector._get_central_projection_on_plate(center, point, plate)

        self.assertIsNone(result)

    def test_get_central_projection_when_parallel(self):
        center = geometry.Point3d(0, 0, 0)
        point = geometry.Point3d(1, 0, 0)
        plate = geometry.Plate3d(0, 0, 1, 1)

        result = Projector._get_central_projection_on_plate(center, point, plate)

        self.assertIsNone(result)

    def test_get_plates_horizontal_cartesian_basis_ordinary(self):
        a, b, c, d = 10, 20, -5, 11
        plate = geometry.Plate3d(a, b, c, d)

        v1, v2 = Projector._get_planes_horizontal_cartesian_basis(plate)

        self.assertAlmostEqual(v1.length(), 1, delta=self.EPS)
        self.assertAlmostEqual(v2.length(), 1, delta=self.EPS)

        self.assertAlmostEqual(v1.z, 0, delta=self.EPS)

        self.assertAlmostEqual(v1.scalar_prod(v2), 0, delta=self.EPS)

        self.assertAlmostEqual(a * v1.x + b * v1.y + c * v1.z, 0, delta=self.EPS)
        self.assertAlmostEqual(a * v2.x + b * v2.y + c * v2.z, 0, delta=self.EPS)

    def test_convert_3d_to_2d(self):
        base1 = geometry.Vector3d(-1, -1, 0)
        base2 = geometry.Vector3d(-0.5, -0.5, 1)
        origin = geometry.Point3d(0.5, 0.5, 0)

        point = geometry.Point3d(-0.25, -0.25, 0.5)

        result = Projector._convert_3d_to_2d(origin, base1, base2, point)
        self.assertAlmostEqual(result.x, 0.5, delta=self.EPS)
        self.assertAlmostEqual(result.y, 0.5, delta=self.EPS)

    def test_project_point_when_exist(self):
        view_vector = geometry.Vector3d(0, 0, 1)
        projector = Projector(view_vector, 90)
        point = geometry.Point3d(0, 0, 0.5)

        actual_projection = projector.project_point_on_view_plate(point)
        expected_projection = geometry.Point2d(0, 0)

        self.assertAlmostEqual(actual_projection.x, expected_projection.x, delta=self.EPS)
        self.assertAlmostEqual(actual_projection.y, expected_projection.y, delta=self.EPS)


if __name__ == "__main__":
    unittest.main()
