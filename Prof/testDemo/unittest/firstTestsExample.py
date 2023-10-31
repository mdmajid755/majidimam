
import unittest
import func


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.testVal = 1
    
    def test_FuncFail(self):
        try:
            self.testVal = 2
            self.assertEqual(func.func(self.testVal), 2)
        except AssertionError:
            print("expected exception caught")
        else:
            raise Exception("failed")
        
    @unittest.expectedFailure
    def test_DecoractedFuncFail(self):
            self.testVal = 2
            self.assertEqual(func.func(self.testVal), 2)

        
    def test_FuncPass(self):
        self.assertEqual(func.func(self.testVal), 2)

if __name__ == '__main__':
    unittest.main()


