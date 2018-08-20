import unittest
import os
from pysvg.svg import *


class TestXmlRepr(unittest.TestCase):
    def test_xml_repr(self):
        @xml_repr
        class TestClass:
            def __init__(self, name):
                self.name = name

            def xml(self):
                return self.name
        random_name = str(os.urandom(10))
        test_instance = TestClass(random_name)
        self.assertEqual(test_instance.__repr__(), random_name)


if __name__ == '__main__':
    unittest.main()
