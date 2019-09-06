class CameraActions:
    MOVE_UP = 0
    MOVE_RIGHT = 1
    MOVE_DOWN = 2
    MOVE_LEFT = 3

    ZOOM_IN = 4
    ZOOM_OUT = 5


class CameraController:
    move_offset = 1
    zoom_offset = 1

    def __init__(self, camera):
        self.camera = camera

        self.actions = {
            CameraActions.MOVE_RIGHT: self._move_right,
            CameraActions.MOVE_UP: self._move_up,
            CameraActions.MOVE_DOWN: self._move_down,
            CameraActions.MOVE_LEFT: self._move_left,
            CameraActions.ZOOM_IN: self._zoom_in,
            CameraActions.ZOOM_OUT: self._zoom_out
        }

    def do_action(self, action):
        if action in self.actions:
            self.actions[action]()
        else:
            raise ValueError("Action is not supported.")

    def _move_up(self):
        if self.camera.height < 90 - CameraController.move_offset:
            self.camera.height += CameraController.move_offset

    def _move_right(self):
        self.camera.azimuth = (self.camera.azimuth + CameraController.move_offset) % 360

    def _move_down(self):
        if self.camera.height > CameraController.move_offset:
            self.camera.height -= CameraController.move_offset

    def _move_left(self):
        self.camera.azimuth -= CameraController.move_offset
        if self.camera.azimuth < 0:
            self.camera.azimuth += 360

    def _zoom_out(self):
        if self.camera.angle <= 180 - CameraController.zoom_offset:
            self.camera.angle += CameraController.zoom_offset

    def _zoom_in(self):
        if self.camera.angle >= 1 + CameraController.zoom_offset:
            self.camera.angle -= CameraController.zoom_offset
