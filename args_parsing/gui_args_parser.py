from .common_args_parser import ArgumentsParser


class Display:
    def __init__(self, format_string):
        if format_string == 'full':
            self.height = self.width = 0
            self.is_full = True
        else:
            h, w = format_string.split('x')
            self.height = int(h)
            self.width = int(w)
            self.is_full = False


class GuiArgsParser(ArgumentsParser):
    def __init__(self):
        super().__init__()

        self.parser.add_argument(
            '--display', type=Display, default=Display('600x600'),
            help="display settings in format (height)x(width) or full - full screen mode"
        )
