import unittest
import addOneUT

# def addOne(target):
#     return target +1


class test_addOne(unittest.TestCase):

    def test_addOnePass(self):
        self.assertEqual(addOneUT.addOne(2), 3)
    
    @unittest.expectedFailure
    def test_addOneFail(self):
        self.assertEqual(addOneUT.addOne(2), 4)


if __name__ == '__main__':
    unittest.main()