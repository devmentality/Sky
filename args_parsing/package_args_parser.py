from .common_args_parser import ArgumentsParser


class ImageSize:
    def __init__(self, format_string):
        self.width, self.height = map(int, format_string.split('x'))


class PackageArgsParser(ArgumentsParser):
    def __init__(self):
        super().__init__()

        self.parser.add_argument(
            '--filename', required=True,
            help='file name image will be saved to'
        )

        self.parser.add_argument(
            '--size', type=ImageSize, default=ImageSize('600x600'),
            help='image size in format (width)x(height)'
        )
