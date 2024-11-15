import unittest
import calculate
import math


class TestCalculate(unittest.TestCase):

    def test_calc_invalid_triangle_sides(self):
        figure_type = "triangle"
        side1 = 1
        side2 = 2
        side3 = 5
        with self.assertRaises(AssertionError):
            calculate.calc(figure_type, "area", [side1, side2, side3])

    def test_calc_circle_area_correct_input(self):
        figure_type = "circle"
        radius = 5
        expected_area = math.pi * radius**2
        result = calculate.calc(figure_type, "area", [radius])
        self.assertEqual(result, expected_area)

    def test_calc_triangle_area_correct_input(self):
        figure_type = "triangle"
        side1 = 5
        side2 = 8
        side3 = math.sqrt(side1**2 + side2**2)
        expected_area = 20
        result = calculate.calc(figure_type, "area", [side1, side2, side3])
        self.assertAlmostEqual(result, expected_area, places=2)

    def test_calc_invalid_figure_type(self):
        figure_type = "invalid"
        radius = 5
        with self.assertRaises(AssertionError):
            calculate.calc(figure_type, "area", [radius])

    def test_calc_invalid_function_name(self):
        figure_type = "circle"
        radius = 5
        with self.assertRaises(AssertionError):
            calculate.calc(figure_type, "invalid", [radius])

    def test_calc_incorrect_number_of_arguments_circle(self):
        figure_type = "circle"
        radius = 5
        with self.assertRaises(AssertionError):
            calculate.calc(figure_type, "area", [radius, radius])

    def test_calc_incorrect_number_of_arguments_square(self):
        figure_type = "square"
        side = 5
        with self.assertRaises(AssertionError):
            calculate.calc(figure_type, "area", [side, side])

    def test_calc_incorrect_number_of_arguments_triangle(self):
        figure_type = "triangle"
        side1 = 5
        side2 = 8
        with self.assertRaises(AssertionError):
            calculate.calc(figure_type, "area", [side1, side2])

    def test_calc_negative_argument_circle(self):
        figure_type = "circle"
        radius = -5
        with self.assertRaises(AssertionError):
            calculate.calc(figure_type, "area", [radius])

    def test_calc_negative_argument_square(self):
        figure_type = "square"
        side = -5
        with self.assertRaises(AssertionError):
            calculate.calc(figure_type, "area", [side])

    def test_calc_negative_argument_triangle(self):
        figure_type = "triangle"
        side1 = 5
        side2 = 8
        with self.assertRaises(AssertionError):
            calculate.calc(figure_type, "area", [side1, side2, -math.sqrt(side1**2 + side2**2)])


if __name__ == '__main__':
    unittest.main()
