import unittest
import main as code
import math

class TestCase(unittest.TestCase):
    def test_volume_1(self):
        self.assertEqual(code.calcVolume(-3), 27)
    @unittest.expectedFailure
    def test_volume_2(self):
        self.ass(code.calcVolume("a"), 97**3)
    @unittest.expectedFailure
    def test_volume_3(self):
        self.assertEqual(code.calcVolume(math.sqrt(-1)), 1)
if __name__ == "__main__":
    unittest.main(verbosity=2)