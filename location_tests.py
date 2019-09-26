import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(repr(loc),"Location('Paris', 35.3, -120.7)")

    def test_eq_false(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertFalse(loc1 == loc2)

    def test_eq_true(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc1 == loc2)

    def test_eq_true2(self):
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc1 == loc1)

    def test_eq_false_none1(self):
        loc1 = None
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertFalse(loc1 == loc2)

    def test_eq_false_none2(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = None
        self.assertFalse(loc1 == loc2)


    # Add more tests!

if __name__ == "__main__":
        unittest.main()
