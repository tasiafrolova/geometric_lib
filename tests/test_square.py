import unittest
import square

class TestSquare(unittest.TestCase):

 def test_square_area_positive_side(self):
  """Checks the correct calculation of the square area with a positive side."""
  side = 4
  expected_area = 16
  result = square.area(side)
  self.assertEqual(result, expected_area)
  
  def test_square_area_zero_side(self):
    """Checks the correct calculation of the square area with a zero side."""
    side = 0
    expected_area = 0
    result = square.area(side)
    self.assertEqual(result, expected_area)
    
  def test_square_perimeter_positive_side(self):
    """Checks the correct calculation of the square perimeter with a positive side."""
    side = 4
    expected_perimeter = 16
    result = square.perimeter(side)
    self.assertEqual(result, expected_perimeter)
    
  def test_square_perimeter_zero_side(self):
    """Checks the correct calculation of the square perimeter with a zero side."""
    side = 0
    expected_perimeter = 0
    result = square.perimeter(side)
    self.assertEqual(result, expected_perimeter)
