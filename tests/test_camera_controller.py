import os
import sys
import unittest

sys.path.append(
    os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), os.path.pardir))

from projecting.camera import Camera
from gui.camera_controller import CameraController, CameraActions


class TestCameraController(unittest.TestCase):
    def _test_vertical_moves(self, action, init_height, final_height):
        camera = Camera(90, init_height, 30, 100, 100)
        camera_controller = CameraController(camera)
        camera_controller.do_action(action)

        self.assertEqual(final_height, camera.height)

    def test_move_up_when_able(self):
        self._test_vertical_moves(
            CameraActions.MOVE_UP, 10, 10 + CameraController.move_offset)

    def test_move_up_when_not_able(self):
        self._test_vertical_moves(CameraActions.MOVE_UP, 90, 90)

    def test_move_down_when_able(self):
        self._test_vertical_moves(
            CameraActions.MOVE_DOWN, 10, 10 - CameraController.move_offset)

    def test_move_down_when_not_able(self):
        self._test_vertical_moves(CameraActions.MOVE_DOWN, 0, 0)

    def _test_horizontal_moves(self, action, init_azimuth, final_azimuth):
        camera = Camera(init_azimuth, 30, 30, 100, 100)
        camera_controller = CameraController(camera)
        camera_controller.do_action(action)

        self.assertEqual(final_azimuth, camera.azimuth)

    def test_move_left_inside_circle(self):
        self._test_horizontal_moves(
            CameraActions.MOVE_LEFT, 10, 10 - CameraController.move_offset)

    def test_move_left_outside_circle(self):
        self._test_horizontal_moves(CameraActions.MOVE_LEFT, 0, 359)

    def test_move_right_inside_circle(self):
        self._test_horizontal_moves(
            CameraActions.MOVE_RIGHT, 10, 10 + CameraController.move_offset)

    def test_move_right_outside_circle(self):
        self._test_horizontal_moves(CameraActions.MOVE_RIGHT, 359, 0)

    def _test_zoom(self, action, init_angle, final_angle):
        camera = Camera(10, 30, init_angle, 100, 100)
        camera_controller = CameraController(camera)
        camera_controller.do_action(action)

        self.assertEqual(final_angle, camera.angle)

    def test_zoom_out_when_able(self):
        self._test_zoom(
            CameraActions.ZOOM_OUT, 10, 10 + CameraController.zoom_offset)

    def test_zoom_out_when_not_able(self):
        self._test_zoom(CameraActions.ZOOM_OUT, 180, 180)

    def test_zoom_in_when_able(self):
        self._test_zoom(
            CameraActions.ZOOM_IN, 10, 10 - CameraController.zoom_offset)

    def test_zoom_in_when_not_able(self):
        self._test_zoom(CameraActions.ZOOM_IN, 0, 0)


if __name__ == "__main__":
    unittest.main()