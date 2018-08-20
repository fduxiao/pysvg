import unittest
from pysvg.geometry import *
import math


class TestGeometry(unittest.TestCase):
    def test_unit(self):
        self.assertAlmostEquals(90*deg, deg*90, deg(90))
        ninety_degree = 90 * deg
        self.assertAlmostEquals(math.sin(ninety_degree), 1)


if __name__ == '__main__':
    unittest.main()
