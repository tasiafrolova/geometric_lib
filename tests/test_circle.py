import unittest
import circle
import math

class TestCircle(unittest.TestCase):

    def test_circle_area_positive_radius(self):
        """Checks the correct calculation of the circle area with a positive radius."""
        radius = 5
        expected_area = math.pi * radius**2
        result = circle.area(radius)
        self.assertEqual(result, expected_area)

    def test_circle_area_zero_radius(self):
        """Checks the correct calculation of the circle area with a zero radius."""
        radius = 0
        expected_area = 0
        result = circle.area(radius)
        self.assertEqual(result, expected_area)

    def test_circle_perimeter_positive_radius(self):
        """Checks the correct calculation of the circle perimeter with a positive radius."""
        radius = 5
        expected_perimeter = 2 * math.pi * radius
        result = circle.perimeter(radius)
        self.assertEqual(result, expected_perimeter)

    def test_circle_perimeter_zero_radius(self):
        """Checks the correct calculation of the circle perimeter with a zero radius."""
        radius = 0
        expected_perimeter = 0
        result = circle.perimeter(radius)
        self.assertEqual(result, expected_perimeter)

if __name__ == '__main__':
    unittest.main()
