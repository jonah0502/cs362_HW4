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





    @unittest.expectedFailure
    def test_average_1(self):
        self.assertEqual(code.Average([]), 0)
        
    @unittest.expectedFailure
    def test_average_2(self):
        self.assertEqual(code.Average(["a", "b", "c"]), TypeError())
    
    @unittest.expectedFailure
    def test_average_3(self):
        self.assertEqual(code.Average(["1", "2", "3"]), TypeError())





    @unittest.expectedFailure
    def test_name_1(self):
        self.assertEqual(code.fullName(1, 2), TypeError())

    def test_name_2(self):
        self.assertEqual(code.fullName("1", "2"), "1 2")

    def test_name_3(self):
        self.assertEqual(code.fullName(" ", " "), "   ")

if __name__ == "__main__":
    unittest.main(verbosity=2)