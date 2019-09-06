import re
from .star_description import StarDescription


class StarDescriptionParser:
    @classmethod
    def parse(cls, record, N):
        alpha = cls._from_time_to_angle(
            *map(float, record["ALF"].split(':'))
        )

        delta = cls._calculate_angle(
            *map(float, record["DEL"].split(':'))
        )

        return StarDescription(alpha, delta,
                               cls._get_color_from_spectre(record["SP"]),
                               float(record["M"]))

    @staticmethod
    def _calculate_angle(degrees, mins, secs):
        return degrees + mins / 60 + secs / 3600

    @staticmethod
    def _from_time_to_angle(hours, mins, secs):
        koeff = 360 / (24 * 3600)
        return (hours * 60 * 60 + mins * 60 + secs) * koeff

    @staticmethod
    def _get_color_from_spectre(spectre):
        colors = {
            'O': (170, 191, 255),
            'B': (202, 215, 255),
            'A': (248, 247, 255),
            'F': (248, 247, 255),
            'G': (255, 242, 161),
            'K': (255, 228, 111),
            'M': (255, 160, 64),
            'C': (255, 50, 20),
            'S': (255, 30, 10)
        }
        r = re.compile(".{3}([OBAFGKMCS]).*")
        result = r.fullmatch(spectre)
        if result is None:
            return 255, 0, 0
        return colors[result.group(1)]
