def addOne(number):
    if isinstance(number, (int, float)):
        return number + 1
    else:
        raise TypeError("The input must be a number")
    
import unittest

from . import addOneUT

class TestAddOne 

def test_positive(self)
    
    self.assertEqual(addOne(1), 2)

def test_negative(self):

    self.assertNotEqual(addOne(1, 3))

if_name_=="_main_":
    unittest.main()