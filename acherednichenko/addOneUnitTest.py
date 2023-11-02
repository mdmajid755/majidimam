import unittest
from  addOne import add_one

class TestAddOne(unittest.TestCase):
    def test_addOne(self):
        self.assertEqual(add_one(3), 4)

    @unittest.expectedFailure
    def test_addOneWrongAssert(self):
        self.assertEqual(add_one(3), 2)