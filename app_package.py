import os
import sys
from PyQt5 import QtWidgets
from args_parsing.package_args_parser import PackageArgsParser
from projecting.camera import Camera
from data.database_reader import DatabaseReader
from projecting.scene_builder import SceneBuilder
from rendering.stars_renderer import StarsRenderer
from basic import time_handling as th

if __name__ == "__main__":
    parser = PackageArgsParser()
    args = parser.parse()

    stars = DatabaseReader.read(
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), args.database))

    if args.filter:
        stars = [star for star in stars if star.visual_size < args.filter]

    app = QtWidgets.QApplication(sys.argv)

    width = args.size.width
    height = args.size.height

    cam = Camera(args.azimuth, args.height, args.angle, width, height)
    dt, tz = args.datetime
    star_time = th.time_in_seconds_to_degrees(
        th.calculate_star_time_in_seconds(
            dt, tz, args.long))

    scene_builder = SceneBuilder(stars, args.lat, star_time)

    scene_identities = scene_builder.build_scene(cam)
    image = StarsRenderer.render(
        stars, scene_identities, cam.display_height, cam.display_width)

    image.save(args.filename)