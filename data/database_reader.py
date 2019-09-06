from dbfread import DBF
from .star_description_parser import StarDescriptionParser


class DatabaseReader:
    @staticmethod
    def read(name):
        return list(StarDescriptionParser.parse(record, index) for (index, record) in enumerate(DBF(name)))
