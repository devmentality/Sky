import os
import sys
import unittest
import datetime


sys.path.append(
    os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)), os.path.pardir))

import basic.time_handling as time_handling


class TestTimeHandling(unittest.TestCase):
    def test_any_data(self):
        st = time_handling.calculate_star_time_in_seconds(
            datetime.datetime(2010, 1, 20, 20, 30, 0), -3, 50 + 37/60)

        h = st // 3600
        m = st % 3600 // 60

        self.assertEqual(10, h)
        self.assertAlmostEqual(53, m, delta=3)


if __name__ == "__main__":
    unittest.main()