import unittest
from src.scheduler import max_appointments


class TestScheduler(unittest.TestCase):

    def test_non_overlapping(self):
        self.assertEqual(max_appointments([(9,10),(10,11),(11,12)]), 3)

    def test_overlapping(self):
        self.assertEqual(max_appointments([(9,11),(10,12),(11,13)]), 2)

    def test_mixed(self):
        self.assertEqual(max_appointments([(9,10),(9,12),(11,13),(12,14)]), 2)

    def test_nested(self):
        self.assertEqual(max_appointments([(9,15),(10,11),(11,12),(12,13)]), 3)

    def test_empty(self):
        self.assertEqual(max_appointments([]), 0)


if __name__ == "__main__":
    unittest.main()