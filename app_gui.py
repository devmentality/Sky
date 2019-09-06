import os
import sys
from PyQt5 import QtWidgets
from gui.app_window import AppWindow
from args_parsing.gui_args_parser import GuiArgsParser
from projecting.camera import Camera
from data.database_reader import DatabaseReader
from basic import time_handling as th

if __name__ == "__main__":
    parser = GuiArgsParser()
    args = parser.parse()

    stars = DatabaseReader.read(
        os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)), args.database))

    if args.filter:
        stars = [star for star in stars if star.visual_size < args.filter]

    app = QtWidgets.QApplication(sys.argv)

    if args.display.is_full:
        scr = app.desktop().screenGeometry()
        width = scr.width()
        height = scr.height()
    else:
        width = args.display.width
        height = args.display.height

    cam = Camera(args.azimuth, args.height, args.angle, width, height)
    dt, tz = args.datetime
    star_time = th.time_in_seconds_to_degrees(
        th.calculate_star_time_in_seconds(
            dt, tz, args.long))

    window = AppWindow(args.lat, star_time, cam, stars, height, width)
    window.show()
    sys.exit(app.exec_())
