from PyQt5 import QtWidgets, QtCore

from projecting.scene_builder import SceneBuilder
from rendering.stars_renderer import StarsRenderer
from .camera_controller import CameraController, CameraActions


class AppWindow(QtWidgets.QWidget):
    camera_action_by_key = {
        QtCore.Qt.Key_Up: CameraActions.MOVE_UP,
        QtCore.Qt.Key_Right: CameraActions.MOVE_RIGHT,
        QtCore.Qt.Key_Down: CameraActions.MOVE_DOWN,
        QtCore.Qt.Key_Left: CameraActions.MOVE_LEFT,
        QtCore.Qt.Key_Minus: CameraActions.ZOOM_OUT,
        QtCore.Qt.Key_Plus: CameraActions.ZOOM_IN
    }

    def __init__(self, phi, star_time, camera, stars, height, width, parent=None):
        super().__init__(parent=parent)
        self.camera = camera
        self.stars = stars
        self.picture = QtWidgets.QLabel()
        self.info = QtWidgets.QLabel()
        self.camera_controller = CameraController(camera)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.picture)
        layout.addWidget(self.info)
        self.setLayout(layout)
        self.scene_builder = SceneBuilder(stars, phi, star_time)
        self.setWindowTitle("Sky")
        self.setFixedSize(width, height)

    def paintEvent(self, event):
        scene_identities = self.scene_builder.build_scene(self.camera)
        image = StarsRenderer.render(
            self.stars, scene_identities,
            self.camera.display_height, self.camera.display_width)
        self.picture.setPixmap(image)
        self.info.setText("Azimuth: {0}, Height: {1}, Angle: {2}".format(
            self.camera.azimuth, self.camera.height, self.camera.angle))

    def keyPressEvent(self, event):
        if event.key() in self.camera_action_by_key:
            self.camera_controller.do_action(self.camera_action_by_key[event.key()])
            self.update()

    def showEvent(self, event):
        self.grabKeyboard()

    def hideEvent(self, event):
        self.releaseKeyboard()
