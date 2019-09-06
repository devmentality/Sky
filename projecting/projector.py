import math
from basic.geometry import (
    Vector3d, Point3d, Plate3d, EPS, Point2d,
    from_degrees_to_radians)


class Projector:
    def __init__(self, view_vector, view_angle):
        self.view_angle = view_angle
        self.view_vector = view_vector

        view_vector_to_plate = math.cos(
            from_degrees_to_radians(self.view_angle / 2)) * self.view_vector

        self.plate_point = Point3d(view_vector_to_plate.x,
                                   view_vector_to_plate.y,
                                   view_vector_to_plate.z)

        self.view_plate = Projector._get_normal_plate(
            self.view_vector, self.plate_point)
        self.center = self._get_projecting_center()
        self.base1, self.base2 = \
            Projector._get_planes_horizontal_cartesian_basis(self.view_plate)
        self.base1, self.base2 = \
            Projector._transform_basis_to_display_variant(
                self.base1, self.base2, self.view_vector)

    def project_point_on_view_plate(self, point):
        """
            point: point to project in cartesian basis
        """
        projected_point = \
            Projector._get_central_projection_on_plate(self.center, point, self.view_plate)
        if projected_point:
            return Projector._convert_3d_to_2d(
                self.plate_point, self.base1, self.base2, projected_point)

        return None

    def _get_projecting_center(self):
        """
            projecting center is placed that we can see a sphere segment from 90 degrees
        """
        circle_rad = math.sin(from_degrees_to_radians(self.view_angle / 2))
        vector_to_circle_center = Point3d(0, 0, 0).get_vector_to(self.plate_point)

        vector_to_proj_center = (-1) * self.view_vector * circle_rad
        return Point3d(vector_to_circle_center.x + vector_to_proj_center.x,
                       vector_to_circle_center.y + vector_to_proj_center.y,
                       vector_to_circle_center.z + vector_to_proj_center.z)

    @staticmethod
    def _get_normal_plate(n_vec, point):
        d = -(n_vec.x * point.x + n_vec.y * point.y + n_vec.z * point.z)
        return Plate3d(n_vec.x, n_vec.y, n_vec.z, d)

    @staticmethod
    def _get_central_projection_on_plate(center, point, plate):
        k = plate.a * (point.x - center.x) + plate.b * (point.y - center.y) + plate.c * (point.z - center.z)
        if math.fabs(k) < EPS:
            if math.fabs(plate.d) < EPS:
                return point
            return None

        t = (-plate.d - plate.a * center.x - plate.b * center.y - plate.c * center.z) / k
        if t < 0:
            return None

        return Point3d(center.x + t * (point.x - center.x),
                       center.y + t * (point.y - center.y),
                       center.z + t * (point.z - center.z))

    @staticmethod
    def _get_planes_horizontal_cartesian_basis(plate):
        # horizontal means vz1 = 0
        if plate.a == 0 and plate.b == 0:
            return Vector3d(1, 0, 0), Vector3d(0, 1, 0)

        if plate.a == 0 and plate.c == 0:
            return Vector3d(1, 0, 0), Vector3d(0, 0, -1)

        v1 = Vector3d(plate.b, -plate.a, 0)

        if plate.a != 0 and plate.b != 0:
            p = (plate.a ** 2 + plate.b ** 2)
            v2 = Vector3d(
                -plate.c + plate.b ** 2 * plate.c / p,
                -plate.a * plate.b * plate.c / p,
                plate.a
            )
        elif plate.b != 0:
            v2 = Vector3d(0, plate.c, -plate.b)
        else:
            v2 = Vector3d(plate.c, 0, -plate.a)

        return v1.normalized(), v2.normalized()

    @staticmethod
    def _transform_basis_to_display_variant(base1, base2, normal_vec):
        new_base2 = base2
        if base2.z > 0:
            new_base2 = -1 * base2

        new_base1 = base1
        if Vector3d.mixed_product(new_base1, new_base2, normal_vec) < 0:
            new_base1 = -1 * base1
        return new_base1, new_base2

    @staticmethod
    def _convert_3d_to_2d(origin, base1, base2, point):
        r_vector = origin.get_vector_to(point)
        if math.fabs(base1.x * base2.y - base1.y * base2.x) > EPS:
            v1, v2, t = base1.x, base2.x, r_vector.x
            u1, u2, s = base1.y, base2.y, r_vector.y
        elif math.fabs(base1.x * base2.z - base1.z * base2.x) > EPS:
            v1, v2, t = base1.x, base2.x, r_vector.x
            u1, u2, s = base1.z, base2.z, r_vector.z
        elif math.fabs(base1.y * base2.z - base1.z * base2.y) > EPS:
            v1, v2, t = base1.y, base2.y, r_vector.y
            u1, u2, s = base1.z, base2.z, r_vector.z
        else:
            return None

        det = u2 * v1 - v2 * u1
        a = (t * u2 - s * v2) / det
        b = (s * v1 - t * u1) / det

        return Point2d(a, b)
