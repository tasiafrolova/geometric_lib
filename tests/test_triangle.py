import unittest
import triangle


class TestTriangle(unittest.TestCase):

    def test_triangle_area_valid_sides(self):
        a = 3
        b = 4
        c = 5
        expected_area = 6
        result = triangle.area(a, b, c)
        self.assertEqual(result, expected_area)

    def test_triangle_perimeter_valid_sides(self):
        a = 3
        b = 4
        c = 5
        expected_perimeter = 12
        result = triangle.perimeter(a, b, c)
        self.assertEqual(result, expected_perimeter)


if __name__ == '__main__':
    unittest.main()
