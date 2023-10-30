
import unittest
import func


class TestFuncMethods(unittest.TestCase):
    testVal = 1
    
    def test_FuncFail(self):
        print(self.testVal)
        try:
            self.testVal = 2
            self.assertEqual(func.func(self.testVal), 2)
        except AssertionError:
            print("expected exception caught")
        else:
            raise Exception("failed")
        
    def test_FuncPass(self):
        print(self.testVal)
        self.assertEqual(func.func(self.testVal), 2)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestFuncMethods('test_FuncFail'))
    suite.addTest(TestFuncMethods('test_FuncPass'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

