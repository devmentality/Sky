from PyQt5 import QtGui


class StarsRenderer:
    @classmethod
    def render(cls, stars, identified_coords, display_height, display_width):
        image = QtGui.QPixmap(display_width, display_height)

        painter = QtGui.QPainter(image)
        painter.setBrush(QtGui.QColor(0, 0, 0))
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        painter.drawRect(0, 0, display_width, display_height)

        for identified_coord in identified_coords:
            color = stars[identified_coord.identity].color
            painter.setPen(QtGui.QColor(color[0], color[1], color[2]))
            painter.setBrush(QtGui.QColor(color[0], color[1], color[2]))
            painter.drawEllipse(identified_coord.coordinates.x,
                                identified_coord.coordinates.y, 3, 3)

        return image
