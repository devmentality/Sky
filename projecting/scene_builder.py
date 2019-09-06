import basic.coordinates_converter as Conv
from projecting.projector import Projector
import math
import basic.geometry as geometry


class IdentifiedCoordinates:
    def __init__(self, identity, coordinates):
        self.identity = identity
        self.coordinates = coordinates


class SceneBuilder:
    def __init__(self, stars, phi, star_time):
        self.stars = stars
        self.identities_in_cartesian = []
        for (index, star) in enumerate(stars):
            coordinates = Conv.from_equatorial_to_cartesian(
                        star.alpha, star.delta, phi, star_time, 1)
            self.identities_in_cartesian.append(
                IdentifiedCoordinates(index, coordinates))

    def build_scene(self, camera):
        view_point = Conv.from_horizontal_to_cartesian(
            camera.azimuth, camera.height, 1)
        projector = Projector(
            geometry.Point3d(0, 0, 0).get_vector_to(view_point), camera.angle)

        identities_on_plate = list(filter(
            lambda identity: identity.coordinates is not None,
            [
                IdentifiedCoordinates(
                    star.identity,
                    projector.project_point_on_view_plate(star.coordinates))
                for star in self.identities_in_cartesian
            ]
        ))
        identities_on_display = self.transform_to_display_coordinates(
            camera, identities_on_plate
        )

        identities_to_draw = list(
            filter(
                lambda p: (0 <= p.coordinates.x <= camera.display_width and
                           0 <= p.coordinates.y <= camera.display_height),
                identities_on_display))

        return identities_to_draw

    def transform_to_display_coordinates(self, camera, identities_on_plate):
        max_dimension = max(camera.display_width, camera.display_height)
        scale = max_dimension / \
                (2 * math.sin(
                    geometry.from_degrees_to_radians(camera.angle) / 2))
        return [
            IdentifiedCoordinates(
                star.identity,
                geometry.Point2d(
                    scale * star.coordinates.x + camera.display_width / 2,
                    scale * star.coordinates.y + camera.display_height / 2
                )
            )
            for star in identities_on_plate
        ]
