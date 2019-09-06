import argparse
from datetime import datetime


def latitude_handler(s_latitude):
    hemisphere = s_latitude[0]
    lat_parts = list(map(int, s_latitude[1:].split(':')))
    if len(lat_parts) != 3:
        raise argparse.ArgumentTypeError('wrong latitude format')

    if not (0 <= lat_parts[0] <= 90 and
            0 <= lat_parts[1] <= 60 and
            0 <= lat_parts[2] <= 60):
        raise argparse.ArgumentTypeError(
            'wrong latitude value')
    latitude = lat_parts[0] + lat_parts[1] / 60 + lat_parts[2] / 3600
    if latitude > 90:
        raise argparse.ArgumentTypeError('wrong latitude value')

    if hemisphere == 'N':
        return latitude
    elif hemisphere == 'S':
        return -latitude
    else:
        raise argparse.ArgumentTypeError('invalid hemisphere prefix')


def azimuth_handler(s_azimuth):
    azimuth = int(s_azimuth)
    if azimuth < 0 or azimuth > 360:
        raise argparse.ArgumentTypeError('azimuth should be between 0 and 360')
    return azimuth


def height_handler(s_height):
    height = int(s_height)
    if height < 0 or height > 90:
        raise argparse.ArgumentTypeError('height should be between 0 and 90')
    return height


def longitude_handler(s_longtitude):
    hemisphere = s_longtitude[0]
    long_parts = list(map(int, s_longtitude[1:].split(':')))
    if len(long_parts) != 3:
        raise argparse.ArgumentTypeError('wrong longtitude format')

    if not (0 <= long_parts[0] <= 180 and
            0 <= long_parts[1] <= 60 and
            0 <= long_parts[2] <= 60):
        raise argparse.ArgumentTypeError(
            'wrong longtitude value')
    longitude = long_parts[0] * 3600 + long_parts[1] * 60 + long_parts[2]
    if longitude > 180 * 3600:
        raise argparse.ArgumentTypeError('wrong longtitude value')

    if hemisphere == 'E':
        return longitude
    elif hemisphere == 'W':
        return -longitude
    else:
        raise argparse.ArgumentTypeError('invalid longtitude prefix')


def datetime_handler(s_datetime):
    arg_parts = s_datetime.split('/')
    if len(arg_parts) != 2:
        argparse.ArgumentTypeError('invalid datetime format')
    dt, tz = arg_parts
    return datetime.strptime(dt, '%Y-%m-%d_%H:%M:%S'), int(tz)


def get_current_time_and_timezone():
    current_time = datetime.now()
    tz = (datetime.now() - datetime.utcnow()).seconds // 3600
    return current_time, tz


class ArgumentsParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument(
            '--lat', required=True, type=latitude_handler,
            help="latitude of observer in format (N|S)A:MM:SS")
        self.parser.add_argument(
            '--long', required=True, type=longitude_handler,
            help="longitude of observer in format (W|E)A:MM:SS"
        )

        self.parser.add_argument(
            '--datetime', type=datetime_handler,
            help="local datetime in format YYYY-MM-DD_HH:MM:SS/timezone"
        )

        self.parser.add_argument(
            '--azimuth', required=True, type=azimuth_handler,
            help="azimuth of view point")
        self.parser.add_argument(
            '--height', required=True, type=height_handler,
            help="height of view point")

        self.parser.add_argument_group()

        self.parser.add_argument(
            '--filter', type=float,
            help="filter stars: do not show stars with apparent "
                 "magnitude more than given value"
        )

        self.parser.add_argument(
            '--angle', type=int, default=45,
            help="angle of view in degrees from 1 to 180"
        )

        self.parser.add_argument(
            '--database', default="bright.dbf",
            help="path to database from current directory"
        )

    def parse(self):
        parsed_args = self.parser.parse_args()
        if not parsed_args.datetime:
            parsed_args.datetime = get_current_time_and_timezone()

        return parsed_args
