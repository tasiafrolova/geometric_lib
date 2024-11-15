import unittest
import triangle
import math

class TestTriangle(unittest.TestCase):

 def test_triangle_area_valid_sides(self):
  """Checks the correct calculation of the triangle area with valid sides."""
  a = 3
  b = 4
  c = 5
  expected_area = 6
  result = triangle.area(a, b, c)
  self.assertEqual(result, expected_area)

 def test_triangle_perimeter_valid_sides(self):
  """Checks the correct calculation of the triangle perimeter with valid sides."""
  a = 3
  b = 4
  c = 5
  expected_perimeter = 12
  result = triangle.perimeter(a, b, c)
  self.assertEqual(result, expected_perimeter)

 def test_triangle_area_invalid_sides_not_triangle(self):
  """Checks that the function throws an exception if the sides do not form a triangle."""
  a = 1
  b = 2
  c = 5
  with self.assertRaises(ValueError):
   triangle.area(a, b, c) 

